#include <cstdio>
#include <algorithm>

#define MAX 2000100
using namespace std;

int value[1001];
int n,t;
int d1[MAX+100];
int d2[MAX+100];

void split()
{
	int i,sum=0,m=-1;
	int total=0;
	for(i=0;i<n;i++)
	{
		sum ^= value[i];
		total += value[i];
	}
	d1[0]=0;
	for(i=0;i<n;i++)
	{
		copy(d1,d1+MAX+100,d2);
		for(int j=0;j<MAX+1;j++)
			if(d1[j]!=-1)
				if(d1[j^value[i]]<d1[j]+value[i])
					d2[j^value[i]]=d1[j]+value[i];
		copy(d2,d2+MAX+100,d1);
	}

	for(i=0;i<MAX+1;i++)
	    if(d1[i]!=-1 && d1[i]!=total)
			if((sum^i)==i)
				m=max(m,d1[i]);
	if(m==-1)
		printf("NO\n");
	else
		printf("%d\n",m);
}


int main()
{
	freopen("l.in","r",stdin);
	freopen("l.out","w",stdout);
    scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		memset(value,0,sizeof(value));
		memset(d1,-1,sizeof(d1));
		scanf("%d",&n);
		for(int j=0;j<n;j++)
		{
			scanf("%d",&value[j]);
		}
		printf("Case #%d: ",i+1);
		split();
	
	}
	return 0;
}
