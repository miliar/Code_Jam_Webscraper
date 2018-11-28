#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <utility>
#include <queue>
#include <map>
#include <sstream>

#include <cmath>

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned char UC;

using namespace std;

int main(void)
{
	int n;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {
		ULL result = 0;

		ULL r, k, n;
		cin >> r >> k >> n;
		vector<ULL> group(n);
		for(ULL i=0;i<n;++i) {
			cin >> group[i];
		}
		vector<pair<ULL, ULL> > t(n);
		ULL idx=0;
		for(ULL rr=0;rr<r;++rr) {
			if(t[idx].first != 0) {
				result += t[idx].first;
				idx = t[idx].second;
			} else {
				ULL pidx = idx;
				ULL sum = 0;
				while(sum+group[idx]<=k) {
					sum += group[idx];
					++idx; if(idx == n) idx = 0;
					if(idx == pidx) break;
				}
				t[pidx].first = sum;
				t[pidx].second = idx;
				result += sum;
			}
		}

		cout << "Case #" << nn+1 << ": " << result << endl;
	}
	
	return 0;
}
