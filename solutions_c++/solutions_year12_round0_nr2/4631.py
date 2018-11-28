#include<iostream>
using namespace std;
int main()
{
	int ca,n,s,p,x,i,ans,test=0;
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin>>ca;
	while(ca--)
	{
		cin>>n>>s>>p;
		ans=0;
		for(i=1;i<=n;i++)
		{
			cin>>x;
			if(p==0) ans++;
            else if(x>=3*p-2) ans++;
			else if(x>=3*p-4 && x>0 && s>0) {s--;ans++;}
		}
		cout<<"Case #"<<++test<<": "<<ans<<endl;
	}
	return 0;
}