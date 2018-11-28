#include <iostream>
using namespace std;
int main()
{
	int T,N,minv,a,i;
	unsigned int sum,res;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	cin>>T;

	for(i=1;i<=T;++i)
	{
		cin>>N;
		sum=0;
		res=0;
		minv=10000000;
		while(N--)
		{
			cin>>a;
			if(a<minv)
				minv=a;
			sum+=a;
			res^=a;
		}
		sum-=minv;
		if(res!=0)
			cout<<"Case #"<<i<<": NO"<<endl;
		else
		{
			cout<<"Case #"<<i<<": "<<sum<<endl;
		}
	}
	return 0; 
}