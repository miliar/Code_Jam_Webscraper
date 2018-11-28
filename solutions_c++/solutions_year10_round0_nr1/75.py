#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cmath>
#include<string>
#include<utility>
#include<cstdlib>
#include<ctime>
using namespace std;
int T,n,k,i;
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (i=1;i<=T;i++)
	{
		cin>>n>>k;
		cout<<"Case #"<<i<<": ";
		if ((k%(1<<n))==((1<<n)-1)) cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}
	return 0;
}
