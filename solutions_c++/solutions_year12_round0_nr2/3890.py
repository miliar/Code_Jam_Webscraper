#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	int T,N,S,p,X;
	int i;
	int teste=1;
	int resposta;
	int duvida;
	
	scanf("%d",&T);
	
	while(teste <= T)
	{
		scanf("%d %d %d",&N, &S, &p);
		
		resposta=0;
		duvida=0;
		
		for(i=1; i<=N; i++)
		{
			scanf("%d",&X);
			if(X%3 == 0)
			{
				if(X/3 >= p) resposta++;
				else if(X>0){
					if(1 + X/3 >= p) duvida++;
				}
			}
			else if(X%3 == 1)
			{
				if((int)(X/3)+1 >= p)
				{
					resposta++;
				}
			}
			else
			{
				if((int)(X/3)+1 >= p) resposta++;
				else{
					if((int)(X/3)+2 >= p) duvida++;
				}
			}
			
		}
		printf("Case #%d: ",teste++);
		if(duvida <= S){
			printf("%d\n",resposta+duvida);
		}
		else{
			printf("%d\n",resposta+S);
		}
	}
	
}