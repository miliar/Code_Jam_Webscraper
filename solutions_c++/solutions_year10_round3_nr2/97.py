#include<iostream>
#include<string>
using namespace std;

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t;
	int cas=1;
	cin>>t;
	long long l,p,c;
	while(t--)
	{
		cin>>l>>p>>c;
		long long k=(p-1)/l+1;
		int res=0;
		while(c<k)
		{
			res++;
			c*=c;
		}
		cout<<"Case #"<<cas++<<": "<<res<<'\n';
	}
	return 0;
}