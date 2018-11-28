#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
	int tn[3];
	int pn[3];
	int C,N;
	int Pmax;
	scanf("%d",&C);
	for(int i = 1 ; i <= C ; i++ )
	{
		scanf("%d",&N);
		for(int j = 0; j< N; j++)
		{
			scanf("%d",&tn[j]);
		}
		Pmax = N*(N-1)/2;
		
		int Pmin=0x7fffffff;
		int Pcnt=0;
		for(int j=0;j<N-1; j++)
		{
			for(int k= j+1; k < N; k++)
			{
				int tmp = abs(tn[j]-tn[k]);
				pn[Pcnt] = tmp;
				if(Pmin>tmp && tmp)
				{
					Pmin= tmp;
				}					
				Pcnt++;
			}	
		}
		while(1){
			int min=Pmin;
			int tmp;
			int same=1;
			for(int j=0;j<Pmax; j++){
				if(pn[j] == Pmin && same)
					pn[j] = Pmin;
				else
					pn[j] = pn[j]%Pmin;
				if(pn[j]==Pmin)
					same=0;
				if(min>pn[j] && pn[j])
				{
					min=pn[j];
				}
			}
			Pmin=min;
			int cnt=0;
			for(int j = 0 ;j<Pmax ; j++)
			{
				if(pn[j]!=0)
					cnt++;
			}
			if(cnt==1)
				break;
		}
		int y;
		if(Pmin == 1 || tn[0]%Pmin == 0)
			y=0;
		else
			y = Pmin -(tn[0]%Pmin);
		printf("Case #%d: %d\n",i,y);
	}
	return 1;
}