#include "iostream"
using namespace std;
int main(void) 
{
	unsigned long int r,k,n,g[1000],res,t,x,y,tres,i,j;
	cin>>t;
	for (i = 1; i <= t; i++)
	{
		cin>>r;
		cin>>k;
		cin>>n;
		for (j = 0; j < n; j++)
			cin>>g[j];
		res=0;
		x=0;
		for (j = 1; j <= r; j++)
		{
			tres=0;
			y=x;
			while((tres+g[x])<=k)
			{
				tres=tres+g[x];
				x++;
				x=x%n;
				if(x==y)
					break;
			}
			res=res+tres;			
		}
		cout<<"Case #"<<i<<": "<<res<<"\n";
	}
	return 0;
}
