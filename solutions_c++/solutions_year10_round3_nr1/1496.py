#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back


int main()
{
    freopen("A-small-attempt5.in", "r", stdin);
    freopen("A-small-attempt5.out", "w", stdout);

    int t;
    cin >> t;
    REP (tt, t)
    {

        int nline;
        int A1, B1,A2,B2,count=0;
	 scanf("%d", &nline);
    //cin >>nline;
	if (nline==2)
	{
		scanf("%d %d", &A1,&B1);
		scanf("%d %d", &A2,&B2);
	  if ((A1-A2)*(B1-B2)<0)
       count=count+1;
	}
	else if (nline=1){
		scanf("%d %d", &A1,&B1);
	   count=0;
	}
	else
      count=0;
      cout <<"Case #" << (tt+1) << ": "<<count<<endl;
	}
	return 0;
}
