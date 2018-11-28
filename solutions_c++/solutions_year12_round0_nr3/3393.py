#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <fstream>

using namespace std;

int t,a,b;
int num[101];

bool ok(int i,int j)
{
	char m[10],n[10],t1[10],t2[10];
	int k=0,p;
	for(k=0; i>0; k++)
	{
		m[k] = i%10+'0';
		i /= 10;
	}
	for(k=0; j>0; k++)
	{
		n[k] = j%10+'0';
		j /= 10;
	}
	m[k] = 0;
	n[k] = 0;
	/*strcpy(t1,m);
	strcpy(t2,n);
	sort(t1,t1+k);
	sort(t2,t2+k);
	if(strcmp(t1,t2))
		return 0;*/
	for(i=0; i<k; i++)
	{
		if(n[i]==m[0])
		{		
			p = i+1;
			for(j=1; j<k; j++)
			{
				if(p>=k)
					p = 0;
				if(m[j]!=n[p++])
					break;
			}
			if(j>=k)
				return 1;
		}
	}
	return 0;
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("output.out","w",stdout);
	int cas = 1,ans,i,j;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",cas++);
		scanf("%d%d",&a,&b);
		ans = 0;//cout<<a<<' '<<b<<endl;;
		for(i=a; i<=b; i++)
		{
			for(j=i+1; j<=b; j++)
				if(ok(i,j))
					ans++;
		}
		printf("%d\n",ans);
	}
	return 0;
}
