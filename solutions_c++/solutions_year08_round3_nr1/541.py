#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<cmath>
using namespace std;
int main()
{
	int N;
	cin>>N;
	for(int cases=1;cases<=N;cases++)
	{
		int p,k,l;
		cin>>p>>k>>l;
		vector<long long> v(l);
		for(int i=0;i<l;i++)
				cin>>v[i];
		sort(v.begin(),v.end(),greater<long long>());
		long long ret=0;
		for(int i=0,m=1;i<l;m++)
		{
			int g=i;
			for(int j=i;j<k+g && i<l;j++,i++)
				ret+=(m*v[j]);
//cout<<ret<<".......\n";			
		}
		cout<<"Case #"<<cases<<": "<<ret<<endl;
	}
	return 0;
}
