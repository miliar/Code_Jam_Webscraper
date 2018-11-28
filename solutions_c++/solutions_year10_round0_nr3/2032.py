#include <stdio.h>
#include <string.h>
#define NMAX 2005
#define ll long long
int t,r,k,n,A[NMAX],caz,B[NMAX],D[NMAX],poz_st,steps,cicluri,last_visit;
ll sum,C[NMAX],rez,E[NMAX];
char viz[NMAX];
void read()
{
	scanf("%d%d%d",&r,&k,&n);
	int i;
	for (i=1; i<=n; i++)
	{
		scanf("%d",&A[i]);
		A[n+i]=A[i];
		sum+=A[i];
		if (sum>k)
			sum=0,caz=1;
	}
}
void precompute()
{
	int i,j;
	ll part;
	for (i=1; i<=n; i++)
	{
		part=0;
		for (j=i; j<=2*n; j++)
		{
			part+=A[j];
			if (part>k)
			{
				B[i]=j-1;
				if (B[i]>n)
					B[i]-=n;
				part-=A[j];
				C[i]=part;
				break ;
			}
		}
	}
}
void solve()
{
	memset(viz,0,sizeof(viz));
	int st=1,new_pos;
	viz[1]=1; 
	while (steps<r)
	{
		steps++;
		new_pos=B[st]+1;
		if (new_pos>n)
			new_pos-=n;
		rez+=C[st];
		E[steps]=E[steps-1]+C[st];
		last_visit=new_pos;
		if (viz[new_pos])
		{
			poz_st=D[new_pos];
			break ;
		}
		else
		{
			D[new_pos]=steps;
			st=new_pos;
			viz[st]=1;
		}
	}
}
void simulare()
{
	steps=0;
	int st=last_visit,new_pos;
	while (steps<r)
	{
		steps++;
		new_pos=B[st]+1;
		rez+=C[st];
		st=new_pos;
	}
}
int main()
{
	//freopen("pb3.in","r",stdin);
	//freopen("pb3.out","w",stdout);
	scanf("%d",&t);
	int i,per;
	ll part2;
	for (i=1; i<=t; i++)
	{
		sum=0; caz=0; rez=0; steps=0; poz_st=0; cicluri=0;
		read();
		if (!caz)
		{
			printf("Case #%d: %lld\n",i,sum*r);
			continue ;
		}
		precompute();
		solve();
		if (steps==r)
		{
			printf("Case #%d: %lld\n",i,rez);
			continue ;
		}
		rez=E[poz_st];
		r-=poz_st;
		per=steps-poz_st;
		part2=(ll)E[steps]-rez;
		cicluri=r/per;
		rez+=part2*cicluri;
		r-=cicluri*per;
		simulare();
		printf("Case #%d: %lld\n",i,rez);
	}
	return 0;
}
