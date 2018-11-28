#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
#include<vector>
using namespace std;
int k,n;
//int num[1024];
int main()
{
	//freopen("data.in","r",stdin);
	//freopen("C-large.out","w",stdout);
	
	cin>>k;
	int i,j;
	for(i=1;i<=k;++i)
	{
		cout<<"Case #"<<i<<": ";
		cin>>n;
		int m=0;
		int num;
		int sum=0;
		int minN=1<<30;
		for(j=0;j<n;++j)
		{
			cin>>num;
			m^=num;
			sum+=num;
			if(minN>num) minN=num;
		}
		if(m!=0) cout<<"NO"<<endl;
		else cout<<sum-minN<<endl;


	}
	return 0;
}