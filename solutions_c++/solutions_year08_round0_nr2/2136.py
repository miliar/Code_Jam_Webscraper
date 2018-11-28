#include <stdio.h>
#include <stdlib.h>


int time(FILE *in)
{
	char str[15],*s;
	int h=0,m=0;
	fscanf(in,"%s",&str);
	str[2]=0;
	str[5]=0;
	h=atoi(str);
	m=atoi(str+3);
	return (h*60+m);
}

void remove(int* a, int n, int k)
{

	for(int j=k;j<n-1;j++)
		a[j]=a[j+1];
}

void solve(FILE* in, FILE* out)
{
	int n=0,t=0,na=0,nb=0,aa=0,ab=0;
	char str[15],*s;
	int a[150][3],sol[150][2];
	fscanf(in,"%d",&t);
	fscanf(in,"%d %d",&na,&nb);
	n=na+nb;
	for(int i=0;i<n;i++)
	{
		a[i][0]=time(in);
		a[i][1]=time(in);
		if(i>=na)a[i][2]=1;else a[i][2]=0;
	}
	for(i=0;i<n;i++)
		for(int j=0;j<n-1;j++)
		{
			if((a[j][0]>a[j+1][0])||((a[j][0]==a[j+1][0])&&(a[j][1]>a[j+1][1])))
			{
				int t=0;
				t=a[j][0];a[j][0]=a[j+1][0];a[j+1][0]=t;
				t=a[j][1];a[j][1]=a[j+1][1];a[j+1][1]=t;
				t=a[j][2];a[j][2]=a[j+1][2];a[j+1][2]=t;
			}

		}

	while(n>0)
	{
		for(i=0;i<n;i++)
		{
			sol[i][0]=0;
			sol[i][1]=-1;
		}
		for(i=0;i<n;i++)
		{
			for(int j=i-1;j>=0;j--)
			{
				if(((a[i][2]+a[j][2])==1)&&(a[i][0]>=(a[j][1]+t)))
				{
					if(sol[i][1]==-1)
					{
						sol[i][1]=j;
						sol[i][0]=sol[j][0]+1;
					}
					else if(sol[j][0]>sol[i][0])
					{
						sol[i][1]=j;
						sol[i][0]=sol[j][0]+1;
					}
				}
			}
		}
		int max=0,l=0;
		for(i=1;i<n;i++)
			if(sol[max][0]<sol[i][0])max=i;
		while(max!=-1)
		{
			l=sol[max][1];
			if(l==-1)
			{
				if(a[max][2]==0)aa++; else ab++;
			}
			for(i=max;i<n-1;i++)
				for(int j=0;j<3;j++)
					a[i][j]=a[i+1][j];
			for(i=max;i<n-1;i++)
				for(int j=0;j<2;j++)
					sol[i][j]=sol[i+1][j];
			n--;
			max=l;
		}
	}
	fprintf(out,"%d %d",aa,ab);
}

int main()
{
	int n=0;
	FILE *in=fopen("a.in","r");
	FILE *out=fopen("a.out","w+");
	fscanf(in,"%d",&n);
	for(int i=0;i<n;i++)
	{
		fprintf(out,"Case #%d: ",i+1);
		solve(in,out);
		fputs("\n",out);
	}
	fclose(in);
	fclose(out);
	return 0;
}