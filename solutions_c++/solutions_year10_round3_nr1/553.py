#include <iostream>

using namespace std;

int t,n;
int a[1000],b[1000];
int x;

int main()
{
	int c,i,j;
	cin>>t;
	for (c=1; c<=t; c++)
	{
		//Do here
		cin>>n;
		x=0;
		for (i=0; i<n; i++)
			cin>>a[i]>>b[i];
		for (i=0; i<n-1; i++)
			for (j=i+1; j<n; j++)
				if (!(a[i]<=a[j]&&b[i]<=b[j]||a[i]>=a[j]&&b[i]>=b[j]))
					x++;
cout<<"Case #"<<c<<": "<<x<<endl;
		/*if (n==1)
		
		cout<<"Case #"<<c<<": "<<0<<endl;
		if (n==2)
			if (a[1]<a[0]&&b[1]<b[0]||a[1]>a[0]&&b[1]>b[0])
				cout<<"Case #"<<c<<": "<<0<<endl;
			else cout<<"Case #"<<c<<": "<<1<<endl;*/
	}
	return 0;
}
