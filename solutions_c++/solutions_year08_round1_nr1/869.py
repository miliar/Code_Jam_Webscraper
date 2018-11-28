#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int a[1000],b[1000],t,n,i,j;
	long s;
	cin >>t;j=0;
	while(t--)
	{
		cin >>n;j++;
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(i=0;i<n;i++)
			scanf("%d",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		s=0;
		for(i=0;i<n;i++)
			s=s+a[i]*b[n-i-1];
		cout <<"Case #"<<j<<": "<<s<<endl;
	}
	return 0;
}
