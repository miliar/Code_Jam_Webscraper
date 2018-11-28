#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<string>
#include<cmath>
using namespace std;

int n,i,j,k,l;
char a[100][100];
int v[100],nr;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int T,I;
	cin>>T;
	for(I=1;I<=T;++I)
	{
		cin>>n;
		nr = 0;
		for(i=1;i<=n;++i)
			cin>>a[i];
		for(i=1;i<=n;++i)
		{
			v[i] = n;
			j = n-1;
			while(a[i][j]=='0' && j>=0)
			{
				--v[i];
				--j;
			}
		}
		for(i=1;i<=n;++i)
			if(v[i]<=i) continue;
			else
			{
				for(j=i+1;j<=n;++j)
					if(v[j]<=i) break;
				nr += j-i;
				for(;j>i;--j)
					swap(v[j],v[j-1]);
			}
		cout<<"Case #"<<I<<": "<<nr<<endl;
	}
	return 0;
}
