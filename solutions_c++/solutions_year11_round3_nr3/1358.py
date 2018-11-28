#include<iostream>
#include<algorithm>
using namespace std;

long long datain[1100];

long long gcd(long long a,long long b)
{
	if(a<b)
		return gcd(b,a);
	if(b==0)
		return a;
	else
		return gcd(b,a%b);
}

int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		long long N,L,H;
		bool ok;
		cin>>N>>L>>H;
		for(int j=0;j<N;++j)
		{
			cin>>datain[j];
		}
		sort(&datain[0],&datain[N]);
		long long resVal;
		ok=false;
		for(int j=L;j<=H;++j)
		{
			//check j;
			int count=0;
			for(int t=0;t<N;++t)
			{
				if(j%datain[t]==0)
				{
					++count;
				}
			}
			if(count==N)
			{
				ok=true;
				resVal=j;
				break;
			}

			count=0;
			for(int t=0;t<N;++t)
			{
				if(datain[t]%j==0)
				{
					++count;
				}
			}
			if(count==N)
			{
				ok=true;
				resVal=j;
				break;
			}
			//

			for(int t=0;t<N;++t)
			{
				int count1=0;
				int count2=0;
				for(int p=0;p<=t;++p)
				{
					if(j%datain[p]==0)
					{
						++count1;
					}
				}
				for(int p=t+1;p<N;++p)
				{
					if(datain[p]%j==0)
					{
						++count2;
					}
				}
				if(count1==t+1&&count2==N-t-1)
				{
					ok=true;
					resVal=j;
					break;
				}
			}
			if(ok)
			{
				break;
			}
		}


		if(ok)
		{
			printf("Case #%d: ",i);
			cout<<resVal<<endl;
		}
		else
		{
			printf("Case #%d: NO\n",i);
		}
	}
	return 0;
}