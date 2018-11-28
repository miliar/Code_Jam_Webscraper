#include<stdio.h>
#include<conio.h>
int testcase,n;
int o[100],b[100];
char ch,ord[100];
FILE *in,*out;
int i,ro,rb,j,time,or,ob;

int main()
{
	in=fopen("input.txt","r");
	out=fopen("output.txt","w");
	fscanf(in,"%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		ro=0;
		j=0;
		rb=0;
		time=0;
		or=1;
		ob=1;
		fprintf(out,"Case #%d: ",caseId);
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++)
		{
			fscanf(in," %c ",&ch);
			if(ch=='O')
			{
				fscanf(in,"%d",&o[ro++]);
			}
			if(ch=='B')
				fscanf(in,"%d",&b[rb++]);
			ord[i]=ch;
		}
		i=0;
		ro=0;rb=0;
		int flag=0;
		while(i<n)
		{
			time++;
			if(o[ro]==or&&ord[i]=='O')
				flag=1;

			if(b[rb]==ob&&ord[i]=='B')
				flag=2;
			if(o[ro]<or)
				or--;
			if(o[ro]>or)
				or++;
			if(b[rb]<ob)
				ob--;
			if(b[rb]>ob)
				ob++;
			if(flag==1)
			{
				i++;
				flag=0;
				ro++;
			}
			if(flag==2)
			{
				i++;
				flag=0;
				rb++;
			}
		}
		fprintf(out,"%d\n",time);
	}
	return 0;
}