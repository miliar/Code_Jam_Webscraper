#include<cstdio>
#include<cstring>
#include<algorithm>
#define mxn 5000
using namespace std;
int p[mxn],rank[mxn],ct=0;
int prime[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009};
void makeset(int x)
{
	rank[x]=0;
	p[x]=x;
	ct++;
}
void init()
{
	ct=0;
	memset(p,0,sizeof(p));
	memset(rank,0,sizeof(rank));
}
int findset(int x)
{
	int px=x,i;
	while (px!=p[px]) px=p[px]; 
	while (x!=px)
	{
		i=p[x];
		p[x]=px;
		x=i;
	}
	return px;
}

void unionset (int x , int y)
{
	ct--;
	if( rank[x] > rank[y]) p[y]=x;
	else
	{
		p[x]=y;
		if( rank[x]==rank[y]) rank[y]++;
	}
}
int main()
{
	int i,j,k,t,a,b,pp,o=0;
	bool ff;
	freopen("gcd__b.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		init();
		scanf("%d%d%d",&a,&b,&pp);
		for (i=a;i<=b;i++) makeset(i);
		ff=1;
		while(ff)
		{
			ff=0;
			for (i=a;i<b;i++)
				for (j=i+1;j<=b;j++)
				{
					int fi=findset(i);
					int fj=findset(j);
					if (fi!=fj)
					{
						for (k=0;prime[k]<1000;k++)
						{
							if (prime[k]<pp) continue;
							if (i%prime[k]==0 && j%prime[k]==0) 
							{
								unionset(fi,fj);
								ff=true;
								break;
							}
						}
					}
				}
		}
		printf("Case #%d: %d\n",++o,ct);
	}
	fclose(stdout);
	return 0;
}
