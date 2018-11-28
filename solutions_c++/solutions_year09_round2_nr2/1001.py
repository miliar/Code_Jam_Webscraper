#include <iostream>
#include <list>
#include <set>
#include <string>
#include <assert.h>
#include <vector>
#include <algorithm>

#define _CRT_SECURE_NO_WARNINGS

#define For(v, m, n) for(int v = m; v < n; ++v)
#define InOut(name) freopen("..\\" ##  #name ## ".in","r", stdin); \
	freopen("..\\" ##  # name  ## ".out", "w", stdout);
#define In(name) freopen("..\\" ##  #name ## ".in","r", stdin);
#define MAX(a, b) ((a)>(b))?(a):(b)
#define MIN(a, b) ((a)<(b))?(a):(b)

using namespace std;

int main() {
	InOut(B-large);
	int T; cin>>T;
	for(int i = 0; i < T; ++i) {
		string number;cin>>number;
		cout<<"Case #"<<i+1<<": ";
		list<int> jegyek;
		for(string::iterator iter = number.begin(); iter != number.end(); ++iter) {
			jegyek.push_back(*iter - '0');
		}
		list<int> save;
		for(list<int>::iterator iter = jegyek.begin(); iter != jegyek.end(); ++iter) {
			save.push_back(*iter);
		}
		if (next_permutation<list<int>::iterator>(jegyek.begin(), jegyek.end())) {
			for(list<int>::iterator iter = jegyek.begin(); iter != jegyek.end(); ++iter) {
				cout<<*iter;
			}
		}
		else {
			save.push_front(0);
			next_permutation<list<int>::iterator>(save.begin(), save.end());
			for(list<int>::iterator iter = save.begin(); iter != save.end(); ++iter) {
				cout<<*iter;
			}
		}
		cout<<endl;
	}
	return 0;
}