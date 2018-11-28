#include<cstdio>
#include<cstring>

typedef long long i64;

int H,W;
i64 SM [501][501];
i64 SMX[501][501];
i64 SMY[501][501];

i64 GetRange(const i64 A[501][501],int T,int L,int B,int R) {
	return -A[B][L-1]+A[B][R]+A[T-1][L-1]-A[T-1][R];
}

i64 Get(const i64 A[501][501],int X,int Y) {
	return GetRange(A,X,Y,X,Y);
}

int solve() {
	int ret=2;
	int i,j,k,T,L,B,R;
	for(i=1;i<=H;i++) {
		for(j=1;j<=W;j++) {
			for(k=ret+1;i+k-1<=H&&j+k-1<=W;k++) {
				T=i;
				L=j;
				B=i+k-1;
				R=j+k-1;
				i64 M=GetRange(SM ,T,L,B,R);
				M-=Get(SM ,T,L)+Get(SM ,T,R)+Get(SM ,B,L)+Get(SM ,B,R);
				i64 X=GetRange(SMX,T,L,B,R);
				X-=Get(SMX,T,L)+Get(SMX,T,R)+Get(SMX,B,L)+Get(SMX,B,R);
				i64 Y=GetRange(SMY,T,L,B,R);
				Y-=Get(SMY,T,L)+Get(SMY,T,R)+Get(SMY,B,L)+Get(SMY,B,R);
				if(X*2!=M*(T+B))continue;
				if(Y*2!=M*(L+R))continue;
				ret=k;
			}
		}
	}
	return ret>=3?ret:0;
}

void input() {
	int i,j,k,B; char c;
	memset(SM,0,sizeof(SM));
	memset(SMX,0,sizeof(SMX));
	memset(SMY,0,sizeof(SMY));
	scanf("%d%d%d",&H,&W,&B);
	for(i=1;i<=H;i++) {
		for(j=1;j<=W;j++) {
			scanf(" %c",&c);
			k=B+c-'0';
			SM [i][j]=     k  +SM [i][j-1]-SM [i-1][j-1]+SM [i-1][j];
			SMX[i][j]=(i64)k*i+SMX[i][j-1]-SMX[i-1][j-1]+SMX[i-1][j];
			SMY[i][j]=(i64)k*j+SMY[i][j-1]-SMY[i-1][j-1]+SMY[i-1][j];
		}
	}
}

int main() {
	int T,S,ret;
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		input();
		printf("Case #%d: ",S);
		ret=solve();
		if(ret)printf("%d\n",ret);
		else puts("IMPOSSIBLE");
	}
	return 0;
}
