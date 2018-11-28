#include<stdio.h>




void main()
{
	FILE *f,*g;
	f=fopen("input","r");
	g=fopen("output","w");

	int n;
	int Nr;
	int x;
	int min;
	int sum;
	int allXor=0;
	fscanf(f,"%d",&n);
	for(int j=0;j<n;j++)
	{
		min=1000000;
		sum=0;
		allXor=0;
		fscanf(f,"%d",&Nr);
		for(int i=0;i<Nr;i++)
		{
			
			fscanf(f,"%d ",&x);
			if(x<min)
				min=x;
			allXor^=x;
			sum+=x;
		}

		if(allXor)
			fprintf(g,"Case #%d: NO\n",(j+1));
		else
			fprintf(g,"Case #%d: %d\n",(j+1),sum-min);


	}


	fcloseall();
}
