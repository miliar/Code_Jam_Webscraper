// pros.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <iterator>
#include <bitset>

using namespace std;

#include <stdio.h>

void readFile(string);
void process(string);

vector<string> svec;

void readFile(string inName);
void process( string outName);

int main(int argc, char * *argv)
{
  if( 3 != argc)
  {
    cout << endl << "Incorrec args" << endl;
     return -1;
  }
  readFile(string(argv[1]));
  process(string(argv[2]));
	return 0;
}

vector<int> Gno;
int Gsize = 0;
int Gcnt = 0;


void solve (long long  int sum, int pos, int prevpos, int type)
{
  long long  int tmp = 0;
  for ( int i = prevpos+1; !(i > pos) ; ++i)
  {
    tmp = tmp * 10 + Gno[i];
  }
  if ( pos == Gsize-1 )
  {
    if ( type == 1 )
      sum += tmp;
    else
      sum -= tmp;

    if ( sum == 0 || 
        (sum%2 == 0) || 
        (sum%3 == 0) ||
        (sum%5 == 0) ||
        (sum%7 == 0) )
    {
      ++Gcnt;
    }
    return;
  }

  solve ( sum, pos+1, prevpos, type);

  if ( type == 2 )
    sum -= tmp;
  else
    sum += tmp;

  solve (sum, pos+1, pos, 1);
  solve (sum, pos+1, pos, 2);
}
void process ( string outName)
{
  ofstream ofile(outName.c_str());
  int count = 1;

  vector<string>::iterator itr1 = svec.begin();
  ++itr1;
  char c[2];
  c[1] = '\0';

  while ( itr1 != svec.end() )
  {
    string tmp = *itr1;
    ++itr1;
    int strSize = tmp.size();
    Gno.clear();
    
    
    for ( int i = 0; i < strSize ; ++i)
    {
      Gno.push_back(tmp[i]-48);
    }
    Gsize = Gno.size();
    Gcnt = 0;
    
    solve(0, 0, -1, 1);
      
    ofile << "Case #" << count << ": " << Gcnt << "\n";

    ++count;
  }

}

void readFile(string inName)
{
  ifstream ifile(inName.c_str());

  istream_iterator<string> start(ifile);
  istream_iterator<string> end;

  copy(start, end, back_inserter(svec));
}
