#include <algorithm>
#include <cmath>
using namespace std;
#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <set>

//By chyx111
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
#define SZ(a) ((int)(a).size())

int const N = 2100000;
int neighbor[N][10];
int nn[N];
int main() {
	string text;
	memset(nn,0,(sizeof nn));
	for(int i = 1; i < N; ++i){
		stringstream ss;
		ss << i;
		ss >> text;
		int sz = SZ(text);
		Rep(j, sz)if(text[j] != '0'){
			int t = 0;
			Rep(k, sz){
				t = t * 10 + text[(j + k) % sz] - '0';
			}
			if(t > i){
				neighbor[i][nn[i]++] = t;
			}
		}
		sort(neighbor[i], neighbor[i] + nn[i]);
		nn[i] = unique(neighbor[i], neighbor[i] + nn[i]) - neighbor[i];
		if(i % 10000 == 0)cerr << "\r" << i;
		//if(rand() % 10000 == 0){
		//	cout << i << ": ";
		//	Rep(j, nn[i]){
		//		cout << neighbor[i][j] << " ";
		//	}
		//	cout << endl;
		//}
	}
	int ca;
	scanf("%d", &ca);
	Rep(ica, ca){
		int a, b;
		int ans = 0;
		scanf("%d%d", &a, &b);
		for(int i = a; i <= b; ++i){
			Rep(j, nn[i]){
				if(neighbor[i][j] > b){
					break;
				}
				ans++;
			}
		}
		fprintf(stderr, "Case #%d: %d\n", ica + 1, ans);
		printf("Case #%d: %d\n", ica + 1, ans);
	}
	return 0;
}

