#include <iostream>
#include <set>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <math.h>
#include <cstdlib>
#include <memory.h>
#include <sstream>
#include <assert.h>

using namespace std;

#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)>(0)?(a):(-(a)))
#define mp make_pair
#define pnt pair<int,int>
#define MEMS(a,b) memset((a),(b),sizeof(a))
#define pb push_back
#define LL long long
#define U unsigned
bool check(LL k)
{
	LL l=0,r=2000000000;
	while (l<=r)
	{
		LL m=(l+r)/2;
		if (m*m==k)
			return true;
		if (m*m>k)
			r=m-1;
		else
			l=m+1;
	}
	return false;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(test,1,t+1)
	{
		printf("Case #%d: ",test);
		string s;
		cin>>s;
		int num=0;
		FOR(i,0,s.size())
			if (s[i]=='?')
				num++;
		int p=(1<<num);
		FOR(it,0,p)
		{
			int cnt=0;
			string s1=s;
			FOR(j,0,s.size())
			{
				if (s[j]=='?')
				{
					if ((it>>cnt)&1)
						s[j]='1';
					else
						s[j]='0';
					cnt++;
				}
			}
			LL num=0;
			LL p=1;
			for (int i=(int)s.size()-1; i>=0; --i)
			{
				num+=p*(s[i]-'0');
				p*=2;
			}
			if (check(num))
			{
				cout<<s<<endl;
				break;
			}
			s=s1;
		}
	}
	return 0;
}