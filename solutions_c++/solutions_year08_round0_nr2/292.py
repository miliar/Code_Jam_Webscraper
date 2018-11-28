#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int Num(int * N,int num)
{
	int train = 0;
	//sort
	int p = 0;
	for (int i = 0,j = 0;i<num-1;i++)
	{
		for (j = i+1;j<num;j++)
		{
			if ((N[i]%10000)>(N[j]%10000))
			{
				p = N[j];
				N[j] = N[i];
				N[i] = p;				
			}
			else				
			{
				if ((N[i]%10000) == (N[j]%10000) && N[i]<10000 && N[j] >= 10000)
				{
					p = N[j];
					N[j] = N[i];
					N[i] = p;				
				}
			}
				
		}
	}


	p = 0;
	for (i = 0;i<num;i++)
	{
		if (N[i]<10000)
		{
			if (p<=0)
			{
				p =0;

				
				if (N[i]%10000<2400)
				{
					train++;
					printf("Leave time:%d\n",N[i]);
					
				}
				
			}
			else
				p--;
		}
		else
			p++;
	}
	return train;
}

void main()
{
	FILE * fileIn = NULL,* fileOut = NULL;
	if (NULL == (fileIn = fopen("d:\\small.in","r")))
	{
		return;
	}
	if (NULL == (fileOut = fopen("d:\\small.out","w")))
	{
		return;
	}
	
	int na = 0,nb = 0;
	int T = 0;
	int Na[200],Nb[200];
	char line[60];
	int nCase = 0;
	int nTa = 0,nTb = 0;


	fgets(line,60,fileIn);
	sscanf(line,"%d",&nCase);
	for (int i = 0;i<nCase;i++)
	{
		fgets(line,60,fileIn);
		sscanf(line,"%d",&T);
		fgets(line,60,fileIn);
		sscanf(line,"%d %d",&na,&nb);
		int ta1 = 0,ta2 = 0;
		int tb1 = 0,tb2 = 0;
		int j = 0;
		for (j = 0;j<na+nb;j++)
		{
			if (j<na)
			{
				fgets(line,60,fileIn);
				sscanf(line,"%d:%d %d:%d",&ta1,&ta2,&tb1,&tb2);
				Na[j] = ta1*100 + ta2;				
				if (tb2 + T >= 60)
				{
					Nb[j] = 10000 + (tb1+1)*100 + (tb2+T)%60;
				}
				else
					Nb[j] = 10000 + tb1*100 + tb2+T;				
			}
			else
			{
				fgets(line,60,fileIn);
				sscanf(line,"%d:%d %d:%d",&ta1,&ta2,&tb1,&tb2);
				Nb[j] = ta1*100 + ta2;				
				if (tb2 + T >= 60)
				{
					Na[j] = 10000 + (tb1+1)*100 + (tb2+T)%60;
				}
				else
					Na[j] = 10000 + tb1*100 + tb2+T;
			}
		}
		printf("Na:\n");
		nTa = Num(Na,na+nb);
		printf("Nb:\n");
		nTb = Num(Nb,na+nb);
		printf("Case #%d: %d %d\n",i+1,nTa,nTb);
		fprintf(fileOut,"Case #%d: %d %d\n",i+1,nTa,nTb);
		
	}




	fclose(fileIn);
	fclose(fileOut);

}