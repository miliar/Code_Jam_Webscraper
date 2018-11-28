//We believe ourselves
#include "cstdlib"
#include "cctype"
#include "cstring"
#include "cstdio"
#include "cmath"
#include "algorithm"
#include "vector"
#include "string"
#include "set"
#include "map"
#include "iostream"
#include "sstream"
#include "queue"
using namespace std;

//----------------------------------------

struct ff
{
	__int64 val;
}f[1100];

__int64 hash[1100];
__int64 temp[1100];

int main()
{

	freopen("D:\\C-large.in","r",stdin);
	freopen("D:\\C-large.out","w",stdout);


	__int64 r,k,n;
	__int64 i,j;
	__int64 t;
	__int64 sum;
	scanf("%I64d",&t);
	int ca=0;
	while(t--)
	{
		ca++;
		scanf("%I64d %I64d %I64d",&r,&k,&n);
		sum=0;
		for(i=1;i<=n;i++)
		{
			scanf("%I64d",&f[i].val);
			sum+=f[i].val;
		//	printf("%I64d\n",sum);
		}
		printf("Case #%d: ",ca);
		memset(hash,0,sizeof(hash));
		if(sum<=k)
		{
			printf("%I64d\n",sum*r);
			continue;
		}
		__int64 s=1;
		__int64 huan=-1;
		bool flag=false;
		__int64 st;
		temp[0]=0;
		for(i=1;i<=r;i++)
		{
			if(hash[s]!=0)
			{
				huan=i-hash[s];
				flag=true;
				st=hash[s]-1;
				break;
			}
			hash[s]=i;

			sum=0;
			for(s;;s++)
			{
				if(s>n)
					s=s-n;
				sum=sum+f[s].val;
				if(sum>k)
				{
					sum=sum-f[s].val;
					break;
				}
			}

			temp[i]=temp[i-1]+sum;

		}
		if(flag==false)
			printf("%I64d\n",temp[r]);
		else
		{
			__int64 ans=0;
			ans=ans+temp[st];
			__int64 jie=temp[st+huan]-temp[st];
			r=r-st;
			ans=ans+jie*(r/huan);
			r=r%huan;
			ans=ans+temp[st+r]-temp[st];
			printf("%I64d\n",ans);
		}

	}
	return 0;
}

