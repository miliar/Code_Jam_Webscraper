#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
 
using namespace std;
 
typedef long long int lint;
typedef pair<lint,lint> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)

int main() {
	int T;
	cin >> T;
	rep(i,T) {
		int K,n;
		int ind[101];
		int disp[6001]={};
		cin >> K;
		cin >> n;
		rep(j,n)
			cin >> ind[j];
		int start=1;
		disp[1]=1;
		Rep(j,2,K+1) {
			int count=0;
			while (count!=j) {
				start++;
				if (start==K+1)
					start=1;
				if (disp[start])
					continue;
				count++;
			}
			disp[start]=j;
		}
		//Rep(j,1,K+1) cout << disp[j] << endl;
		cout << "Case #" << i+1 << ":";
		rep(j,n)
			cout << " " << disp[ind[j]];
		cout << endl;
	}
	return 0;
}

