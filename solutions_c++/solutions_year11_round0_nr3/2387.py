#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int d[2000];

int main(int argc, char **argv)
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,I,n,i,r;
	long long s;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n;
		r=0;
		for(i=0;i<n;i++) {
			cin>>d[i];
			r^=d[i];
		}
		if(r) printf("Case #%d: NO\n",I);
		else {
			sort(d,d+n);
			s=0;
			for(i=1;i<n;i++) s+=d[i];
			printf("Case #%d: %lld\n",I,s);
		}
	}
		
	return 0;
}

