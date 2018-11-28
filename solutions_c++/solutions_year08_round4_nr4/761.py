#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>

#include <algorithm>

#define INF 100005

using namespace std;



#define SZ 1005
#define SZ2 10


char str[SZ];
char tmpstr[SZ];

long perm[SZ2];

long fact[]={1,1,2,6,24,120};

long process(long k);


int main()
{
	long i,j,k,kase,inp,n,temp,res,m,x,y,z;

//	freopen("D-sample.in","r",stdin);
//	freopen("D-sample.out","w",stdout);

	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small.out","w",stdout);

//	freopen("D-large.in","r",stdin);
//	freopen("D-large.out","w",stdout);

	
	scanf("%I64d",&inp);
	for(kase=1;kase<=inp;kase++)
	{
		scanf("%ld",&k);
		scanf("%s",str);
		for(i=0;i<k;i++)
		{
			perm[i]=i;
		}
		
		res=process(k);
		while(next_permutation(perm,perm+k))
		{
			temp=process(k);
			if(temp<res)
				res=temp;
		}
		printf("Case #%ld: %ld\n",kase,res);
	}
	return 0;
}

long process(long k)
{
	long len,i,cnt,j;
	len = strlen(str);
	for(i=0;i<len;i++)
	{
		tmpstr[i]=str[(i/k)*k+perm[i%k]];
	}
	cnt=0;
	for(i=0;i<len;)
	{
		cnt++;
		j=i+1;
		while(tmpstr[j]==tmpstr[j-1])
			j++;
		i=j;
	}
	return(cnt);
}

int sortfunc(const void *a, const void *b)
{
	long *x=(long *)a;
	long *y=(long *)b;
	if(*x>*y)
		return 1;
	if(*x<*y)
		return -1;
	return 0;
}
