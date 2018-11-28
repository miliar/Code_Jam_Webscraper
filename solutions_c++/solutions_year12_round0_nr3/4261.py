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

ifstream fin ("jam.in");
ofstream fout ("out.txt");

//const int lol=1000000;
//const int inf=1000000;

int t;
long long res=0;

int main()
{
  fin>>t;
  for (int i=0 ; i<t ; i++)
    {
      int a, b;
      fin>>a>>b;
      res=0;
      
      for (long long n=a ; n<b ; n++)
	for (long long m=n+1 ; m<=b ; m++)
	  {
	    stringstream s1, s2;
	    s1<<n; s2<<m; 

	    if (s1.str().length()!=s2.str().length()) continue;

	    string x=s1.str()+s2.str();
	    string tmp1="", tmp2="", tmp3="", tmp4="";
	    
	    for (int k=1 ; 2*k<x.length() ; k++)
	      {
		tmp1=x.substr(0, (x.length()/2)-k);
		tmp2=x.substr((x.length()/2)-k, k);
		tmp3=x.substr((x.length()/2), k);
		tmp4=x.substr((x.length()/2)+k);
		if (tmp1==tmp4 && tmp2==tmp3) {if (i==-1) cout<<x<<nl; res++;}

		tmp1=""; tmp2=""; tmp3=""; tmp4="";
	      }
	  }

      fout<<"Case #"<<i+1<<": "<<res<<nl;
    }
}
