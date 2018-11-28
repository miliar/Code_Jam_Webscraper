#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <deque>
#include <algorithm>
#include <complex>
using namespace std;


typedef long long LL;
typedef pair<int,int> PII;

#define pb push_back
#define mp make_pair
#define sz size()
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)<(0)?-(a):(a))
#define HAS(x,k) ((x).find(k)!=(x).end())
#define sqr(a) ((a)*(a))

#define PREV(x) ((x)&((x)-1))
#define NEXT(x) (((x)<<1) - PREV(x))

struct node
{
	string s;
	map<string,int> n;
};
node A[100000];
int size=0;
int add(string s)
{
	FOR(i,0,s.sz) if (s[i]=='/') s[i]=' ';
	istringstream iss(s); 
	int p=0;
	string t;
	int res=0;
	while(iss>>t)
	{
		if (!HAS(A[p].n,t))
		{
			++res;
			A[size].s=t;
			A[size].n.clear();
			A[p].n[t]=size;
			++size;
		}
		p=A[p].n[t];
	}
	return res;
}



int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int t; scanf("%d",&t);
	int tc=0;
	while(t--)
	{
		++tc;
		
		int N,M; scanf("%d%d",&N,&M);
		size=1;
		A[0].s="root";
		A[0].n.clear();
		FOR(i,0,N)
		{
			string s; cin >> s;
			add(s);
		}
		int r=0;
		FOR(i,0,M)
		{
			string s; cin >> s;
			r+=add(s);
		}
		printf("Case #%d: %d\n",tc,r);
	}


	
	
	return 0;
}