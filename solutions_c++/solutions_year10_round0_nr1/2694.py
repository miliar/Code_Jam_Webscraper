#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char **argv)
{

	int N, cases, n;
	long x, K;
	
    //freopen("A-small-attempt0.in","rt",stdin);
	//freopen("A-small-attempt0.out","wt",stdout);

	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	scanf("%d",&cases);

	for(n=1; n<=cases; n++)
	{
		scanf("%d %ld",&N,&K);

		//while(K-pow(double(2),N)>0)
		//	K=K-pow(double(2),N);

		x =long(pow(double(2),N));
		K=K%x;

		if(K==x-1)
			printf("Case #%d: ON\n",n);
		else 
			printf("Case #%d: OFF\n",n);
	}
	return 0;
}
