#include<iostream>
using namespace std;
long long t,n,h1,h2,mn,ss,cc=1;
int main(){
	//freopen("out.txt","w",stdout);
	//freopen("C-large.in","r",stdin);
	cin>>t;
	while(t--)
	{
		cin>>n;
		long long res=0;
		ss=mn=0;
		for(h1=0;h1<n;h1++)
		{
			cin>>h2;
			ss+=h2;
			res^=h2;
			if(!mn)mn=h2;
			else mn=min(mn,h2);
		}
		cout<<"Case #"<<cc++<<": ";
		if(res)cout<<"NO\n";
		else cout<<ss-mn<<endl;
	}
}
