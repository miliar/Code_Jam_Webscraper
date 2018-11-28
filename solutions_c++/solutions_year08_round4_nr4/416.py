#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>

using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b_);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

string Do(string a,vector<int >&v)
{
	int n=SZ(a);
	int k=SZ(v);
	int ped=n/k;
	string res;
	int ini=0;
	REP(i,ped)
	{
		string h;
		REP(j,k)
		{
			h+=a[v[j]+ini];
		}
		res+=h;
		ini+=k;
	}
	return res;
} 
int Si(string &a)
{
	int n=SZ(a),q=0,i=0;
	while (i<n)
	{
		char p=a[i];
		while (i<n&&a[i]==p)
			i++;
		q++;
	}
	return q;
}
char Pal[10000];
int main ()
{
	int c,cas=1;
	scanf ("%d",&c);
	freopen ("output","w",stdout);
	while (c--)
	{
		int k;
		
		scanf ("%d",&k);
		scanf ("%s", Pal);
		vector<int> V(k);
		REP(i,k)
		{
			V[i]=i;
		}
		int res=strlen(Pal);
		do
		{
			string app= Do(Pal,V);
			res=min (res,Si(app));
		}
		while(next_permutation(ALL(V)));
		printf ("Case #%d: ",cas++);
		
		printf ("%d",res);
		printf ("\n");
	}
	fclose(stdout);
}


