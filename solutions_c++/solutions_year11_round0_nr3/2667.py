#include <iostream>
#include <iomanip> 
#include <string> 
#include <algorithm> 
#include <vector> 
#include <set> 
#include <map> 
#include <math.h> 
#include <cstdlib>
#include <queue>
using namespace std;

int main(void) {
	freopen("/Users/admin/Desktop/[Contests]/informatics/Cpl/be/a.in","r",stdin);
	freopen("/Users/admin/Desktop/[Contests]/informatics/Cpl/be/a.out","w",stdout);
	int n, t, f;
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		scanf("%d", &t);
		long long sum = 0;
		int min = 100000000, ans = 0;
		for (int j = 0; j < t; j++) {
			scanf("%d", &f);
			sum += f;
			if (f < min) {
				min = f;
			}
			ans ^= f;
		}
		if (ans != 0) {
			cout << "Case #"<< i + 1<< ": NO" << endl;
		} else {
			cout << "Case #"<< i + 1<< ": " << (sum - min) << endl;
		}
	}
	return 0;
}