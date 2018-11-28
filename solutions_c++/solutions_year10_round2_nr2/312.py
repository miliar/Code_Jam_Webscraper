#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <assert.h>

using namespace std;
typedef long long ll;

const double PI=acos(-1.0);
const double eps=1e-11;

#define dump(x) cerr<<#x<<" = "<<(x)<<endl;
#define foreach(c,itr) for (__typeof( (c).begin() ) itr=(c).begin();itr!=(c).end() ;itr++ )


int countbit(int n) {return (n==0)?0:1+countbit(n&(n-1));}
int lowbit(int n) {return n&(n^(n-1));}
string toString(ll v) { ostringstream sout;sout<<v;return sout.str();}
string toString(int v) { ostringstream sout;sout<<v;return sout.str();}
int Rand16(){return rand();}
int Rand32(){return rand()*rand();}
double DRand(){return (double)rand()/RAND_MAX;}
int RandRange(int f,int r){return f+(int)(DRand()*(r-f)+0.5);}



const int MAX =50+5;

int T,cas;
int n,k,b,t;
ll x[MAX],v[MAX];
bool ok[MAX];

int main()
{
	int i,j;

	freopen("B-large.in","r",stdin);
	freopen("out","w",stdout);

	cas=0;
	scanf("%d",&T);
	while (T--)
	{
		cas++;
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for (i=0;i<n;i++)
			cin>>x[i];
		for (i=0;i<n;i++)
			cin>>v[i];


		for (i=0;i<n;i++)
		{
			if (x[i]+v[i]*t<b) ok[i]=false;
			else
				ok[i]=true;
		//	printf("ok[%d]=%d\n",i,ok[i]);
		}



		int ans=0;
		int get=0;
		int ob=0;

		for (i=n-1;i>=0 && get<k;i--)		
			if (ok[i])
			{
				ans+=ob;
				get++;
			}
			else
				ob++;
		if (get<k)
			printf("Case #%d: %s\n",cas,"IMPOSSIBLE");
		else
			printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
