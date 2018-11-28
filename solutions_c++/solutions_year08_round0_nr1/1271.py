#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

#define SZ 105
#define SZ2 1005

char names[SZ][SZ];
char input[SZ2][SZ];
long count[SZ];
long position[SZ][SZ2];
long current[SZ];

long find(char str[],long n);
int sortfunc(const void *a,const void *b);

int main()
{
	long s,q,inp,i,max,maxval,last,kase,ind,cnt,prev;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%ld",&inp);
	for(kase=1;kase<=inp;kase++)
	{
		scanf("%ld",&s);
		gets(names[0]);
		for(i=0;i<s;i++)
		{
			gets(names[i]);
		}
		memset(count,0,sizeof(count));
		memset(position,0,sizeof(position));
		memset(current,0,sizeof current);
		scanf("%ld",&q);
		gets(input[0]);
		for(i=1;i<=q;i++)
		{
			gets(input[i]);
			ind=find(input[i],s);
			position[ind][count[ind]]=i;
			count[ind]++;
		}
		for(i=0;i<s;i++)
		{
			qsort(position[i],count[i],sizeof(long),sortfunc);
		}
		last=0;
		max=-1;
		maxval=-1;
		cnt=0;
		prev=-2;
		while(last<=q)
		{
			for(i=0;i<s;i++)
			{
				while((position[i][current[i]]<last)&&(position[i][current[i]]!=0))
					current[i]++;
				if(position[i][current[i]]==0)
				{
					max=q+1;
					maxval=i;
					break;
				}
				if((position[i][current[i]]>max)&&(i!=prev))
				{
					max=position[i][current[i]];
					maxval=i;
				}
			}
			prev=maxval;
			last=max;
			if(max<=q)
				cnt++;
		}
		printf("Case #%ld: %ld\n",kase,cnt);
	}
	return 0;
}

long find(char str[],long n)
{
	long i;
	for(i=0;i<n;i++)
	{
		if(strcmp(str,names[i])==0)
			return(i);
	}
	return(-1);
}

int sortfunc(const void *a,const void *b)
{
	long *x=(long *)a;
	long *y=(long *)b;
	if(*x>*y)
	{
		return 1;
	}
	if(*x<*y)
	{
		return -1;
	}
	return 0;
}
