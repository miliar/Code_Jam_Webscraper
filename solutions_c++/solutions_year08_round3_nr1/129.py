#include<iostream>
#include<algorithm>
using namespace std;

int p,n,k,l;
int val[1050];
int cmp(int a,int b)
{
	if(a>b)
		return 1;
	else
		return 0;
}
int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("Aa.out","w",stdout);
	int T,i,j,fre,t=1;
	__int64 sum=0;
	cin>>T;
	while(T--)
	{
		cin>>k>>p>>l;
		sum=0;
		for(i=0;i<l;i++)
		{
			scanf("%d",&val[i]);
		}

		sort(val,val+l,cmp);
	//	for(i=0;i<l;i++)
	//	{
	//		cout<<val[i]<<endl;
	//	}
		fre=l/p;

		for(i=0;i<fre;i++)
		{
			for(j=0;j<p;j++)
			{
				sum+=val[i*p+j]*(i+1);
			}
		}
		if(l%p!=0)
		{
			int ret=l-fre*p;
			for(i=fre*p;i<l;i++)
				sum+=val[i]*(fre+1);
		}
		printf("Case #%d: %I64d\n",t++,sum);
		//cout<<sum<<endl;
	}
	return 0;
}