/*
 this code was written by Zanaty
 problem kind:
 */
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<set> 
#include<cmath>
#include<fstream>
#include<memory.h>
#include<map>
#include<sstream>
#define OO 10e8
using namespace std;
int s1, s2;
string itos(int x) {
	string s;
	while (x > 0) {
		s += (int) (x % 10) + '0';
		x /= 10;
	}
	reverse(s.begin(), s.end());
	return s;

}
pair<bool, string> check(string s, int idx) {

	string temp = s.substr(idx, s.length());
	temp += s.substr(0, idx);

	if (atoi(temp.c_str()) <= atoi(s.c_str()) || atoi(temp.c_str()) > s2
			|| atoi(temp.c_str()) < s1)
		return make_pair(false, temp);

	return make_pair(true, temp);
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("C-large.in", "rt", stdin);
	freopen("res2.txt", "wt", stdout);
#endif
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++) {

		cin >> s1 >> s2;
		int res = 0;
		for (int i = s1; i <= s2; i++) {

			string temp = itos(i), temp2;
			vector<string> v;
			bool flag = 0;
			for (int sz = 1; sz < temp.length(); sz++) {

				if (temp[sz] >= temp[0] && temp[sz] != '0') {
					pair<bool, string> p = check(temp, sz);
					if (p.first) {
						flag=0;
						//cout << temp << "  " << p.second << endl;

						for (int kk = 0; kk < v.size(); kk++) {
							if (v[kk] == p.second)
								flag = 1;
						}
						v.push_back(p.second);
						if (!flag)
							res++;
					}
				}
			}
		}
		printf("Case #%d: %d\n", tt, res);

	}

	return 0;
}
