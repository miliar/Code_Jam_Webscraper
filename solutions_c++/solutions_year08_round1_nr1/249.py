#include <vector>
#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	freopen("ans2.out","w",stdout);
	freopen("in.in","r",stdin);
	int a[810],b[810];
	int n,i,j;
	int aa,aaa,bb,bbb;
	int t,st;
	__int64 sum,tt;
	scanf("%d",&st);
	for (t=0;t<st;++t)
	{
		scanf("%d",&n);
		for (i=0;i<n;++i) scanf("%d",a+i);
		for (i=0;i<n;++i) scanf("%d",b+i);
		sort(a,a+n);sort(b,b+n);
		sum=0;
		for (i=0;i<n;++i)
		{
			tt=a[i];
			tt*=b[n-1-i];
			sum+=tt;
		}
		cout<<"Case #"<<t+1<<": "<<sum<<endl;
	}
	return 0;
}




