/*
 * Christopher J. Hanks <chanks.met@gmail.com>
 */
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <string>
#include <fstream>

using std::ofstream;
using std::ifstream;
using std::cerr;
using std::endl; 
using std::string;
using std::stringstream;

#define CHAR_SHIFT(_INP_) _INP_ %32 

static char _G_map[26+1];

bool learn_map(void);
bool translate(string& input);

int 
main(int argc, char* argv[])
{
  if (argc != 3)
    {
      cerr << "Missing args..." << endl;
      return 1;
    }

  if (!learn_map())
    {
      cerr << "Failed to learn from seeds / maps " << endl;
      return 1;
    }

  ifstream input(argv[1]);
  ofstream output(argv[2]);
  string buffer;

  std::getline(input, buffer);
  size_t cnt = atoi(buffer.c_str());
  cerr << "Count: " << cnt << endl;
  for (size_t i=0; i<cnt; ++i)
    {
      std::getline(input, buffer);
      translate(buffer);

      output << "Case #" << i+1 << ": " << buffer << endl; 
    }
  output.close();

  return 0;
}

bool 
learn_map()
{
  memset(_G_map, '\0', sizeof(_G_map));
  
  /* program the knowns */
  _G_map[CHAR_SHIFT(' ')] = ' ';
  _G_map[CHAR_SHIFT('a')] = 'y';
  _G_map[CHAR_SHIFT('o')] = 'e';
  _G_map[CHAR_SHIFT('z')] = 'q';

  /* program the seeds */
  stringstream seed_istrm;
  seed_istrm << "ejp mysljylc kd kxveddknmc re jsicpdrysi"
             << "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
             << "de kr kd eoya kw aej tysr re ujdr lkgc jv"
             ;
  
  stringstream seed_ostrm;
  seed_ostrm << "our language is impossible to understand"
             << "there are twenty six factorial possibilities"
             << "so it is okay if you want to just give up"
             ;

  string istr = seed_istrm.str();
  string ostr = seed_ostrm.str();

  if (istr.size() != ostr.size())
    {
      cerr << "Mismatched seeds." << endl;
      return false;
    }

  for (size_t i=0; i<istr.size(); ++i)
    {
      if (istr[i] == ' ')
        continue; 
 
      _G_map[CHAR_SHIFT(istr[i])] = ostr[i];
    }

  /*
   * The only char not otherwise stated in the in-seed is 'q',
   * the only unaccounted for output char is 'z', so rather than solve I put it
   * explicitly.
   */
  _G_map[CHAR_SHIFT('q')] = 'z';

  /* validate map is complete */
  bool ret=true;
  for (size_t i=0; i<26+1; ++i)
    if (_G_map[i] == '\0')
      {
        ret = false;
        cerr << "Unassigned:" << (i+96) << endl;
      }

  /* vaidate the translation */
  translate(istr);
  if (istr != ostr)
    {
      cerr << "FAILED TRANSLATOR" << endl;
      cerr << istr << endl;
      cerr << ostr << endl;
      return false;
    }

  return ret;
}

bool 
translate(string& input)
{
  for (size_t i=0; i<input.size(); ++i)
    {
      input[i] = _G_map[CHAR_SHIFT(input[i])];
    }
  return true;
}
