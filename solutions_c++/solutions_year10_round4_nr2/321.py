#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
int P;
int M[1<<12];
ll price[1<<16];
ll need[1<<16];
int asd[1<<16];
void dfs(int a)
{
	if (a >= 1<<P) {
		int k = a - (1<<P);
		if (M[k]>0) M[k]--;
//		cout<<"lol "<<k<<' '<<M[k]<<'\n';
		return;
	}
	dfs(2*a);
	dfs(2*a+1);
}
int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		memset(asd,0,sizeof(asd));
		cin>>P;
		for(int i=0; i<1<<P; ++i) {
			cin>>M[i];
			M[i] = P-M[i];
		}
		for(int i=P-1; i>=0; --i) {
			for(int j=0; j<1<<i; ++j) {
				cin>>price[(1<<i) + j];
//				cout<<"asd "<<price[(1<<i)+j]<<'\n';
			}
		}
//		for(int i=1; i<1<<P; ++i) cout<<price[i]<<' ';
//		cout<<'\n';

		ll r=0;
		int it=1;
		while(1) {
//			cout<<"jee\n";
			int B = 1<<P;
			int mm=0;
			for(int i=0; i<1<<P; ++i) {
				need[B+i] = M[i] ? 1e9 : 0;
				mm += M[i];
			}
//			cout<<"mm "<<mm<<'\n';
			if (!mm) break;
			for(int i=B-1; i>0; --i) {
				ll p = min(price[i], need[2*i]+need[2*i+1]);
				need[i] = p;
			}
			ll b = max_element(M,M+B)-M;
			int z = (B+b)/2;
			int lz=0;
			while(z>0) {
				if (price[z]==need[z]) lz=z;
				z/=2;
			}
//			cout<<"lol lz "<<lz<<' '<<price[lz]<<'\n';
			dfs(lz);
			r += price[lz];
			price[lz] = 1e15;
#if 0
			for(int i=1; i<B; ++i) {
				if (asd[i/2]==it) asd[i]=it;
				else if (need[i]==price[i]) {
					r += price[i];
					price[i] = 1e15;
					asd[i]=it;
				}
			}
			for(int i=0; i<1<<P; ++i) {
				if (M[i]) --M[i];
			}
#endif
			++it;
		}
		cout<<"Case #"<<a<<": "<<r<<'\n';
	}
}
