#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	int T,N;
	scanf("%d",&T);
	for(int I=1;I<=T;I++){
		scanf("%d",&N);
		char inp[N][N+1];
		double W[N][N],OW[N],OOW[N],w[N];
		for(int i=0;i<N;i++){
			scanf("%s",inp[i]);
			for(int j=0;j<N;j++) W[i][j]=-1.0;
			OW[i]=0.0;
			OOW[i]=0.0;
		}
		for(int i=0;i<N;i++){
			int p=0,q=0;
			for(int j=0;j<N;j++){
				if(inp[i][j]!='.'){
					p+=inp[i][j]-48;
					q++;
				}
			}
			w[i]=(double)p/(double)q;
			for(int j=0;j<N;j++)
				if(inp[i][j]!='.') W[i][j]=(double)(p-inp[i][j]+48)/(double)(q-1);
		}
		
		for(int i=0;i<N;i++){
			int q=0;
			for(int j=0;j<N;j++){
				if(j==i) continue;
				if(W[i][j]>=0){
						OW[i]+=W[j][i];
						q++;
				}
			}
			OW[i]/=(double)q;
		}
		double x=0.0;
		for(int i=0;i<N;i++){
				int q=0;
				for(int j=0;j<N;j++){
					if(i!=j && inp[i][j]!='.'){
						OOW[i]+=OW[j];
						q++;
					}
				}
				OOW[i]/=q;	
		}

		printf("Case #%d:\n",I);
		for(int i=0;i<N;i++) printf("%.8lf\n",0.25*w[i]+0.5*OW[i]+0.25*OOW[i]);
	}
}
