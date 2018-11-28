// GCJ 2008 - Otaku - A

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

#define BUFSIZE 100000

typedef long long bigi;
typedef long double bigd;

// --- common classes / functions ---


void error (char *s) { exit(printf("%s\n", s)); }


class InOut {
  FILE *finput;
  char *buffer;
  int i;
public:
  int eof,counter,len;
  InOut(char *fname)
  {
	  finput = fopen (fname, "r");
	  if ( ! finput) error ("Cannot open input file");

	  buffer = (char *)malloc(BUFSIZE);
	  if ( ! buffer) error ("Malloc :-(");

	  len = counter = eof = 0;
  }
  ~InOut() { free(buffer) ; fclose(finput); }

  vector<string> split (string s, string sep)
  {
	  vector<string> output;
	  int p,pos=0;
	  do {
		  if ((p = s.find(sep, pos)) == string::npos) output.push_back(s.substr(pos));
		  else {
			  output.push_back(p-pos ? s.substr(pos, p-pos):"");
			  pos = p + sep.size();
		  }
	  } while (p != string::npos);
	  return (output);
  }

  char *getline()
  { 
	  *buffer = 0;
	  if (fgets (buffer, BUFSIZE, finput)) counter++;
	  else eof = 1;
	  len = strlen(buffer);
	  while (len && (buffer[len-1]==10 || buffer[len-1]==13)) buffer[--len] = 0;
	  return (buffer);
  }
  void getvector(vector<string> &vs) { vs = split(string(getline()), " "); }
  string getstring () { return string(getline()); }
  int getint()        { return atoi(getline()); }
  double getdouble()  { return atof(getline()); }
  void getvint(vector<int> &vi)
  { 
	  vector<string> vs;
	  getvector(vs);
	  for (i=0 ; i<vs.size() ; i++) vi.push_back(atoi(vs[i].c_str()));
  }
  void getvdouble(vector<double> &vd)
  { 
	  vector<string> vs;
	  getvector(vs);
	  for (i=0 ; i<vs.size() ; i++) vd.push_back(atof(vs[i].c_str()));
  }
  

  template<class T> static void result(int cas, T res)
  {
	  cout << "Case #" << cas << ": " << res << endl;
  }
};


// --- (end) ---



// -- M A I N   C O D E ---


main (int argc, char **argv)
{
	if (argc < 2) error ("Missing input file :-)");

	InOut io(*++argv);

	int cas = 0, T = io.getint();

	int i;

	while ( T-- )
	{
		cas++;

		// ---

		int per,keys,let;
		vector<int> v,freq;
		
		io.getvint(v);
		per = v[0];
		keys = v[1];
		let = v[2];

		io.getvint(freq);

		sort(freq.begin(), freq.end());

		int level=1;
		int nk=0;
		long long used=0;
		int f;

		for (i=freq.size()-1 ; i>=0 ; i--)
		{
			f = freq[i];

			if (f)
			{
				if (++nk > keys)
				{
					nk = 1;
					level++;
				}
				used += (long long)level * (long long)f;
			}
		}

		// ---

		InOut::result(cas, used);
	}
}
