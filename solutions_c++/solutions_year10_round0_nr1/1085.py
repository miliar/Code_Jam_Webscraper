#include <iostream>
using namespace std;
int main()
{
//	freopen("d:\\A-large.in","r",stdin);
//	freopen("d:\\largeo.txt","w",stdout);
	int t,k,n,i;
	int pr[31];
	pr[0]=1;
	for (i=1;i<31;i++) pr[i]=pr[i-1]+pr[i-1];
	cin>>t;
	for (i=0;i<t;i++)
	{
		cin>>n>>k;
		k%=pr[n];
		//cout<<pr[n]<<endl;
		cout<<"Case #"<<i+1<<": ";
		if (k==pr[n]-1) cout<<"ON"; else cout<<"OFF";
		cout<<endl;
	}
	return 0;
}



