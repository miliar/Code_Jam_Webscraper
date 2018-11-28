#include <iostream>
#include <string>

using namespace std;

int K;
string S;
int perm[16];
int result;
bool remain[16];

int count() {
	char* s = new char[S.length()];
	int i = 0;
	while(i < S.length()) {
		for(int j=0; j<K; j++)
			s[i+j] = S[i+perm[j]];
		i+= K;
	}
	int r = 1;
	for(int j=1; j<S.length(); j++)
		if(s[j] != s[j-1])
			r ++;
	delete[] s;
	return r;
}

void work(int k) {
	if(k == K) {
		int r = count();
		if(r < result)
			result = r;
		return;
	}
	for(int i=0; i<K; i++)
		if(remain[i]) {
			perm[k] = i;
			remain[i] = false;
			work(k+1);
			remain[i] = true;
		}
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>K >>S;
		result = 10000;
		memset(remain, 1, sizeof(remain));
		work(0);
		cout <<"Case #" <<i+1 <<": " <<result <<endl;
	}
}

/*
d:\Documents\Visual Studio 2008\Projects\GoogleCodeJam\Debug\
*/