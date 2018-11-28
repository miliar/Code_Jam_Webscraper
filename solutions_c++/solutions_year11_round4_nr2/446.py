#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cctype>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

int n, m, d;
int w[1111][1111];
char s[11111];
LL q[1111][1111], qi[1111][1111], qj[1111][1111], wi[1111][1111], wj[1111][1111];

int main() {
int nt, tt=0; scanf("%d", &nt); while(nt--){
	scanf("%d%d%d", &n, &m, &d);
	FOR(i,0,n){
		scanf("%s", s);
		FOR(j,0,m){
			w[i][j] = s[j]-'0';
			wi[i][j] = w[i][j]*i;
			wj[i][j] = w[i][j]*j;
		}
	}

	CLR(q); CLR(qi); CLR(qj);
	FOR(i,0,n)FOR(j,0,m){
		q[i+1][j+1] = q[i][j+1]+q[i+1][j]-q[i][j]+w[i][j];
		qi[i+1][j+1] = qi[i][j+1]+qi[i+1][j]-qi[i][j]+wi[i][j];
		qj[i+1][j+1] = qj[i][j+1]+qj[i+1][j]-qj[i][j]+wj[i][j];
	}

	int ans = -1;
	int lk = min(n,m);
	for(int k = lk; k>=3; k--){
		FOE(i,0,n-k){FOE(j,0,m-k){
#define RECT(x) (x[i+k][j+k]-x[i][j+k]-x[i+k][j]+x[i][j])
#define CORN(x) (x[i][j]+x[i][j+k-1]+x[i+k-1][j]+x[i+k-1][j+k-1])
			LL si = RECT(qi)-CORN(wi);
			LL su = RECT(q) - CORN(w);
			//if(i==1 && j==1 && k==5)printf("  %I64d %.5f\n", si, si*1.0/su);
			if(si*2LL != 2LL*i*su + (k-1LL)*su)continue;
			LL sj = RECT(qj)-CORN(wj);
			if(sj*2LL != 2LL*j*su + (k-1LL)*su)continue;
			//if(i==1 && j==1 && k==5)printf("  %I64d %.5f\n", si, si*1.0/su);
			ans = k;
			break;
		} if(ans>=0)break;}
		if(ans>=0)break;
	}
	
	printf("Case #%d: ", ++tt);
	if(ans >= 0){
		printf("%d\n", ans);
	}else{
		printf("IMPOSSIBLE\n");
	}
}
	return 0;
}


