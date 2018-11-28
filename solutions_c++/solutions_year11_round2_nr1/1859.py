#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string>
#include <algorithm>
using namespace std;

#define clr(s, x) memset(s, x, sizeof(s))

typedef long long LL;
typedef unsigned long long ULL;
#define SZ 110
char s[SZ][SZ];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cs, T, N, i, j, k, p, zi, mu;
	double wp[SZ], owp[SZ], oowp[SZ], num, num2;
	scanf("%d", &T);
	for(cs=1; cs<=T; cs++){
		clr(s, 0);
		clr(wp, 0);
		clr(owp, 0);
		clr(oowp, 0);
		scanf("%d", &N);
		for(i=0; i<N; i++)
			scanf("%s", s[i]);
		for(i=0; i<N; i++){
			zi=0;
			mu=0;
			for(j=0; j<N; j++){
				if(s[i][j]=='1'){zi++; mu++;}
				if(s[i][j]=='0')mu++;
			}
			if(mu)wp[i]=1.0*zi/(1.0*mu);
			else wp[i]=0.0;
		}

		for(k=0; k<N; k++){
			num=0;
			for(i=0; i<N; i++){
				if(s[k][i]=='.' || k==i)continue;
				else num++;
				zi=0;
				mu=0;
				for(j=0; j<N; j++){
					if(s[i][j]=='.' || k==j)continue;
					if(s[i][j]=='1'){zi++; mu++;}
					if(s[i][j]=='0')mu++;
				}
				if(mu)owp[k]+=(1.0*zi)/(1.0*mu);
				else owp[k]=0.0;
			}
			if(num)owp[k]=owp[k]/(1.0*num);
			else owp[k]=0.0;
		}

		for(p=0; p<N; p++){
			num2=0;
			for(k=0; k<N; k++){
				if(s[p][k]!='.'){oowp[p]+=owp[k]; num2++;}
			}
			if(num2)oowp[p]=oowp[p]/(1.0*num2);
			else oowp[p]=0.0;
		}
		
		printf("Case #%d:\n", cs);
		for(i=0; i<N; i++){
			printf("%lf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}

    return 0;
}
