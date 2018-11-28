#include <iostream>
#include <list>
#include <set>
#include <string>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <sstream>

#define _CRT_SECURE_NO_WARNINGS

#define For(v, m, n) for(int v = m; v < n; ++v)
#define InOut(name) freopen("..\\" ##  #name ## ".in","r", stdin); \
	freopen("..\\" ##  # name  ## ".out", "w", stdout);
#define In(name) freopen("..\\" ##  #name ## ".in","r", stdin);
#define MAX(a, b) ((a)>(b))?(a):(b)
#define MIN(a, b) ((a)<(b))?(a):(b)
#define isLowerCase(c) ('a' < c && c <'z')
#define isUpperCase(c) ('A' < c && c < 'Z')
#define isChar(c) (isLowerCase(c) || isUpperCase(c))
#define isDigit(c) ('0' < c && c < '9')
#define isWhiteSpace(c) (c == ' ' || c == '\n' || c == '\t' || c == '\b')

using namespace std;

int main() {
	InOut(C-small-attempt0);
	int N; cin>>N;
	For(i, 0, N) {
		int min_bribe = -1;
		int P; cin>>P;
		int Q; cin>>Q;
		list<int> q;
		For(j, 0, Q) {
			int t; cin>>t;
			q.push_back(t);
		}
		do {
			int bribe = 0;
			bool *cells = new bool[P];
			For(j, 0, P) {
				cells[j] = true;
			}
			for(list<int>::iterator iter = q.begin(); iter != q.end(); ++iter) {
				cells[*iter-1] = false;
				int a = *iter-2;
				while(a>-1 && cells[a]) {
					bribe++;
					--a;
				}
				a = *iter;
				while(a<P && cells[a]) {
					bribe++;
					++a;
				}
			}
			if (min_bribe == -1) {
				min_bribe = bribe;
			} else 
				min_bribe = MIN(bribe,min_bribe);
		} while (next_permutation(q.begin(),q.end()));
		cout<<"Case #"<<i+1<<": "<<min_bribe<<endl;
	}
	return 0;
}