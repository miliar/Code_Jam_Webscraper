#include<stdio.h>
int main()
{
    FILE *fpin,*fpout;
    fpin=fopen("input.in","r");
    fpout=fopen("output.out","w");
    int t,n,ans,pd,pg;
    fscanf(fpin,"%d",&t);
    for(int i=0;i<t;i++)
    {
	ans=0;
	fscanf(fpin,"%d",&n);
	fscanf(fpin,"%d",&pd);
	fscanf(fpin,"%d",&pg);
	for(int j=1;j<=n;j++)
	{
	    ans=j*pd/100;
	    if(ans*100==j*pd)
	       break;
	}
	if(pd!=0&&pg==0)
		j=n+1;
	if(pg==100)
	   if(pd!=100)
		j=n+1;
	if(j<=n)
	   fprintf(fpout,"Case #%d: Possible\n",i+1);
	else
	   fprintf(fpout,"Case #%d: Broken\n",i+1,ans);
    }
    return 0;
}