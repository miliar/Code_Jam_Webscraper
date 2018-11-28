#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int> > words;
#define fu(i,m,n) for(int i=m; i<n; i++)
typedef long long i64;


int main(void) {
	int T;
	cin >> T;
	fu(t,0,T) {
		int N;
		cin >> N;
		int vals[N];
		fu(i,0,N) {
			char x; int n=-1;
			fu(j,0,N) {
				cin >> x;
				if(x=='1') n=j;
			}
			vals[i]=n;
		}
		int ret=0;
		for(int i=0; i<N;i++) {
			for(int j=i; j<N; j++) {
				if(vals[j]<=i) {
					for(int k=j-1; k>=i; k--) {
						swap(vals[k],vals[k+1]);
						ret++;
					}
					break;
				}
			}
		}
		cout << "Case #" << t+1 << ": " << ret << endl;
	}
}
