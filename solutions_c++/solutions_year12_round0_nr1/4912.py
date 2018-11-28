/*
 * \author Alexej Fink, fink.alexej@googlemail.com
 * yep, python would be a smarter choice for this job.
 */

#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <memory>
#include <vector>

using namespace std;
       
typedef unsigned char uchar;

//===================================================================

bool readfile( const char* infile, string& outbuffer) 
{
  outbuffer.clear();

  struct stat status;
  int ret= stat( infile, &status);
  if (ret != 0) {
    cerr << "[E] Failed to stat file: " << infile << ", err: " << errno << ", " << strerror(errno) << endl;
    return false;
  }

  off_t filelen= status.st_size;
  
  int fd= open(infile, O_RDONLY);
  if (fd == -1) {
    cerr << "[E] Failed to open file: " << infile << ", err: " << errno << ", " << strerror(errno) << endl;
    return false;
  }
  
  bool ok= false;
  
  char* buf= new char[filelen];
  int got= read( fd, buf, filelen);
  if (filelen != got) {
    cerr << "[E] failed to read from file, got " << got << ", from " << filelen << endl;
    if (got == -1) {
      cerr << "  err: " << errno << ", " << strerror(errno) << endl;
    }
  }
  else {
    ok= true;
    cout << "[I] read data from input file " << infile << ", len: " << filelen << endl;
    outbuffer.assign(buf);
  }
    
  close(fd);
  delete[] buf;
  
  return ok;
}

//===================================================================

uchar ascii[256];  // ascii-index to grese symbol
uchar grese[256];  // grese-index to ascii symbol
uchar maped[256];
const char* encSample= ""
"ejp mysljylc kd kxveddknmc re jsicpdrysi\n"
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n"
"de kr kd eoya kw aej tysr re ujdr lkgc jv zq\n";
// Google "forgot" to use the symbols 'z' 	and 'q' in original message...

const char* plainSample= ""
"our language is impossible to understand\n"
"there are twenty six factorial possibilities\n"
"so it is okay if you want to just give up qz\n";

//===================================================================

bool calcChiffre()
{
  for (int i=0; i < 256; ++i) {
    ascii[i]= i;
    grese[i]= i;
    maped[i]= 0;
  }
  
  cout << "[I] calculate chiffre from sample." << endl
    << "encoded: " << endl << encSample << endl
    << "decoded: " << endl << plainSample << endl;
  
  const uchar* plainPtr= (const uchar*)plainSample;
  const uchar* encPtr= (const uchar*)encSample;
  
  while ( *plainPtr != 0 && *encPtr != 0)
  {
    uchar enc= *encPtr;
    uchar plain= *plainPtr;
    if (grese[enc] != enc)
    {
      // check, the chiffre is consistent
      if (grese[enc] != plain) {
	cerr << "[E] about to remap coding!, have grese[" << (int)enc << "]==" << (int)grese[enc] << ", new: " << (int)plain << endl;
	return false;
      }
      else {
	// mapping is already registered
      }
    }
    else {
      grese[enc]= plain;
      ascii[plain]= enc;
//      cerr << "[V] new mapping! grese[" << (int)enc << "]-> " << (int)plain << endl;
    }
    
    ++plainPtr;
    ++encPtr;
  }
  
  if (*plainPtr != *encPtr) {
    cerr << "[E] non equal in/out chiffred sample!" << endl;
    return false;
  }

  cout << "[V] ==== mapping" << endl;
  int remapped= 0;
  for (int i='a'; i <= 'z'; ++i)
  {
    uchar c= grese[i];
    if (isalnum(c)) {
      cout << "g->a sym " << setw(3) << (uchar)i << "->" << grese[i] << " and back " << ascii[(int)grese[i]];
    }
    else {
      cout << "g->a num " << setw(3) << (int)i << "->" << (int)grese[i] << " and back " << (int)ascii[(int)grese[i]];
    }

    if (grese[i] != i ) {
      ++remapped;
    }
    else {
      cout << " [W] unmapped symbol!";
    }
    cout << endl;
    
  }
  cout << "[V] remapped symbols: " << remapped << endl;
}

//===================================================================

void decodeString( const string& encoded, string& decoded)
{
  decoded.clear();
  decoded.reserve(encoded.size());
  
  for (int i=0, iEnd= encoded.size(); i < iEnd; ++i) {
    uchar c= encoded[i];
    decoded.push_back(grese[c]);
  }
}

void decodeBuffer( const uchar* encoded, uchar* decoded, int len)
{
  for (int i=0; i < len; ++i) {
    uchar c= encoded[i];
    decoded[i]= grese[c];
  }
}

//===================================================================

const int BLOCK= 4 << 20;
char blob[BLOCK];
char resLine[BLOCK + 16];
  

int main ( int argc, const char* argv[])
{
  cout << endl << "Googlerese decoder, by fink.alexej@googlemail.com" << endl << endl;
  
  if (argc == 1 || argc > 3) {
    cout << "USAGE: " << argv[0] << " googlerese-encoded-file [output file]";
    return 0;
  }
  
  calcChiffre();

  // test chiffre
  string encoded(encSample);
  string decoded;
  decodeString( encoded, decoded);
  
  if (decoded.compare(plainSample) != 0) {
    cerr << "[E] sample test failed!" << endl;
    return 1;
  }
  // read given input file
  const char* infile= argv[1];
  
  ifstream is;
  is.open( infile, ifstream::in);
  
  if (is.fail()) {
    cerr << "[E] Failed to open input file " << infile << endl;
    return 1;
  }
  
  typedef std::vector<string> TResVec;
  TResVec result;

  // get expected line count
  char lc[16];
  is.getline( lc, 16);
  
  errno= 0;
  const int lineCout= atoi(lc);
  if (errno != 0) {
    cerr << "[E] failed to parse line count! err: " << strerror(errno) << endl;
    return 1;
  }
  
  // process all line by line
  //std::vector<string> blobs;

  while (is.good())
  {
    is.getline( blob, BLOCK);
    int got= is.gcount();
    if (got == BLOCK) {
      cout << "[W] line is too long for a single buffer" << endl;
    }
    else if (got == 0) {
      break;
    }
    
    // TODO: don't put 'case #' if prev line did not end with \n
    int off= sprintf( resLine, "Case #%u: ", (unsigned int)result.size() + 1);  // TODO: add case# in output loop.
    char* outp= resLine + off;
    
    decodeBuffer( (uchar*)blob, (uchar*)outp, got);
    result.push_back(string(resLine));
    
    // TODO: flush results, if used too much memory.
  }
  if (!is.eof()) {
    cerr << "[E] Failure, whire reading from input file: " << infile << endl;
    return 1;
  }
  
  if (lineCout != result.size()) {
    cout << "[W] expect " << lineCout << " lines, but collected: " << result.size() - 1 << endl;
  }
  
  ofstream of;
  if (argc == 3) {
    // write output also to filelen
    of.open( argv[2], ios_base::trunc);
    if (!of.good()) {
      cerr << "[E] Failed to open output file: " << argv[2] << endl;
    }
  }

  cout << " === decoded result ===" << endl;
  TResVec::iterator it= result.begin();
  TResVec::iterator itEnd= result.end();
  for ( ;it  != itEnd; ++it) {
    cout << *it << endl;
    if (of.good()) {
      of << *it << endl;
    }
  }
  
  if (of.is_open()) {
    of.close();
  }

  return 0;
}

//===================================================================
