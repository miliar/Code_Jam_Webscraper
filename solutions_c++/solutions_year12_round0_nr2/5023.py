#include<stdio.h>



int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("sample.out", "w", stdout);
	int T,N,p,S,tp;
	int a,b;
	int sum;
	scanf("%d",&T);

	for(int i=0;i<T;i++){
		scanf("%d%d%d",&N,&S,&p);
		sum = 0;
		for(int j=0;j<N;j++){
			scanf("%d",&tp);
			a=tp/3;
			b=tp%3;
			
			if(a>=p){
				sum++;
			}
			if(a==p-1){
				if(b!=0)
					sum++;
				else
					if(a!=0&&S>0){
						S--;
						sum++;
					}
			}
			if(a==p-2&&b==2&&S>0){
				S--;
				sum++;
			}
		}

		printf("Case #%d: %d\n",i+1,sum);
	}
//	scanf("%d",&T);

	return 0;
}