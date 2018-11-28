#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<complex>
#define mp make_pair
#define pb push_back
#define all(x) (x.begin(),x.end())
using namespace std;
typedef __int64 ll;
ll a=0,ans;
char s[70];
int l;
void dfs(int p)
{
//	printf("%d\n",p);
	if (p==l)
	{
		if (s[0]=='0')return;
		ll a=0;
		for (int i=0;i<l;i++)
		{
			a=a*2+s[i]-'0';
		}
		if (!a)return;
		ll t=(ll)(sqrt(a*1.0)+0.5);
		if (t*t==a)
		{
			cout<<s<<endl;
		}
		ans=1;
		return;
	}
	//if (ans>0)return;
	if (s[p]=='?')
	{
		s[p]='0';
		dfs(p+1);
		s[p]='1';
		dfs(p+1);
		s[p]='?';
		return;
	}
	dfs(p+1);
}
int main()
{
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%s",s);
		l=strlen(s);
		ans=-1;
		a=0;
		printf("Case #%d: ",++cc);
		dfs(0);
	}
	return 0;
}
