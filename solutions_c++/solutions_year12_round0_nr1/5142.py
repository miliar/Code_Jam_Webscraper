//#define NDEBUG
#include <iostream>
#include <fstream>
#include <bitset>
#include <vector>
#include <queue>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <sstream>
#include <string>

using namespace std;
//#define sz(a) int(a.size())
#define all(c) c.begin(),c.end()
#define nl '\n'
#define numofbits(x) __builtin_popcount(x)
#define printv(v) for (long long i=0 ; i<v.size() ; i++) cout<<v[i]<<" "; cout<<nl;
#define printpv(v) for (long long i=0 ; i<v.size() ; i++) cout<<v[i].first<<","<<v[i].second<<" "; cout<<nl;

ifstream fin ("jam2.in");
ofstream fout ("out.txt");

//const int lol=1000000;
//const int inf=1000000;

int t;
string res="";
map<char, char> decode;

int main()
{
  decode['a']='y';
  decode['b']='h';
  decode['c']='e';
  decode['d']='s';
  decode['e']='o';
  decode['f']='c';
  decode['g']='v';
  decode['h']='x';
  decode['i']='d';
  decode['j']='u';
  decode['k']='i';
  decode['l']='g';
  decode['m']='l';
  decode['n']='b';
  decode['o']='k';
  decode['p']='r';
  decode['q']='z';
  decode['r']='t';
  decode['s']='n';
  decode['t']='w';
  decode['u']='j';
  decode['v']='p';
  decode['w']='f';
  decode['x']='m';
  decode['y']='a';
  decode['z']='q';
  decode[' ']=' ';
  fin>>t;

  int k=1;
  string tmp="";
  getline(fin, tmp);
  while (fin.good() && k<=t)
    {
      string inp;
      getline(fin, inp);
      //cout<<inp<<nl;
      res="";

      for (int i=0 ; i<inp.length() ; i++)
	res+=decode[inp[i]];
      
      fout<<"Case #"<<k<<": "<<res<<nl;
      k++;
    }
}
