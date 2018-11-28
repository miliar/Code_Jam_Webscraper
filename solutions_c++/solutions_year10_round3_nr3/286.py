#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <map>
using namespace std;

int ansz,test,testcase,i,j,n,m,f[550][550];
int a[550][550];
int d[550][2];
map<int,int> ans;

bool dp()
{
	int i,j,k,nowlen,x,y;
	ansz=0;
	for (i=1; i<=n; ++i)
		for (j=1; j<=m; ++j)
			if (a[i][j]!=-1) {
				f[i][j]=1;
				ansz=1;
				x=i; y=j;
			}
			else {
				f[i][j]=-1;
			}
			
	for (i=2;i<=n;i++)
		for (j=2;j<=m;j++)
			if ((a[i][j]==a[i-1][j-1])&&(a[i][j]!=a[i-1][j])&&(a[i-1][j]==a[i][j-1])&&
				a[i][j]!=-1 && a[i-1][j-1]!=-1 && a[i-1][j]!=-1 && a[i][j-1]!=-1) {
				f[i][j]=min(f[i-1][j-1],min(f[i][j-1],f[i-1][j]))+1;
				if (ansz<f[i][j]) {
					ansz=f[i][j];
					x=i; y=j;
		        }
			}
	if (ansz>=1) {
		if (ans.find(ansz)!=ans.end()) ++ans[ansz];
		else ans[ansz]=1;
		for (i=x-ansz+1; i<=x; ++i)
			for (j=y-ansz+1; j<=y; ++j)
				a[i][j]=-1;
		return true;
	}
	else return false;
///	printf("%d\n",ansz);
}
char ch;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&testcase);
	for (test=1; test<=testcase; ++test) {
		scanf("%d%d\n",&n,&m);
		for (i=1; i<=n; ++i) {
			int l=0,x;
			for (j=1; j<=m/4; ++j) {
				scanf("%c",&ch);
				if (ch>='A' && ch<='Z') {
					x=ch-'A'+10;
				}
				else x=ch-'0';
		        a[i][l+4]=x&1;
				a[i][l+3]=(x>>1)&1;
				a[i][l+2]=(x>>2)&1;
				a[i][l+1]=(x>>3)&1;
				l+=4;
			}
			scanf("\n");
		}
		ans.clear();
		while (dp());
		printf("Case #%d: %d\n",test,ans.size());
		int x=0;
		for (map<int,int>::iterator it=ans.begin(); it!=ans.end(); ++it) {
			++x;
			d[x][0]=it->first;
			d[x][1]=it->second;
		}
		for (int it=ans.size(); it>=1; --it)
			printf("%d %d\n",d[it][0],d[it][1]);
	}
	return 0;
}