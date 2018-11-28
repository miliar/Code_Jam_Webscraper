#include <cstdio>
#include <cstring>
#include <cmath>
void Solve(int);
const int MAXN=40;
typedef long long int_tt;
int_tt ZwrocL(int_tt,char*);
int main()
{
	int n;
	scanf("%d ",&n);
	for(int i=0;i<n;i++)
		Solve(i+1);
}
void Solve(int x)
{
	char t[MAXN+1];
	scanf("%s",t);
//	printf("%s",t);
	int_tt kp=0,r=0;
	int dl=strlen(t);
	for(int i=0;i<(int)pow(3.0,double(dl-1));i++)
	{
		int_tt z;
		z=ZwrocL(i,t);
		if(z==0) r++;
		else if(z%2==0) r++;
		else if(z%3==0) r++;
		else if(z%5==0) r++;
		else if(z%7==0) r++;
	}
	printf("Case #%d: %lld\n",x,r);
}
int_tt ZwrocL(int_tt q,char *t)
{
	int dl=strlen(t),z=1;
	int_tt r=0,e=t[0]-'0';
//	printf("\n");
	for(int i=1;i<dl;i++)
	{
		if(q%3==0)
		{
			e*=10;
			e+=t[i]-'0';
		}
		if(q%3==1)
		{
			if(z==1)
			{
				r+=e;
//				printf("+%lld ",e);
			}
			else 
			{
				r-=e;
//				printf("-%lld ",e);
			}
			e=t[i]-'0';
			z=1;
		}
		if(q%3==2)
		{
			if(z==1)
			{ 
				r+=e;
//				printf("+%lld ",e);
			}
			else 
			{
				r-=e;
//				printf("-%lld ",e);
			}
			e=t[i]-'0';
			z=2;
		}
		q/=3;
	}
			if(z==1)
			{ 
				r+=e;
//				printf("+%lld ",e);
			}
			else 
			{
				r-=e;
//				printf("-%lld ",e);
			}
	
	return r;
}
