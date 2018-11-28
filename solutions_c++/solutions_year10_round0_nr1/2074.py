// 2010Q1s.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"




int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp1,*fp2;
	fp1=fopen("A-large.in","r");
	fp2=fopen("A-large.out","w");
	long int N,K;
	long int K_count=0;
	int i=0,T=0,T_count=0;
	int	ruizyo[10001];
	int w_count=0;
	fscanf(fp1,"%d",&T);
	while(T_count<T){
		T_count++;
		K_count=0;
		w_count=0;
		for(i=0;i<=10000;i++){
			ruizyo[i]=0;
		}
		fscanf(fp1,"%ld %ld",&N,&K);	//if(K==10000000){指が折れる}

		for(i=0;K != 0 ;i++){
			ruizyo[i]= K%2 ;
			K=K/2;
			//printf("2の%d乗は%d	Ｋ＝%d\n",i,ruizyo[i],K);
		}
		for(i=0;i<=N-1;i++){
			if(ruizyo[i]!=1){
				break;
			}
			if(i==N-1){
				fprintf(fp2,"Case #%d: ON\n",T_count);
				w_count=1;
				break;
			}
		}
		if(w_count==0){
			fprintf(fp2,"Case #%d: OFF\n",T_count);
		}
	}
	//getchar();
	return 0;
}
