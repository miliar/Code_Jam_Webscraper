#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#define ABS(a) ((a>0)?a:-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a<b)?(b):(a))
#define FOR(i,a,n) for (int i=(a);i<(n);++i)
#define FI(i,n) for (int i=0; i<(n); ++i)
#define pnt pair <int,int>
#define mp make_pair
#define PI 3.14159265358979
#define MEMS(a,b) memset(a,b,sizeof(a))
#define LL long long
#define U unsigned
using namespace std;
vector<pnt > a;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	string s;
	getline(cin,s);
	FOR(it,0,test)
	{
		a.clear();
		getline(cin,s);
		stringstream tmp;
		tmp<<s;
		int n;
		tmp>>n;
		FOR(i,0,n)
		{
			string s1;
			int v;
			tmp>>s1>>v;
			if (s1=="O")
				a.push_back(mp(1,v));
			else
				a.push_back(mp(2,v));
		}
		int p1=1,p2=1,t=0,res=0;
		res+=a[0].second;
		t=res;
		if (a[0].first==1)
			p1=res;
		else
			p2=res;
		FOR(i,1,a.size())
		{
			if (a[i].first==a[i-1].first)
			{
				t+=ABS(a[i].second-a[i-1].second)+1;
				res+=ABS(a[i].second-a[i-1].second)+1;
				if (a[i].first==1)
					p1=a[i].second;
				else
					p2=a[i].second;
			}
			else
				if (a[i].first==1)
				{
					int v=ABS(a[i].second-p1);
					t=MAX(0,v-t);
					t++;
					p1=a[i].second;
					res+=t;
				}
				else
				{
					int v=ABS(a[i].second-p2);
					t=MAX(0,v-t);
					t++;
					p2=a[i].second;
					res+=t;
				}
		}
		printf("Case #%d: %d\n",it+1,res);
	}
    return 0;
}