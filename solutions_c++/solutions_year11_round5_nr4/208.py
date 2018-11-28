#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#define uLL unsigned long long

using namespace std;

int tt;
int n;
string s;
uLL ans;

int main() {
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);

	scanf("%d\n",&tt);
	for (int ii=1;ii<=tt;++ii) {
		getline(cin,s);
		n=s.size()-1;
		for (int i=0;i<=n/2;++i) swap(s[i],s[n-i]);
		int cnt=0;
		for (int i=0;i<=n;++i)
			if (s[i]=='?') cnt++;
		ans=(uLL)1 << (uLL)50;
		for (int i=0;i<1 << cnt;++i) {
			int tmp=0;
			uLL now=0;
			for (int j=0;j<=n;++j) {
				if (s[j]=='1') now|=((uLL)1 << (uLL)j);
				if (s[j]=='?') {
					if ((i >> tmp) & 1) now|=((uLL)1 << (uLL)j);
					tmp++;
				}
			}
			uLL pp=(uLL)(sqrt(now)+1e-8);
			if (pp*pp==now) {
				printf("Case #%d: ",ii);
				tmp=0;
				for (int j=0;j<=n;++j)
					if (s[j]=='?') {
						if ((i >> tmp) & 1) s[j]='1';
						else s[j]='0';
						tmp++;
					}
				for (int j=n;j>=0;--j)
					printf("%c",s[j]);
				cout << endl;
				break;
			}
		}
	}
}
