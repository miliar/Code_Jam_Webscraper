#include<iostream>
#include<algorithm>
using namespace std;

int t,n,sum,x;
int num[1000];

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("C-small-attempt0.in","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int ca=1;ca<=t;++ca)
	{
		cin>>n;
		
		printf("Case #%d: ",ca);
		x=sum=0;
		for(int i=0;i<n;++i)
		{
			cin>>num[i];
			x^=num[i];
			sum+=num[i];
		}
		if(x)
		{
			puts("NO");
		}
		else
		{
			cout<<sum-*min_element(num,num+n)<<endl;
		}
	}
	return 0;
}
