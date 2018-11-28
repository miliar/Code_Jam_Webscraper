#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;

int C,N;
int big[1010][55];
int tmp[55];
int g[55],mul[55],Minus[55];

bool eqzero(int a[55])
{
	int i;
	for(i=0;i<55;i++)
	{
		if(a[i]) return false;
	}
	return true;
}

bool greater1(int a[55],int b[55])
{
	int i;
	for(i=54;i>=0;i--)
	{
		if(a[i]>b[i]) return true;
		if(a[i]<b[i]) return false;
	}
	return false;
}

void minus1(int a[55],int b[55])
{
	int i;
	for(i=0;i<55;i++)
	{
		Minus[i]=a[i]-b[i];
	}
	for(i=0;i<54;i++)
	{
		if(Minus[i]<0)
		{
			Minus[i+1]--;
			Minus[i]+=10;
		}
	}
}

void mult(int a[55],int b)
{
	int i;
	for(i=0;i<55;i++)
	{
		mul[i]=a[i]*b;
	}
	for(i=0;i<54;i++)
	{
		mul[i+1]+=mul[i]/10;
		mul[i]%=10;
	}
}

void gcd(int a[55],int b[55])
{
	int i,j;
	while(1)
	{
		if(eqzero(b))
		{
			for(i=0;i<55;i++) g[i]=a[i];
			break;
		}
		if(eqzero(a))
		{
			for(i=0;i<55;i++) g[i]=b[i];
			break;
		}
		for(i=1;;i++)
		{
			mult(a,i);
			if(greater1(mul,b))
			{
				mult(a,i-1);
				minus1(b,mul);
				break;
			}
		}
		for(i=0;i<55;i++) b[i]=a[i];
		for(i=0;i<55;i++) a[i]=Minus[i];
	}
}

int main()
{
	int i,j,Case=1;
	int Min[55];
	freopen("B-small-attempt0.in","r",stdin);
	freopen("aaa.txt","w",stdout);
	scanf("%d",&C);
	for(;C>0;C--)
	{
		fill(Min,Min+55,0);
		scanf("%d",&N);
		getchar();
		for(i=0;i<N;i++)
		{
			char c;
			fill(big[i],big[i]+55,0);
			j=0;
			while(1)
			{
				c=getchar();
				if(c==' ' || c=='\n') break;
				big[i][j++]=c-48;
			}
			reverse(big[i],big[i]+j);
			if(!i) memcpy(Min,big[0],55);
			else
			{
				if(greater1(Min,big[i]))
				{
					memcpy(Min,big[i],55);
				}
			}
		}
		for(i=0;i<N;i++)
		{
			if(!eqzero(big[i]))
				memcpy(tmp,big[i],55);
			minus1(big[i],Min);
			memcpy(big[i],Minus,55);
		}
		gcd(big[0],big[1]);
		for(i=2;i<N;i++)
		{
			gcd(g,big[i]);
		}
		int ans[55];
		for(i=1;;i++)
		{
			mult(g,i);
			if(greater1(mul,tmp))
			{
				mult(g,i-1);
				minus1(tmp,mul);
				if(eqzero(Minus)) memset(ans,0,sizeof(ans));
				else
				{
					minus1(g,Minus);
					for(i=0;i<55;i++) ans[i]=Minus[i];
				}
				break;
			}
		}
		if(eqzero(ans)) printf("Case #%d: 0\n",Case++);
		else
		{
			printf("Case #%d: ",Case++);
			i=54;
			while(!ans[i]) i--;
			for(;i>=0;i--) printf("%d",ans[i]);
			printf("\n");
		}
	}
	return 0;
}
		
		
