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

int w[1111][1111];
int n;
char s[1111];
double wp[1111], owp[1111], rpi[1111];

int main() {
int nt, tt=0; scanf("%d", &nt); while(nt--){
	scanf("%d", &n);
	CLR(w);
	FOR(i,0,n){
		scanf("%s", s);
		FOR(j,0,n){
			if(s[j] == '0')w[i][j] = -1;
			else if(s[j] == '1')w[i][j] = 1;
		}
	}
	FOR(i,0,n){
		int np = 0;
		wp[i] = 0.0;
		owp[i] = 0.0;
		FOR(j,0,n)if(w[i][j]){
			np++;
			if(w[i][j]==1)wp[i]+=1.0;
			int snp = 0;
			double swp = 0.0;
			FOR(k,0,n)if(k!=i && w[j][k]){
				snp++;
				if(w[j][k]==1)swp+=1.0;
			}
			owp[i] += swp/snp;
		}
		wp[i] /= np;
		owp[i] /= np;
		//printf(" %d : %.5f %.5f\n", i, wp[i], owp[i]);
	}
	FOR(i,0,n){
		int np = 0;
		double oowp = 0.0;
		FOR(j,0,n)if(w[i][j]){
			np++;
			oowp += owp[j];
		}
		oowp/=np;
		rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp;
	}
	printf("Case #%d:\n", ++tt);
	FOR(i,0,n)printf("%.12f\n", rpi[i]);
}
	return 0;
}


