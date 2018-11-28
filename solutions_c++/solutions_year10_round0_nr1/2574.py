#include "stdio.h"
#include "stdlib.h" 

__int64 mem[31]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824};

int main()
{
	FILE* f;
	f=fopen("A-large.in","r");
	//f=fopen("A-large-practice.in","r");
	if(f==NULL)
	{
		printf("file read error£¡");
		exit(1); 
	}

	FILE *w;
	w=fopen("A-large.out","w");
	//w=fopen("A-large-practice.out","w");
	if (w==NULL)
	{
		printf("file write error£¡");
		exit(1); 
	}
	int count=0;
	int count_p=0;
	int n;
	__int64 k;
	int point=0;
	int sign=0;
	int tt;
	fscanf(f,"%d",&count);

	for (int i=0;i<count;i++)
	{
		//printf("%d\n",i);
		fscanf(f,"%d",&n);
		fscanf(f,"%I64d",&k);
		//printf("%d %d\n",n,k);

		sign=0;
		tt=0;
		if (k%2==1)
		{
			k=k%mem[n];
			
			if (k+1==mem[n])
			{
					sign=1;
			}
		}
		
		fprintf(w,"Case #%d: ",i+1);
		if (sign>0)
		{
			fprintf(w,"ON");
		}
		else fprintf(w,"OFF");
		fprintf(w,"\n");
	}
	fclose(f);
	fclose(w);

}
