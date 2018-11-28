// GCJ 2008 - Otaku

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


int isdiv(long long x)
{
	return (!(x%2) || !(x%3) || !(x%5) || !(x%7));
}

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

		string s = io.getstring();

		int v[40];
		char o[40];
		int n = s.size();
		int m = n-1;
		long long poss,x,oper;
		int stop,op;

		for (i=0 ; i<n ; i++) v[i] = (int)(s[i] - '0');
		for (i=0 ; i<m ; i++) o[i] = 0;
		o[i] = 1;


		poss = 0;


		if ( ! m)
		{
			poss = (isdiv(v[0]) ? 1:0);
		}
		else
		{
			int end = 0;

			while ( ! end)
			{
				/* 
				for (i=0 ; i<n ; i++) 
				{
					printf ("%d", v[i]);
					if (o[i]) printf ("%c", (o[i]==1 ? '+':'-'));
				}
				printf ("\n");
				*/


				x = oper = op = 0;

				for (i=0 ; i<n ; i++)
				{
					// . + -
					oper = oper*10 + v[i];
					if (o[i])
					{
						if ( ! op) x = oper;
						else
						{
							x += (op == 1 ? 1:-1) * oper;
						}
						op = o[i];
						oper = 0;
					}
				}

				if (isdiv(x)) poss++;

				stop = i = 0;

				while (!stop && i<m)
				{
					if (++o[i] <= 2)
					{
						stop = 1;
					}
					else
					{
						o[i++] = 0;
					}
				}

				if (i >= m) end = 1;
			}
		}


		// ---

		InOut::result(cas, poss);
	}
}
