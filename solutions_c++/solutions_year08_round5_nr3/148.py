#include<stdio.h>

#define MAX 12

int R,C;
char mat[MAX][MAX];

int mm[MAX];

int n;
int nb;
int bmp[1<<11],cnt[1<<11];

int dp[MAX][1<<11];

int bits[1<<11];

int bcount(int k){
	int c=0;
	while(k){
		c+=k%2;
		k/=2;
	}
	return c;
}

int ok(int x){
	int i,p[15];

	for(i=0;i<C;i++){
		p[i]=x%2;
		x/=2;
	}

	for(i=1;i<C;i++)
		if(p[i] && p[i-1])
			return 0;

	return 1;
}

int isect(int top,int bot){
	int i;

	for(i=0;i<C;i++){
		if(bot & (1<<i)){
			if(i>0 && (top & (1<<(i-1))) )
				return 1;
			if(i<C-1 && (top & (1<<(i+1))) )
				return 1;
		}
	}

	return 0;
}

int main(){

	int T,N;
	int r,c,i,j,k , a,b;

	for(k=0;k<(1<<10);k++)
		bits[k] = bcount(k);

	scanf("%d",&T);

	for(N=1;N<=T;N++){
		
		scanf("%d%d",&R,&C);

		for(r=0;r<R;r++){
			scanf("%s",mat[r]);
			mm[r] = 0;
			for(c=0;c<C;c++)
				if(mat[r][c]=='.')
					mm[r] |= (1<<c);
		}


		n = (1<<C);
		nb = 0;
		for(k=0;k<n;k++){
			if(ok(k)){
				bmp[nb] = k;
				cnt[nb] = bcount(k);
				nb++;
			}
		}

//		printf(">>> %d\n",nb);

		for(r=0;r<R;r++)
			for(i=0;i<nb;i++)
				dp[r][bmp[i]] = 0;

		//r=0;
		r = 0;
		for(i=0;i<nb;i++)
			dp[0][ mm[r] & bmp[i] ] = bits[ mm[r] & bmp[i] ];

		for(r=0;r<R-1;r++){
			
			for(i=0;i<nb;i++){

				a = mm[r] & bmp[i];
			
				for(j=0;j<nb;j++){
					
					b = mm[r+1] & bmp[j];

					if( isect(a,b) )
						continue;

					if(dp[r+1][b] < dp[r][a] + bits[b])
						dp[r+1][b] = dp[r][a] + bits[b];
				}
			}
		}

		a = 0;
		for(i=0;i<nb;i++)
			if(dp[R-1][bmp[i]] > a)
				a = dp[R-1][bmp[i]];

		printf("Case #%d: %d\n",N,a);

	}
	return 0;
}