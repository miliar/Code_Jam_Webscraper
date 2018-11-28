#include <stdio.h>

int t,tcase;
int n,m,swi,ele;

int main()
{
	int i,j,tmp;

	FILE *out,*in;
	in=fopen("A-small-attempt0.in","r");
	out=fopen("A-small-attempt0.out","w");

	fscanf(in,"%d",&tcase);
	for(t=0;t<tcase;t++)
	{
		fscanf(in,"%d",&n);
		fscanf(in,"%d",&m);

		swi=0;
		for(j=0;j<m;j++)
		{
			ele=1;
			for(i=0;i<n;i++)
			{
				tmp=swi&ele;
				if(tmp==0)
				{
					swi^=ele;
					break;
				}
				swi^=ele;
				ele<<=1;
			}
		}

		ele=1;
		for(i=0;i<n;i++)
			ele<<=1;
		ele-=1;
		fprintf(out,"Case #%d: ",t+1);
		if(ele==swi)
			fprintf(out,"ON\n");
		else
			fprintf(out,"OFF\n");
	}

	return 0;
}