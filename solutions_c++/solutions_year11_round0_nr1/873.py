#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	cin >> t;
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ": ";
		int n;
		cin >> n;
		int p1 = 1, p2 = 1, c1 = 0, c2 = 0, ret = 0;
		for (int i=0; i<n; i++){
			char c;
			cin >> c;
			int pos;
			cin >> pos;
			if (c == 'O'){
				c2++;
				ret++;
				if (c1 > abs(p1 - pos)){
					c1 = 0;
				} else {
					c2 += abs(p1 - pos) - c1;
					ret += abs(p1 - pos) - c1;
					c1 = 0;
				}
				p1 = pos;
			} else {
				c1++;
				ret++;
				if (c2 > abs(p2 - pos)){
					c2 = 0;
				} else {
					c1 += abs(p2 - pos) - c2;
					ret += abs(p2 - pos) - c2;
					c2 = 0;
				}
				p2 = pos;
			}
		}
		cout << ret << endl;
	}
	return 0;
}