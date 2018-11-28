#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <set>
#include <list>
#include <queue>
#include <memory.h>
#include <stdio.h>
#include <time.h>
 
using namespace std;
 
#define ABS(a) ((a>0)?a:-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a<b)?(b):(a))
#define FOR(i,a,n) for (int i=(a);i<(n);++i)
#define FI(i,n) for (int i=0; i<(n); ++i)
#define pnt pair <int, int>
#define mp make_pair
#define PI 3.14159265358979
#define MEMS(a,b) memset(a,b,sizeof(a))
#define LL long long
#define U unsigned
set <string> s;
string s1;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(it,0,t)
	{
		s.clear();
		int n,m;
		scanf("%d%d",&n,&m);
		FOR(i,0,n)
		{
			cin>>s1;
			FOR(j,1,s1.size())
			{
				if (s1[j]=='/')
				{
					s.insert(s1.substr(0,j+1));
				}
			}
			s.insert(s1+'/');
		}
		int res=0;
		FOR(i,0,m)
		{
			cin>>s1;
			FOR(j,1,s1.size())
			{
				if (s1[j]=='/')
				{
					if (s.find(s1.substr(0,j+1))==s.end())
					{
						++res;
						s.insert(s1.substr(0,j+1));
					}
				}
			}
			if (s.find(s1+'/')==s.end())
			{
				++res;
				s.insert(s1+'/');
			}
		}
		printf("Case #%d: %d\n",it+1,res);
	}
	return 0;
}