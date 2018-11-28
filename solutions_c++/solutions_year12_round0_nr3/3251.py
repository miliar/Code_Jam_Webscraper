#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <sstream>
using namespace std;

int permute(int l, string str) {
	string s1 = str.substr(0,l);
	string s2 = str.substr(l);
	stringstream ss;
	ss << s2 << s1;
	string result = ss.str();
	stringstream convert(result);
	int res;
	convert >> res;
	return res;
}
bool check(int num, int A, int B) {
	return (num >= A && num <= B);
}

int main () {

freopen("As.in", "r", stdin); //for small input
freopen("As.out", "w", stdout);

//freopen("Al.in, "r", stdin); //for large input
//freopen("Al.out, "r", stdout);

int T;
cin >> T;

long long A, B;

for (int t = 1; t <= T; ++t) {
	cin >> A >> B;
	int rB[9000]; memset(rB, 0, sizeof(rB));
	stringstream qq; qq << B;
	string tmp2 = qq.str();
	int cnt = 0;
	multimap<int, int> recycled;
	if (A == B || ( B < 20)) {
		cout << "Case #" << t << ": " << cnt << endl;
		continue;
	}
	int num = A;
		while(num < B) {
			stringstream gg;
			gg << num;
			string tmp = gg.str();
			for (int i = tmp.length() - 1; i > 0; -- i) {
				if (tmp.at(i) < tmp.at(0)) continue;
				if (tmp.at(i) > tmp2.at(0)) continue;
				int res = permute(i, tmp);
				if (res <= num) continue;
				if (check(res, A, B)) {
					rB[cnt] = res;
					recycled.insert(pair<int,int>(res,num));
					++cnt;
				}
			}
			++num;
		}

vector<int> myv (rB, rB + recycled.size());
vector<int>::iterator bp;
bp = unique (myv.begin(), myv.end());
myv.resize (bp - myv.begin());	

cout << "Case #" << t << ": " << myv.size()  << endl;
}


return 0;
}
