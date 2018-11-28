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

int T,n,D,pos[10010],len[10010],f[10010];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%d%d",&pos[i],&len[i]);
		scanf("%d",&D);
		f[0]=pos[0];
		for(int i=1;i<n;i++)
		{
			f[i]=-1;
			for(int j=0;j<i;j++) if (f[j]>=0&&f[j]>=pos[i]-pos[j])
				f[i]=max(f[i],min(pos[i]-pos[j],len[i]));
		}
		int ans=0;
		for(int i=0;i<n;i++) if (f[i]!=-1&&D-pos[i]<=f[i]) ans=1;
		printf("Case #%d: ",tt);
		if (ans) puts("YES"); else puts("NO");
	}
	
	return 0;
}
