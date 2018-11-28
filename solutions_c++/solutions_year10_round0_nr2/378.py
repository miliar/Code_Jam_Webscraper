#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
long long num[10];
int N;
long long gcd(long long a,long long b)
{
	if(a>b)
		return gcd(b,a);
	if(a==0)
		return b;
	return gcd(b%a,a);
}
bool judge(long long ans,long long tmp)
{
	for(int i=0;i<N;i++)
	{
		if((num[i]+ans)%tmp!=0)
			return false;
	}
	return true;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>N;
		for(int i=0;i<N;i++)
			cin>>num[i];
		sort(num,num+N);
		long long tmp=num[1]-num[0];
		for(int i=0;i<N;i++)
			for(int j=i+1;j<N;j++)
			{
				tmp=gcd(tmp,num[j]-num[i]);
			}
		long long k=num[N-1];
		long long ans=0;
		if(k%tmp==0)
			ans=0;
		else
			ans=tmp-k%tmp;
		while(!judge(ans,tmp))
			ans+=tmp;
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}