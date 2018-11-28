#include<stdio.h>
#include<string.h>
#include<math.h>

int main()
{
	int N;
	int steprec[110];
	int times,step;
	int i,j;
	char c,cb='B';
	int Odest,Bdest;
	int Onow,Bnow;
	int Oc,Bc;
	FILE* p;
	FILE* q;
	q=fopen("A-large.in","r");
	fscanf(q,"%d",&N);
	for(i=1;i<=N;i++)
	{
		fscanf(q,"%d",&times);
		Onow=1;
		Bnow=1;
		step=0;
		Oc=0;
		Bc=0;
		c=fgetc(q);
		for(j=1;j<=times;j++)
		{
			c=fgetc(q);
			if(c=='O')
			{
				fscanf(q,"%d",&Odest);
				if(c==cb)
				{
					Oc=Oc+abs(Odest-Onow)+1;
					step=step+abs(Odest-Onow)+1;
				}
				else
				{
					if(Bc>=abs(Odest-Onow)+1)
					{
						Oc=1;
						step++;
					}
					else
					{
						Oc=abs(Odest-Onow)+1-Bc;
						step=step+Oc;
					}
				}
				Onow=Odest;
			}
			else if(c=='B')
			{
				fscanf(q,"%d",&Bdest);
				if(c==cb)
				{
					Bc=Bc+abs(Bdest-Bnow)+1;
					step=step+abs(Bdest-Bnow)+1;
				}
				else
				{
					if(Oc>=abs(Bdest-Bnow)+1)
					{
						Bc=1;
						step++;
					}
					else
					{
						Bc=abs(Bdest-Bnow)+1-Oc;
						step=step+Bc;
					}
				}
				Bnow=Bdest;
			}
			cb=c;
			c=fgetc(q);
		}
		steprec[i]=step;
	}
	p=fopen("output.txt","wt");
	for(i=1;i<=N;i++)
		fprintf(p,"Case #%d: %d\n",i,steprec[i]);
	fclose(p);
	fclose(q);
	return 0;
}