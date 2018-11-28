#include <stdio.h>
#include <algorithm>

int data[10000];

int main()
{
	FILE* fp=fopen("c:\\c-large.in","r");;
	FILE* fp2=fopen("c:\\c-large.txt","w");

	int T;
	fscanf(fp,"%d",&T);
	for (int t=1; t<=T; t++)
	{
		int n,chk=0,sum=0;
		fscanf(fp,"%d",&n);
		for (int i=0; i<n; i++)
		{
			fscanf(fp,"%d",data+i);
		}
		std::sort(&data[0],&data[n]);
		for (int i=0; i<n; i++)
		{
			chk ^= data[i];
			sum += data[i];
		}

		if (chk)
		{
			fprintf(fp2,"Case #%d: NO\n", t);
		}
		else
		{
			fprintf(fp2,"Case #%d: %d\n", t, sum - data[0]);
		}
	}
	return 0;
}