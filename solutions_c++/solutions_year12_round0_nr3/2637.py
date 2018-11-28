/*
 * Google Code Jam 2010. Round 1 - sub-round C
 * (C)Copyright jclin (j i a n c h e n g [at] g_m_a_i_l [dot] c_o_m)
 */
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <ext/hash_map>
#include <list>

using namespace std;
using namespace __gnu_cxx;

struct pair2 {
	int a, b;
};
struct my_hash_ll {
	        size_t operator() (const pair2 &key) const {
				return key.a;
			}
};
struct my_cmp_ll {
	        bool operator() (const pair2 &l, const pair2 &r) const {
				return l.a == r.a && l.b == r.b;
			}
};

int atoi2(char * str, int idx, int end, int len) {
	int num = 0;
	int i;

	for (i=idx; i <end; i++) {
		num = num * 10 + str[i] - '0';
	}
	for (i=0; i <idx; i++) {
		num = num * 10 + str[i] - '0';
	}
	for (i=end; i<len; i++) {
		num = num * 10 + str[i] - '0';
	}

	return num;
}

int go(int min, int max)
{
	hash_map<int, int> used;
	char buf [100];
	int count = 0;
	int i;
	hash_map<pair2, char, my_hash_ll, my_cmp_ll> result;
	for (i = min; i <= max; ++i) {
		int len = sprintf(buf, "%d", i);
		if (len <= 1)
			continue;
		bool same = true;
		for (int j = 0; j < len; j++) {
			if (buf[j] != buf[0])
			{
				same=false;
				break;
			}
		}
		if (same) continue;

		bool legal = true;
		list<int> backup;
		hash_map<int, int> see;

		int pair = 0;
		for (int k = len-1; k > 0; k--) {
			for (int j = len; j <= len; j++) {
				if (buf[k] == '0')
					continue;
				int no = atoi2(buf, k, j, len);
				if (no > i && no >= min && no <= max) {
					pair2 tmp = {i, no};
					result[tmp] = 1;
				}
			}
		}
	}
	/*
	hash_map<pair2, char, my_hash_ll, my_cmp_ll>::iterator it;
	for (it = result.begin(); it != result.end(); it++ ) {
		const pair2 &p = (*it).first;
		cout << p.a << "->" << p.b << endl;
	}
	*/
	return result.size();
}

int main(int ac, char**av)
{
	int T, min, max;

	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> min >> max;
		cout << "Case #" << i+1 << ": " << go(min, max) << endl;
	}
	return 0;
}

