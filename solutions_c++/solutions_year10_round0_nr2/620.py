#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int c,n,a[1010][60],t[60],g[60],w[60];
char s[60];

void minus(int x,int y)
{
	int p,q;
	if (a[x][0]>a[y][0])
	{p=x;q=y;}
	else if (a[x][0]<a[y][0])
	{p=y;q=x;}
	else
	{
		int k=a[x][0];
		while (a[x][k]==a[y][k] && k>0)
			k--;
		if (a[x][k]>a[y][k])
			{p=x;q=y;}
		else {p=y;q=x;}
	}
	memset(t,0,sizeof(t));
	for (int i=a[p][0];i>=0;i--)
		t[i]=a[p][i];
	for (int i=1;i<=t[0];i++)
	{
		t[i]-=a[q][i];
		if (t[i]<0)
		{
			t[i]+=10;
			t[i+1]--;
		}
	}
	while (t[t[0]]==0) t[0]--;
}

bool wBiggerg()
{
	if (w[0]>g[0])
		return true;
	else if (w[0]<g[0])
		return false;
	else
	{
		int k=w[0];
		while (w[k]==g[k] && k>0)
			k--;
		if (w[k]>=g[k])
			return true;
		else return false;
	}
}

bool wUpSmallerg()
{
		int k=w[0],x=g[0];
		while (w[k]==g[x] && k>0)
		{
			k--;
			x--;
		}
		if (w[k]<g[x])
			return true;
		else return false;

}

void wModg()
{
	while (wBiggerg())
	{
		if (wUpSmallerg())
		{
			w[0]--;
			w[w[0]]+=w[w[0]+1]*10;
			w[w[0]+1]=0;
		}
		for (int i=w[0]-g[0]+1,j=1;j<=g[0];i++,j++)
		{
			w[i]-=g[j];
			if (w[i]<0)
			{
				w[i+1]--;
				w[i]+=10;
			}
		}
		while (w[w[0]]==0 && w[0]>0) w[0]--;
	}
}

void gcd() //t%g=w
{
	memset(w,0,sizeof(w));
	for (int i=0;i<=t[0];i++)
		w[i]=t[i];
	while (w[0]>0)
	{
		//t=g
		memset(t,0,sizeof(t));
		for (int i=0;i<=g[0];i++)
			t[i]=g[i];
		//g=w
		memset(g,0,sizeof(g));
		for (int i=0;i<=w[0];i++)
			g[i]=w[i];
		//w=t%g
		memset(w,0,sizeof(w));
		for (int i=0;i<=t[0];i++)
			w[i]=t[i];
		wModg();
	}
}

int main()
{
	FILE *input=fopen("b.in","r"); 
	FILE *output=fopen("b.out","w"); 
	fscanf(input,"%d",&c);
	for (int cc=1;cc<=c;cc++)
	{
		memset(a,0,sizeof(a));
		memset(t,0,sizeof(t));
		fscanf(input,"%d",&n);
		for (int i=1;i<=n;i++)
		{
			fscanf(input,"%s",s);
			a[i][0]=strlen(s);
			for (int j=1;j<=a[i][0];j++)
				a[i][j]=s[a[i][0]-j]-'0';
		}
		minus(1,2);
		memset(g,0,sizeof(g));
		g[0]=t[0];
		for (int i=1;i<=g[0];i++)
			g[i]=t[i];
		for (int i=1;i<=n;i++)
			for (int j=i+1;j<=n;j++)
			{
				minus(i,j);
				gcd();
			}
		memset(w,0,sizeof(w));
		for (int i=0;i<=a[1][0];i++)
			w[i]=a[1][i];
		//ans= g-(w%g)
		wModg();
		if (w[0]==0)
		{
			g[0]=1;
			g[1]=0;
		}
		else for (int i=1;i<=g[0];i++)
		{
			g[i]-=w[i];
			if (g[i]<0)
			{
				g[i]+=10;
				g[i+1]--;
			}
		}
		while (g[g[0]]==0 && g[0]>1) g[0]--;
		fprintf(output,"Case #%d: ",cc);
		for (int i=g[0];i>=1;i--)
			fprintf(output,"%d",g[i]);
		fprintf(output,"\n");
	}
	fclose(input);
	fclose(output);
	return 0;
}