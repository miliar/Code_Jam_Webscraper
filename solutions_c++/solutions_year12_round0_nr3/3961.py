#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include <sstream>
#include <utility>
#define FOR(i, a, b) for(int i = a; i < b; ++i)

using namespace std;

int tam(int n) {
	return (1+ floor(log10(double(n))));
}

map<pair<int, int>, bool> vec;
bool matriz[1001][1001];

int main() {
	int t, a, b, num, res;
	string s1, s2;
	scanf("%d", &t);
	FOR(i, 0, t) {
//		memset(matriz, false, sizeof matriz);
		vec.clear();

		res = 0;
		scanf("%d %d", &a, &b);
		FOR(j, a, b+1) {
			stringstream ss;
			ss << j;
			s1 = ss.str();
			if(s1.size() > 1) {
				FOR(k, 0, s1.size()-1) {
					s1 += s1[0];
					s1.erase(0, 1);

					stringstream sa(s1);
					sa >> num;
					if((tam(j) == tam(num)) && num > j && num <= b && !vec[make_pair(num, j)]) {
						res++;
						vec[make_pair(j, num)] = vec[make_pair(num, j)] = true;
						//matriz[j][num] = matriz[num][j] = true;
					}
				}
			}
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
}
