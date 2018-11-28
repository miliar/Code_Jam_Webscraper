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
int a[30][30];
vector<pnt > bad;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(it,0,test)
	{
		MEMS(a,-1);
		bad.clear();
		int c;
		scanf("%d",&c);
		string s;
		FOR(i,0,c)
		{
			cin>>s;
			int v1=s[0]-'A';
			int v2=s[1]-'A';
			int v3=s[2]-'A';
			a[v1][v2]=a[v2][v1]=v3;
		}
		int d;
		scanf("%d",&d);
		FOR(i,0,d)
		{
			cin>>s;
			int v1=s[0]-'A';
			int v2=s[1]-'A';
			bad.push_back(mp(v1,v2));
		}
		vector<char> res;
		int n;
		cin>>n>>s;
		FOR(i,0,n)
		{
			int v=s[i]-'A';
			while (res.size()>0)
			{
				int v1=res[res.size()-1]-'A';
				if (a[v][v1]!=-1)
				{
					v=a[v][v1];
					res.pop_back();
				}
				else
					break;
			}
			res.push_back(v+'A');
			FOR(it,0,bad.size())
			{
				bool f1=false,f2=false;
				FOR(j,0,res.size())
				{
					if (res[j]==bad[it].first+'A')
						f1=true;
					if (res[j]==bad[it].second+'A')
						f2=true;
				}
				if ((f1) && (f2))
					res.clear();
			}
		}
		printf("Case #%d: [",it+1);
		FOR(i,0,res.size())
		{
			if (i)
				printf(", ");
			printf("%c",res[i]);
		}
		printf("]\n");
	}
    return 0;
}