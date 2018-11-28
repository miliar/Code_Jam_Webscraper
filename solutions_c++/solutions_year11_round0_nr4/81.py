#include <iostream>
using namespace std;
int main()
{
	int t,i,j,n,a;
	double s;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		s=0;cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>a;
			if(a!=i+1) s++;
			
		}
		cout<<"Case #"<<j<<": ";
		printf("%.6lf\n",s);
	}
}
