#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
#include <list>
#include <set>
#include <algorithm>
#include <string>
#include <sstream>
#include <functional>
#include <numeric>
#include <iterator>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i+1);
		string s;
		cin >> s;
		int l = s.size();
		int j = l-1;
		while (j > 0 && s[j] <= s[j-1]) {
			--j;
		}
		if (j == 0) { // add 0
			char minc = '9' + 2;
			int pos = -1;
			for (int k = 0; k < l; ++k) {
				if (s[k] != '0' && s[k] < minc) {
					minc = s[k];
					pos = k;
				}
			}
			s[pos] = s[0];
			s[0] = minc;
			s += '0';
			sort(s.begin() + 1, s.end());			
		}
		else { // rearrange
			int c = s[j-1];
			int diff = 10;
			int pos = -1;
			for (int k = j; k < l; ++k) {
				if ((s[k] > c) && (s[k] - c < diff)) {
					diff = s[k] - c;
					pos = k;
				}
			}
			assert(pos != -1);
			s[j-1] = s[pos];
			s[pos] = c;
			sort(s.begin() + j, s.end());
		}
		printf("%s\n", s.c_str());
		
	}
	
	return 0;
}
