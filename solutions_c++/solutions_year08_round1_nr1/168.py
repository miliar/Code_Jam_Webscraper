#include <iostream>
#include <algorithm>

using namespace std;

int N;
long long a[800], b[800];

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>N;
		for(int j=0; j<N; j++)
			cin >>a[j];
		for(int j=0; j<N; j++)
			cin >>b[j];
		sort(a, a+N);
		sort(b, b+N);
		long long r = 0;
		for(int j=0; j<N; j++)
			r += a[j] * b[N-1-j];
		cout <<"Case #" <<i+1 <<": " <<r <<endl;
	}
}

/*
d:\Documents\Visual Studio 2008\Projects\GoogleCodeJam\Debug\
*/