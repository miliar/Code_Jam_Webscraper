#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64

int64 tt(long n)
{
  if(n==1) return 1;
  if(n==2) return 0;
  return n-1;
}

int main()
{
  string Ts;
  long T;

  getline (cin,Ts);
  T = atoi(Ts.c_str());

  for( int t=1; t<=T; ++t )
    {
      string s;
      cin >>s;
      map<char,int64> D;
      D[s[0]] = 1;
      int ns = s.size();

      for( int i = 1; i < ns; ++i)
	{
	  if(D.find(s[i]) == D.end())
	    {
	      int e = D.size();
	      D[s[i]]=tt(e+1);
	    }
	}
      
      int64 ans=0;
      int64 b = D.size();
      if(b<2) b = 2;
      int64 p = 1;
      for( int i = ns-1; i>=0; --i)
	{
	  ans+=D[s[i]]*p;
	  p*=b;
	  
	}

      //      cout <<"debug ";
      //      for(int i =0; i < ns; ++i) cout <<D[s[i]]; cout<<endl;

      cout <<"Case #"<<t<<": ";
      cout <<ans<<endl;
    }
}
