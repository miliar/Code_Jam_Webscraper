#include<iostream>
#include<algorithm>
using namespace std;

int p[1000],v[1000];
bool a[1000];
int main()
{
	int t,n,k,b,t1,num,num1,mm=1,i,j;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&t1);
	while(t1--)
	{
		scanf("%d%d%d%d",&n,&k,&b,&t);
		memset(a,false,sizeof(a));
		num=0;num1=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&p[i]);
		}
		for(i=0;i<n;i++)
		{
			scanf("%d",&v[i]);
		}
		for(i=0;i<n;i++)
		{
			if(t*v[i]+p[i]>=b){a[i]=true;}
		}
		num=0;
		for(i=n-1;i>=0;i--)
		{
			if(a[i])
			{
				num++;
				for(j=i+1;j<n;j++)
				{
					if(a[j]==false)num1++;
				}
				if(num==k)break;
			}
		}
		//cout<<num<<endl;
		if(num<k)
			printf("Case #%d: IMPOSSIBLE\n",mm++);
		else 
			printf("Case #%d: %d\n",mm++,num1);
	}
	return 0;
}
