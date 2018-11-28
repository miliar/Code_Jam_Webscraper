#include <iostream>
#include <vector>
using namespace std;
typedef vector<int> VI;
typedef vector<long long> VL;

int main() {
	int t;
	cin>>t;
	for (int c=1;c<=t;++c) {
		int r,k,n;
		cin>>r>>k>>n;
		VI g(n);
		VI d(n,-1);
		VL s(n);
		VI jmp(n);
		VL p(n);
		long long ss=0L;
		for (int i=0;i<n;++i) {
			cin>>g[i];
			ss+=g[i];
		}
		
		// trivial case
		if (ss<=k) {
			cout<<"Case #"<<c<<": "<<ss*r<<endl;
			continue;
		}
		
		// set up jump table (linear)
		long long z=0L;
		int j=n-1;
		for (int i=0;i<n;++i) {
			for (j=(j+1)%n;z<=k;j=(j+1)%n)
				z+=g[j];
			j=(j+n-1)%n;
			jmp[i]=j;
			p[i]=z-g[j];
			z-=g[i];
		}
		
		// simulation with loop detection (linear in n)
		int i=0;
		j=0;
		long long x=0L;
// 		bool end=false;
		bool end=true;
		while (r) {
			if (end) {
				--r;
			} else if (d[i]<0) {
				d[i]=j;
				s[i]=x;
				--r;
			} else {
				long long xx=x-s[i];
				int dd=j-d[i];
				x+=xx*(r/dd);
				r=r%dd;
				end=true;
			}
			
			x+=p[i];
			i=jmp[i];
			++j;
		}
		cout<<"Case #"<<c<<": "<<x<<endl;
	}
	return 0;
}
