#include <cstdlib>
#include <iostream>
#include<fstream>

using namespace std;
long long a[200],b[200];
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
    long long i,j,t,n,m,k,r,sum,ans,p,q;
    a[0]=1;
    for(i=1;i<=170;i++)
    {
        a[i]=a[i-1]*2;
        b[i]=a[i]-1;
    }
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>n>>m;
		if((m-b[n])%a[n]==0)
		{
		    cout<<"Case #"<<j<<": ON"<<endl;
		}
		else{
		    cout<<"Case #"<<j<<": OFF"<<endl;
		}

	}
    return 0;
}
