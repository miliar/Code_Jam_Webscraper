#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdio>
#include<iomanip>
#include<map>
#include<set>
#include<vector>
#include<list>
#include<deque>
#include<cstdlib>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

int main()
{
	long i,tests,n,k;
	cin>>tests;
	freopen("tt.out","w",stdout);
	for(i=1;i<=tests;i++)
	{
		cin>>n>>k;
		k%=1<<n;
		cout<<"Case #"<<i<<": ";
		if(k==(1<<n)-1)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
	}
return 0;
}