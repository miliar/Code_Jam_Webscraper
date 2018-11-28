#include<stdio.h>
#include<string.h>

int s[300],p,n;

int che[300],ches[300],sol[300][300];

int checks(int a)
{
	if(ches[a]!=-1) return ches[a];
	int i,j,k;
	for(i=0; i<=10; i++)
		for(j=i-2; j<=i+2 ;j++)
		{
			if(j<0) continue;
			if(i+j>a) break;
			k = a-i-j;
			if(k-i>2 || i-k>2 || j-k>2 || k-j>2) continue;
			if(i-k==2 || k-i==2 || j-k==2 || k-j==2)
				if(i>=p || j>=p || k>=p)
					return ches[a]=1;
		}
	return ches[a]=0;
}


int check(int a)
{
	if(che[a]!=-1) return che[a];
	int i,j,k;
	for(i=0; i<=10; i++)
		for(j=i-1; j<=i+1 ;j++)
		{
			if(j<0) continue;
			if(i+j>a) break;
			k = a-i-j;
			if(k-i>1 || i-k>1 || j-k>1 || k-j>1) continue;
			if(i>=p || j>=p || k>=p)
				return che[a]=1;
		}
	return che[a]=0;
}

int solve(int i, int ss)
{
	if(i==n)
		return 0;
	if(sol[i][ss]!=-1) return sol[i][ss];
	int a=0,b;
	if(ss)
		a = checks(s[i]) + solve(i+1,ss-1);
	b = check(s[i]) + solve(i+1,ss);
	if(a>b)
		return sol[i][ss]=a;
	return sol[i][ss]=b;
}

int main()
{
	int qq,q,ss;
	FILE *in=fopen("s.in","r");
	FILE *out=fopen("s.out","w");
	fscanf(in,"%d",&qq);
	for(q=1; q<=qq ;q++)
	{
		memset(che,-1,sizeof che);
		memset(ches,-1,sizeof ches);
		memset(sol,-1,sizeof sol);
		fscanf(in,"%d%d%d",&n,&ss,&p);
		//fprintf(out,"%d %d %d\n",n,ss,p);
		for(int i=0; i<n;i++)
		{
			fscanf(in,"%d",&s[i]);
			//fprintf(out,"%d ",s[i]);
		}
		fprintf(out,"Case #%d: %d\n",q,solve(0,ss));
	}
}
