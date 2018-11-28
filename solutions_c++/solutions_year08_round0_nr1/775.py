#include<iostream>
#include<map>
using namespace std;
const int MXS=110;
const int MX=100000000;
char t[200];
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int c,n;
	scanf("%d\n",&n);
	for (c=1;c<=n;++c) {
		int s,i;
		scanf("%d\n",&s);
		map<string,int> index;
		for (i=0;i<s;++i) {
			gets(t);
			index[t]=i;
		}
		int f[MXS]={0};
		int q,j;
		scanf("%d\n",&q);
		for (i=1;i<=q;++i) {
			gets(t);
			int d=index[t];
			f[d]=MX;
			for (j=0;j<s;++j)
				if (j!=d) f[d]=min(f[d],f[j]+1);
		}
		int ans=MX;
		for (j=0;j<s;++j)
			ans=min(ans,f[j]);
		printf("Case #%d: %d\n",c,ans);
	}
}
