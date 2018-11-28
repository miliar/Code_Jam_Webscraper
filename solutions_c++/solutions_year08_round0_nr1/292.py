#include <cstdio>
#include <string>
#include <map>
#include <iostream>
using namespace std;
const int c=1000;
const int inf=1000000000;
int a[c+1];
typedef char str[c+1];
map<string,int> s;
int n,m,kd;
int r[c+1][c+1];
void solve(int ii) {
	int i,j,k,ans;
	memset(r,0,sizeof(r));
	for (i=1; i<=n; ++i) if (i!=a[1]) r[1][i]=0; else r[1][i]=inf;
	for (i=2; i<=m; ++i)
		for (j=1; j<=n; ++j) {
			r[i][j]=inf;
			if (a[i]==j) continue;
			if (r[i-1][j]<inf) r[i][j]=r[i-1][j];
			for (k=1; k<=n; ++k) if (k!=j) if (r[i][j]>r[i-1][k]+1) r[i][j]=r[i-1][k]+1;
		}
	ans=inf;
	for (i=1; i<=n; ++i) if (r[m][i]<ans) ans=r[m][i];
	printf("Case #%d: %d\n",ii,ans);
}				
int main() {
	int i,ii;
	str temp;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kd);
	for (ii=1; ii<=kd; ++ii) {
		scanf("%d\n",&n);
		s.clear();
		for (i=1; i<=n; ++i) {
			gets(temp);
			s[temp]=i;
			cerr << temp << '\n';
		}
		scanf("%d\n",&m);
		for (i=1; i<=m; ++i) {
			gets(temp);
			cerr << temp << '\n';
			a[i]=s[temp];
		}
		for (i=1; i<=m; ++i) cerr << a[i] << ' ';
		cerr << '\n';
		solve(ii);
	}
	return 0;
}
	