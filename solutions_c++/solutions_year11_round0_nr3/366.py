#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#pragma comment(linker, "/STACK:167772160")
typedef long long int64;
using namespace std;
int tes,o,n,i,a[1001],s;
int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>tes;
	for(o=0;o<tes;o++)
	{
		cin>>n;
		for(i=0;i<n;i++)scanf("%d",&a[i]);
		s=0;
		for(i=0;i<n;i++)s=(s^a[i]);

		if(s!=0)cout<<"Case #"<<o+1<<": "<<"NO"<<endl;else
		{
			sort(a,a+n);
			s=0;
			for(i=1;i<n;i++)s+=a[i];

			cout<<"Case #"<<o+1<<": "<<s<<endl;


		}
	}
}