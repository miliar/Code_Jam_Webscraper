#include <iostream>
#include <string>

using namespace std;

int main()
{
	int i,t,n,j;
	long long c,sum,xor,mn;
	freopen("C-large.in","r",stdin); 
	freopen("output.txt","w",stdout);
	cin>>t;

	for(i=0;i<t;i++)
	{
		sum=0; xor=0; mn=1000001;
		cin>>n;
		for(j=0;j<n;j++)
		{
			cin>>c;
			xor^=c;
			sum+=c;
			if(mn>c) mn=c;
		}
		if(xor==0) {cout<<"Case #"<<i+1<<": "<<sum-mn<<endl;} else {cout<<"Case #"<<i+1<<": "<<"NO"<<endl;} 
	}
	fclose(stdin); fclose(stdout);
}