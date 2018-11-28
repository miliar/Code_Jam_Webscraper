#include <iostream>
using namespace std;
int K;
int a[256][256];

bool in(int x, int y)
{
	return x>=0 && y>=0 && x<K && y<K;
}
bool test(int a, int b, int c, int d)
{
	return !in(a,b) || !in(c,d) || ::a[a][b]==::a[c][d];
}
bool test1(int x, int y)
{
	for(int i=0; i<K; ++i) {
		for(int j=0; j<K; ++j) {
			int a = x+y - (i+j);
			int b = x-y + (j-i);
			if (a>=0 && !test(i,j,i+a,j+a)) return 0;
			if (b>=0 && !test(i,j,i+b,j-b)) return 0;
		}
	}
	return 1;
}
bool test2(int x, int y)
{
	for(int i=0; i<K; ++i) {
		for(int j=0; j<K; ++j) {
			int a = x+y - (i+j) - 1;
			int b = x-y + (j-i);
			if (a>=0 && !test(i,j,i+a,j+a)) return 0;
			if (b>=0 && !test(i,j,i+b,j-b)) return 0;
		}
	}
	return 1;
}
int max4(int a, int b, int c, int d)
{
	return max(max(a,b),max(c,d));
}
int f(int a, int b, int c, int d, bool k)
{
	int z = 2*max4(a,b,c,d) + (1-k);
	return z*z - K*K;
}

int main()
{
	int t;cin>>t;
	for(int z=1; z<=t; ++z) {
		cin>>K;
		for(int i=0; i<K; ++i)
			for(int j=0; j<=i; ++j)
				cin>>a[i-j][j];
		for(int i=1; i<K; ++i)
			for(int j=0; j<K-i; ++j)
				cin>>a[K-j-1][i+j];
		int r=1e9;
		for(int i=-2*K; i<=2*K; ++i) {
			for(int j=-2*K; j<=2*K; ++j) {
				if (test1(i,j)) r = min(r, f(i,j,K-i-1,K-j-1,0));
				if (test2(i,j)) r = min(r, f(i,j,K-i,K-j,1));
			}
		}
		cout<<"Case #"<<z<<": "<<r<<'\n';
	}
}
