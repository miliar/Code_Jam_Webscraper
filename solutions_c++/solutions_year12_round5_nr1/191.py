/*
	Author : ChnLich
*/
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<string>
#include<bitset>
#include<functional>
#include<utility>

using namespace std;

typedef long long llint;
typedef pair<int,int> ipair;
#define fi first
#define se second
#define mp make_pair

void read(int &k)
{
	k=0; char x=getchar();
	while(x<'0'||x>'9') x=getchar();
	while(x>='0'&&x<='9') { k=k*10-48+x; x=getchar(); }
}

int n,T,a[1010],l[1010],k;
double p[1010];

int sgn(double x,double y)
{
	if (fabs(x-y)<1e-8) return 0;
	return x>y?1:-1;
}

bool cmp(int x,int y)
{
	int t=sgn(l[x]*p[y],l[y]*p[x]);
	return t<0||(t==0&&x<y);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++) scanf("%d",&l[i]);
		for(int i=1;i<=n;i++) scanf("%d",&k),p[i]=k/100.0;
		for(int i=1;i<=n;i++) a[i]=i;
		stable_sort(a+1,a+n+1,cmp);
		printf("Case #%d: ",tt);
		for(int i=1;i<n;i++) printf("%d ",a[i]-1);
		printf("%d\n",a[n]-1);
	}
	
	return 0;
}
