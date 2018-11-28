#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define EPS 1e-8

int T;

struct item{
	int b, e, w;
	bool operator<(const item &sec) const {
		return w < sec.w; 
	}
} arr[1005];

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> T;
	for (int I=0; I<T; I++){
		cout << "Case #" << I+1 << ": ";
		int x, s, r, n, tw;
		double t;
		cin >> x >> s >> r >> t >> n;
		tw = x;
		for (int i=0; i<n; i++){
			cin >> arr[i].b >> arr[i].e >> arr[i].w;
			tw -= arr[i].e - arr[i].b;
			arr[i].e -= arr[i].b;
		}
		arr[n].w = 0;
		arr[n].b = 0;
		arr[n].e = tw;
		n++;
		sort(arr, arr+n);
		double ret = 0;
		for (int i=0; i<n; i++){
			if (t < EPS){
				ret += (double)(arr[i].e)/(arr[i].w + s);
			} else {
				if ((double)arr[i].e / (arr[i].w + r) < t){
					ret += (double)arr[i].e / (arr[i].w + r);
					t -= (double)arr[i].e / (arr[i].w + r);
				} else {
					ret += t;
					ret += (arr[i].e - t*(arr[i].w + r))/(arr[i].w + s);
					t = 0;
				}
			}
		}
		cout << fixed << setprecision(8) << ret <<endl;
	}
	return 0;
}