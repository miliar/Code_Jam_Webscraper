#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> VI;

int swaps(VI& v, int k) {
/*	cerr << k << endl;
	for (int i=0;i<v.size();++i) cerr << v[i];
	cerr << endl;*/
	if (k==v.size()-1) return 0;
	int count=0;
	int i;
	for (i=k;i<v.size();++i) {
		if (v[i]<=k) break;
	}
	for (int j=i;j>k;--j) {
		swap(v[j],v[j-1]);
		count++;
	}
	return count+swaps(v,k+1);
}

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;++t) {
		int N;
		cin >> N;
		VI fill(N);
		for (int i=0;i<N;++i) {
			string s;
			cin >> s;
			for (int j=0;j<N;++j) {
				if (s[j]=='1') fill[i]=j;
			}
		}
		cout << "Case #" << t << ": " << swaps(fill,0) << endl;
	}
}

