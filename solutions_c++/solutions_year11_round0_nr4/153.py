#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#define M 1010
using namespace std;
int f[M],s[M];
int main()
{
	int t,cas = 0;
	//freopen("./d.in","r",stdin);
	//freopen("./dd.out","w",stdout);
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		for(int i = 0; i < n; ++i){
			cin>>f[i];
			s[i] = f[i];
		}
		sort(s,s+n);
		double ans = 0;
		for(int i = 0; i < n; ++i)
			if(s[i] != f[i])
				ans += 1.0;
		cout<<"Case #"<<++cas<<": ";
		printf("%.6f\n",ans);
	}
	return 0;
}

