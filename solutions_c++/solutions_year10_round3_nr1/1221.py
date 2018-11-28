#include "iostream"
using namespace std;
int main(void) 
{
	int t,n,a[1000],b[1000],res,i,j,k;
	cin>>t;
	for (i = 1; i <= t; i++)
	{
		res = 0;
		cin>>n;
		for (j=0; j<n; j++)
		{
			cin>>a[j];
			cin>>b[j];
		}
		for (j=0; j<n; j++)
		{
			for (k=(j+1); k<n; k++)
			{
				if(((a[j]<a[k])&&(b[j]>b[k]))||((a[j]>a[k])&&(b[j]<b[k])))
					res+=1;				
			}
		}
		cout<<"Case #"<<i<<": "<<res<<"\n";
	}
	return 0;
}
