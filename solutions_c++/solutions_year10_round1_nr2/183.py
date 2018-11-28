#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int TT;
int D,I,M,N;
int pixels[128];
int PD[128][256];

int calc(int a1,int a2, int b1, int b2, int v) {
	if(b1<a1)
		swap(a1,b1),swap(a2,b2);
	//intervalo bi, a2
	if(v>=b1 and v<=a2)
		return 0;
	return min(std::abs(b1-v),std::abs(a2-v));

}
int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		scanf("%d %d %d %d",&D,&I,&M,&N);
		for(int i=0;i<N;i++)
			scanf("%d",pixels+i+1);

		memset(PD,0x3f,sizeof(PD));
		for(int i=0;i<256;i++)
			PD[0][i]=0;

		for(int i=1;i<=N;i++) {
			for(int j=0;j<256;j++)
				for(int k=0;k<256;k++)  {
					//remover
					if(j==k)
						PD[i][j]=min(PD[i][j],PD[i-1][k]+D);
					if(std::abs(j-k)<=M) {
						//mudo valor para j
						PD[i][j]=min(PD[i][j],PD[i-1][k]+std::abs(pixels[i]-j));
					}
					if(M!=0)
					//insiro atras e mudo valor
						PD[i][j]=min(PD[i][j],PD[i-1][k]+std::abs(pixels[i]-j)+I*( max(0,(std::abs(j-k)-1))/M) );
					PD[0][0]=0;

					/*
					if(std::abs(j-k)<=2*M) {
						//insiro na frente e mudo valor
						PD[i][j]=min(PD[i][j],PD[i-1][k]+calc(j-M,j+M,k-M,k+M,pixels[i])+I);
					}*/
				}
		}
		int ans=0x3f3f3f3f;
		for(int i=0;i<256;i++)
			ans=min(ans,PD[N][i]);
		printf("Case #%d: %d\n",T,ans);
	}

	return 0;
}
