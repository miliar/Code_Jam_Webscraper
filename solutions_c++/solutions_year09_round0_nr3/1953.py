#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front
#define BN begin()
#define RN rbegin()
#define RD rend()
#define ED end()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it)
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it) 
#define VV(X) vector < vector< X > >
#define PIB(X)  pair<IT(X),bool >  

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;	/*}}}*/

string str;
int c[20][505];
int main()
{
	int cas;
	cin>>cas;
	string s="welcome to code jam";
	int l=s.length();
//	int a[20];
/*	FOR(i,0,20)
	{
	//	a[i]=i;
		c[i]=0;
	}*/
	getline(cin,str);
	FOR(t,0,cas)
	{

		getline(cin,str);
//		cout<<str<<endl;
		int len=str.length();

//			c[0][i]=0;
		FOR(i,0,l+1)
			FOR(j,0,len+1)
				c[i][j]=0;
		
		int ans=0;
		FOR(i,0,len)
			c[0][i]=1;
		FOR(i,0,l)
		{
			FOR(j,0,len)
			{
				c[i+1][j+1]=c[i+1][j];

				if(str[j]==s[i])
				{
					c[i+1][j+1]+=c[i][j];
				}

				c[i+1][j+1]%=1000;
//				if(i==l-1)
//					ans+=c[i+1][j+1];
			}
				
		}
		cout<<"Case #"<<t+1<<": ";
		printf("%04d\n",c[l][len]);//<<endl;
	}	
	return 0;
}
