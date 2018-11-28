#include <iostream>
using namespace std;
struct point
{
	long long int x,y;
};
int main()
{
	long long int t,n,a,b,c,d,x,y,m;
	point arr[101];
	memset(arr,0,sizeof arr);
	cin>>t;
	for(int tn=1;tn<=t;tn++)
	{
		int count=0;
		cin>>n>>a>>b>>c>>d>>x>>y>>m;
		arr[0].x=x;
		arr[0].y=y;
		a%=m;
		c%=m;
		b%=m;
		d%=m;
		for(int i=1;i<=n-1;i++)
		{
			arr[i].x=((a*arr[i-1].x)%m+b)%m;
			arr[i].y=((c*arr[i-1].y)%m+d)%m;
//			cout<<arr[i].x<<" "<<arr[i].y<<endl;
		}
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
				for(int k=j+1;k<n;k++)
					if(((arr[i].x%3+arr[j].x%3+arr[k].x%3)%3==0)&&((arr[i].y%3+arr[j].y%3+arr[k].y%3)%3==0))
						count++;
		cout<<"Case #"<<tn<<": "<<count<<endl;
	}
      	return 0;
}
