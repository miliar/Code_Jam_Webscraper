#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for(i = 0;i<n;i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
#define eps (1e-11)
#define inf (1<<29)

int max(int a,int b)
{
	if(a>b) return a;
	else return b;
}
int min(int a,int b)
{
	if(a<b) return a;
	else return b;
}
#define MX 41
char a[MX][MX];
int n;
bool ok(string s,int a)
{
	int i;
	for(i = 0;i<s.size();i++)
	{
		if(s[i]=='1'&&i>a)
			return 0;
	}
	return true;
}
int findap(int p)
{
	int i = p,j;
	int k;
	for(k = 0;k<n;k++,i++)
		if(ok(a[i],p))
		{
			char tmp[MX];
			strcpy(tmp,a[i]);
			for(j = i-1;j>=p;j--)
				strcpy(a[j+1],a[j]);
			strcpy(a[p],tmp);
			return k;
		}
}
int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.txt","w",stdout);
	int tc,i,fg = 1;
	cin>>tc;
	while(tc--)
	{
		int i;
		cin>>n;
		for(i = 0;i<n;i++)
		{
			scanf("%s",&a[i]);
		}
		int ret = 0;
		FOR(i,n)
		{
			ret+=findap(i);
		}
		printf("Case #%d: %d\n",fg++,ret);

	}
	
	return 0;
}