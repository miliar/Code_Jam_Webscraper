#include <iostream.h>
#include <conio.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
unsigned long int R,k,N,a,tp;
unsigned long int queue[1001],earn;
int fr,pfr;
int main()
{
	FILE *in,*out;
	int ncases,c,i,j,k,l;
	in=fopen("CS.in","r+");
	out=fopen("COS.out","w+");
	fscanf(in,"%d",&ncases);
	for(c=0;c<ncases;c++)
	{
		fscanf(in,"%ld %ld %ld\n",&R,&k,&N);
		for(i=0;i<N;i++)
			fscanf(in,"%ld",&queue[i]);

		cout<<endl;
		fr=0;
		earn=0;
		for(a=0;a<R;a++)
		{
			tp=queue[fr];
			pfr=fr;
			while((tp+queue[(fr+1)%N])<=k&&((fr+1)%N!=pfr))
			{
					fr++;
					fr=fr%N;
					tp+=queue[fr];
			}
			fr++;
			fr=fr%N;
			earn+=tp;
		}
		fprintf(out,"Case #%d: %ld\n",c+1,earn);
	}
	fclose(in);
	fclose(out);
	clrscr();
	return 0;
}