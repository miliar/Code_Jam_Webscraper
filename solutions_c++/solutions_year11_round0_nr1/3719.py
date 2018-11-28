#include<stdio.h>

int o[3][1005];
int b[3][1005];
int on,bn;

int main()
{
	int t,i,j,p,b1,o1,b2,o2;
	char r,r1,r2;
	int n;
	FILE *fp1=fopen("input.in","r");
	FILE *fp2=fopen("output.out","w");
	fscanf(fp1,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(fp1,"%d",&n);
		on=bn=0;
		for(j=1;j<=n;j++)
		{
			fscanf(fp1,"%c%c%c%d",&r1,&r,&r2,&p);
			if(r=='O')
			{
				o[1][++on]=j;
				o[2][on]=p;
			}
			if(r=='B')
			{
				b[1][++bn]=j;
				b[2][bn]=p;
			}
		}
		b1=o1=b2=o2=1;
		o[1][on+1]=n+1;
		o[2][on+1]=200;
		b[1][bn+1]=n+1;
		b[2][bn+1]=200;
		for(j=1;j<j+1;j++)
		{
			if(b[1][b2]>o[1][o2])
			{
				if(b[2][b2]>b1)
					b1++;
				else if(b[2][b2]<b1)
					b1--;
				if(o[2][o2]>o1)
					o1++;
				else if(o[2][o2]<o1)
					o1--;
				else
					o2++;
			}
			else
			{
				if(o[2][o2]>o1)
					o1++;
				else if(o[2][o2]<o1)
					o1--;
				if(b[2][b2]>b1)
					b1++;
				else if(b[2][b2]<b1)
					b1--;
				else
					b2++;
			}
			if(o2>on && b2>bn)
				break;
		}
		fprintf(fp2,"Case #%d: %d\n",i,j);
	}
	return 0;
}