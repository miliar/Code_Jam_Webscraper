#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		string s;
		cin >> s;
		if (!next_permutation(s.begin(),s.end())) {
			sort(s.begin(),s.end());
			int minv = 10, idx = -1;
			for (int i=0;i<s.length();++i) {
				if (s[i]!='0' && s[i]-'0' < minv) {
					minv = s[i]-'0';
					idx = i;
				}
			}
			assert(idx!=-1);
			s.erase(s.begin()+idx);
			s = string(1,minv+'0') + "0" + s;
		}
		else {

		}
		printf("Case #%d: %s\n", z, s.c_str());
	}
}
