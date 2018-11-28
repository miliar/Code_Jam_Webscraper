#include<iostream>

using namespace std;

double P[1024];

int main()
{
	int i,j,T,N,tag,cnt;
	double R,k,tmp,euros;
	scanf("%d",&T);
	for(i=0;i<T;i++){
		scanf("%lf%lf%d",&R,&k,&N);
		for(j=0;j<N;j++)
			scanf("%lf",P+j);
		euros=0; tag=0;
		for(j=0;j<R;j++){
			tmp=0;cnt=0;
			while(tmp+P[tag]<=k&&cnt<N){
				tmp+=P[tag];
				tag=(tag+1)%N; cnt++;
			}
			euros+=tmp;
		}
		printf("Case #%d: %.0lf\n",i+1,euros);
	}
	return 0;
}
