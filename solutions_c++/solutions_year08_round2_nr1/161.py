#include<stdio.h>

typedef unsigned __int64 LL;

#define C3(x)	((x)*(x-1)/2 * (x-2)/3)
#define C2(x)	((x)*(x-1)/2)

LL cnt[4][4];

int main(){

	int N,T,i;
	LL n,a,b,c,d,x,y,m;
	LL tot;

	scanf("%d",&T);

	for(N=1;N<=T;N++){

		for(a=0;a<3;a++)
			for(b=0;b<3;b++)
				cnt[a][b] = 0;

		scanf("%I64u%I64u%I64u%I64u%I64u%I64u%I64u%I64u",&n,&a,&b,&c,&d,&x,&y,&m);

		for(i=0;i<n;i++){
			cnt[x%3][y%3]++;
			x = (a*x + b)%m;
			y = (c*y + d)%m;
		}

		tot = C3(cnt[0][0]) + C3(cnt[0][1]) + C3(cnt[0][2])
			+ C3(cnt[1][0]) + C3(cnt[1][1]) + C3(cnt[1][2])
			+ C3(cnt[2][0]) + C3(cnt[2][1]) + C3(cnt[2][2]);

		tot+= cnt[0][0]*cnt[0][1]*cnt[0][2];
		tot+= cnt[1][0]*cnt[1][1]*cnt[1][2];
		tot+= cnt[2][0]*cnt[2][1]*cnt[2][2];

		tot+= cnt[0][0]*cnt[1][0]*cnt[2][0];
		tot+= cnt[0][1]*cnt[1][1]*cnt[2][1];
		tot+= cnt[0][2]*cnt[1][2]*cnt[2][2];

		tot+= cnt[0][0]*cnt[1][1]*cnt[2][2];
		tot+= cnt[0][0]*cnt[1][2]*cnt[2][1];
		tot+= cnt[0][1]*cnt[1][0]*cnt[2][2];
		tot+= cnt[0][1]*cnt[1][2]*cnt[2][0];
		tot+= cnt[0][2]*cnt[1][0]*cnt[2][1];
		tot+= cnt[0][2]*cnt[1][1]*cnt[2][0];

		printf("Case #%d: %I64u\n",N,tot);
	}

	return 0;
}