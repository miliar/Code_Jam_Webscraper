#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define pv(v)  tr((v),i) cout << *i << " "; cout << endl
#define pr(i) cout << #i << "=" << (i) << endl
#define pr2(i,j) cout << #i << "=" << (i) << " " << #j << "=" << (j) << endl
#define pr3(i,j,k) cout << #i << "=" << (i) << " " << #j << "=" << (j) << endl << " " << #k << "=" << (k) << endl
using namespace std;

int main() {
    int t;
              
    cin>>t;
    
    for(int kases = 1; kases <= t; kases ++) {
		int n;
		cin >> n;
		vector<int> candies(n);
		for(int i = 0; i < n; i++) {
			cin >> candies[i];
		}
		int ans = -1;
		for(int i = 1; i < (1<<n)-1; i++) {
			int sum = 0;
			int exor_sean = 0, exor_pat = 0;
			for(int j = 0 ; j < n; j++) {
				if(i & (1 << j)) {
					sum += candies[j];
					exor_sean ^= candies[j];
				}
				else {
					exor_pat ^= candies[j];
				}
			}
			if(exor_sean == exor_pat) {
				ans = max(ans, sum);
			}
		}
    	cout << "Case #" << kases << ": ";
		if(ans == -1) {
    		cout << "NO" << endl;
    	} else {
    		cout << ans << endl;
    	}
    	
    }
	 
    return 0;
}







