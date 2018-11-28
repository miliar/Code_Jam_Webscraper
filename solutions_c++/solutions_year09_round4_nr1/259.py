#include <iostream>
#include <string>
#include <cstdio>
#include <utility>
#include <cstring>

using namespace std;

int N;
int arr[128];

int solve(int n)
{
	if (n==N) return 0;
	int k;
	for(k=n; arr[k]>n; ++k) ;
	if (k==n) return solve(n+1);
	memmove(arr+n+1, arr+n, (k-n)*4);
	return (k-n)+solve(n+1);
}

int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>N;
		string s;
		for(int i=0; i<N; ++i) {
			cin>>s;
//			cout<<N<<' '<<s<<'\n';
			int j;
			for(j=N-1; j>=0; --j)
				if (s[j]=='1') break;
			arr[i]=max(j,0);
//			cout<<j<<'\n';
		}
		printf("Case #%d: %d\n", a,solve(0));
	}
}
