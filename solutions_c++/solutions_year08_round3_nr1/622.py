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

void readFile(string);
void process(string);

vector<int> ivec;



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

void process ( string outName)
{
  ofstream ofile(outName.c_str());
  int count = 0;

  vector<int>::iterator itr1 = ivec.begin();

  ++itr1;

  while ( itr1 !=  ivec.end() )
  {
    ++count;


    int P = *itr1;
    ++itr1;
    int K = *itr1;
    ++itr1;
    int L = *itr1;
    ++itr1;

    vector<int> letters;
    for ( int i = 0 ;i < L ; ++i)
    {
      letters.push_back(*itr1);
      ++itr1;
    }

    sort(letters.begin(), letters.end());
    int presses = 0;

    int mul = 1;
    for ( int i = L -1; i >=0 ; --i)
    {
        if ( (L - i ) > mul * K )
          ++mul;
        presses += mul * letters[i];
    }
    
    ofile << "Case #" << count << ": " << presses << "\n";

  }

}

void readFile(string inName)
{
  ifstream ifile(inName.c_str());

  istream_iterator<int> start(ifile);
  istream_iterator<int> end;

  copy(start, end, back_inserter(ivec));
}

