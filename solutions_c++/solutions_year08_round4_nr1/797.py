#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>

#define INF 10000000


#define SZ 10005
#define SZ2 1005

long store[SZ][2];
long gate[SZ];
long change[SZ];

int sortfunc(const void *a, const void *b);

void findforand(long i,long c);
void findforor(long i,long c);

int main()
{
	long i,j,k,kase,inp,n,l,p,temp,res,m,v;

//	freopen("A-sample.in","r",stdin);
//	freopen("A-sample.out","w",stdout);

//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small.out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%ld",&inp);
	for(kase=1;kase<=inp;kase++)
	{
		scanf("%ld %ld",&m,&v);
		for(i=0;i<=m;i++)
			store[i][0]=store[i][1]=INF;
		for(i=1;i<=(m-1)/2;i++)
		{
			scanf("%ld %ld",&gate[i],&change[i]);
		}
		for(i=(m-1)/2+1;i<=m;i++)
		{
			scanf("%ld",&l);
			store[i][l]=0;
		}
		for(i=(m-1)/2;i>0;i--)
		{
			if(gate[i]==1)
			{
				findforand(i,0);
				if(change[i]==1)
				{
					findforor(i,1);
				}
			}
			else
			{
				findforor(i,0);
				if(change[i]==1)
				{
					findforand(i,1);
				}
			}
		}
		printf("Case #%ld:",kase);
		if(store[1][v]<INF)
			printf(" %ld\n",store[1][v]);
		else
			printf(" IMPOSSIBLE\n");
	}
	return 0;
}

void findforand(long i,long c)
{
	if(store[i*2][0]+store[i*2+1][0]+c<store[i][0])
		store[i][0]=store[i*2][0]+store[i*2+1][0]+c;
	if(store[i*2][0]+store[i*2+1][1]+c<store[i][0])
		store[i][0]=store[i*2][0]+store[i*2+1][1]+c;
	if(store[i*2][1]+store[i*2+1][0]+c<store[i][0])
		store[i][0]=store[i*2][1]+store[i*2+1][0]+c;
	if(store[i*2][1]+store[i*2+1][1]+c<store[i][1])
		store[i][1]=store[i*2][1]+store[i*2+1][1]+c;
}

void findforor(long i,long c)
{
	if(store[i*2][0]+store[i*2+1][0]+c<store[i][0])
		store[i][0]=store[i*2][0]+store[i*2+1][0]+c;
	if(store[i*2][0]+store[i*2+1][1]+c<store[i][1])
		store[i][1]=store[i*2][0]+store[i*2+1][1]+c;
	if(store[i*2][1]+store[i*2+1][0]+c<store[i][1])
		store[i][1]=store[i*2][1]+store[i*2+1][0]+c;
	if(store[i*2][1]+store[i*2+1][1]+c<store[i][1])
		store[i][1]=store[i*2][1]+store[i*2+1][1]+c;
}

int sortfunc(const void *a, const void *b)
{
	__int64 *x=(__int64 *)a;
	__int64 *y=(__int64 *)b;
	if(*x>*y)
		return -1;
	if(*x<*y)
		return 1;
	return 0;
}
