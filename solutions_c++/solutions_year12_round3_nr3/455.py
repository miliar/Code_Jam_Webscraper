#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <algorithm>
#define _clr(a,b) (memset((a),(b),sizeof((a))));
#define print(cas) printf("Case #%d: ",(cas)++); 
#define inf 1<<25;
using namespace std;

int n,m;
__int64 a[10],b[105];
int odr1[10],odr2[105];
__int64 maxans;

void dfs(int index1,int index2,__int64 sum)
{
	int i;
	if(index1==n||index2==m)
	{
		if(sum>maxans)maxans=sum;
		return ;
	}
	dfs(index1+1,index2,sum);
	for(i=index2;i<m;i++)
	{
		if(odr1[index1]==odr2[i])
		{
			__int64 temp;
			if(a[index1]==b[i])
			{
				temp=a[index1];
				a[index1]=b[i]=0;
				dfs(index1+1,i+1,sum+temp);
				a[index1]=b[index1]=temp;
			}
			else if(a[index1]>b[i])
			{
				temp=b[i];
				a[index1]-=b[i];
				b[i]=0;
				dfs(index1,i+1,sum+temp);
				a[index1]+=temp;
				b[i]=temp;
			}
			else 
			{
				temp=a[index1];
				b[i]-=a[index1];
				a[index1]=0;
				dfs(index1+1,i,sum+temp);
				b[i]+=temp;
				a[index1]=temp;
			}
			break;
		}
	}
}

int main()
{
	int cas=1,txt,i,j;
	freopen("1.in","r",stdin);
	freopen("2.txt","w",stdout);
	scanf("%d",&txt);
	while(txt--)
	{
		maxans=0;
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
			scanf("%I64d %d",&a[i],&odr1[i]);
		for(i=0;i<m;i++)
			scanf("%I64d %d",&b[i],&odr2[i]);
		dfs(0,0,0);
		print(cas);
		printf("%I64d\n",maxans);
	}
	return 0;
}

