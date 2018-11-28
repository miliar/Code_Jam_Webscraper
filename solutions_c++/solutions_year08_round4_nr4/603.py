#include "stdio.h"
#include "string.h"

int num[100],l,k,min;
bool ex[100]={0};
char s[100000],s1[100000];

void find(int p)
{
	int i,t,m;
	if(p>=k)
	{
		for(i=0;i<k;i++)
		{
			t=0;
			while(t*k<l)
			{
				s1[t*k+i]=s[num[i]+t*k];
				t++;
			}
		}
		m=1;
		i=1;
		while(i<l)
		{
			if(s1[i]!=s1[i-1])
			{
				m++;
			}
			i++;
		}
		if(m<min)
		{
			min=m;
		}
		return ;
	}
	for(i=0;i<k;i++)
	{
		if(!ex[i])
		{
			num[p]=i;
			ex[i]=1;
			find(p+1);
			ex[i]=0;
		}
	}
}

int main()
{
	freopen("small.txt","r",stdin);
	freopen("small_out.txt","w",stdout);
	int v,ca;
	scanf("%d",&ca);
	for(v=1;v<=ca;v++)
	{
		scanf("%d%s",&k,s);
		l=strlen(s);
		s1[l]='\0';
		min=1000000;
		find(0);
		printf("Case #%d: %d\n",v,min);
	}
	return 0;
}