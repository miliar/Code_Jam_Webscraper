#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<vector>
#include<cmath>
#include<iostream>
using namespace std;
#define mem(a,b) memset(a,b,sizeof(a))
typedef long long ll;
typedef pair<int,int> PII;
const double eps = 1e-7;
const double PI = acos(-1.0);
const int oo = 1<<29;

const int N = 4;

char a[N][N];

int f(char c) {
	for(int i=0;i<N;i++) {
		int ok=1;
		for(int j=0;j<N;j++) if(a[i][j]!=c&&a[i][j]!='T') {
			ok=0;
			break;
		}
		if(ok) return 1;
	}
	for(int j=0;j<N;j++) {
		int ok=1;
		for(int i=0;i<N;i++) if(a[i][j]!=c&&a[i][j]!='T') {
			ok=0;
			break;
		}
		if(ok) return 1;
	}
	int o=1;
	for(int i=0;i<N;i++) {
		if(a[i][i]!=c&&a[i][i]!='T') o=0;
	}
	if(o) return 1;
	o=1;
	for(int i=0;i<N;i++) {
		if(a[i][3-i]!=c&&a[i][3-i]!='T') o=0;
	}
	if(o) return 1;
	return 0;
}

int nop() {
	for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(a[i][j]=='.') {
		return 1;
	}
	return 0;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.ou","w",stdout);
	int T; scanf("%d",&T);
	for(int ka=1;ka<=T;ka++) {
		for(int i=0;i<N;i++) scanf("%s",a[i]);
		printf("Case #%d: ",ka);
		if(f('X')) puts("X won");
		else if(f('O')) puts("O won");
		else if(nop()) puts("Game has not completed");
		else puts("Draw");
	}

	return 0;
}
