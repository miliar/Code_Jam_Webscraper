#define _CRT_SECURE_NO_WARNINGS 1
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <string>
#include <bitset>
#include <math.h>
#include <limits.h>
#include <float.h>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <assert.h>
#include <sstream>
#include <limits>
#include <list>
#include <stdlib.h>
using namespace std;
typedef unsigned long long ULL;
typedef signed long long SLL;
typedef unsigned short ushort;
typedef signed char schar;
typedef unsigned char uchar;

#define max_macro(a,b)    (((a) > (b)) ? (a) : (b))
#define min_macro(a,b)    (((a) < (b)) ? (a) : (b))
#define MOD 10007
typedef pair<unsigned, unsigned> NumPair;
typedef map<NumPair, unsigned> MovesMap;
typedef set<NumPair> BadPosSet;
typedef deque<NumPair> NextMoveQ;
MovesMap M;
BadPosSet BP;
NextMoveQ NMQ;

void add_move(const NumPair& q, unsigned mmp) {
	MovesMap::iterator j = M.find(q);
	if(j == M.end()) {
		M[q] = mmp;
		NMQ.push_back(q);
	} else {
		(*j).second += mmp;
		(*j).second %= MOD;
	}
}

int main(void) {
	unsigned num_tests;
	scanf(" %u", &num_tests);
	for(unsigned test_it = 1; test_it <= num_tests; ++test_it) {
		M.clear();
		BP.clear();
		NMQ.clear();
		unsigned h, w, r;
		scanf(" %u %u %u", &h, &w, &r);
		for(unsigned j = 0; j < r; ++j) {
			unsigned z1, z2;
			scanf(" %u %u", &z1, &z2);
			BP.insert(NumPair(z1 - 1, z2 - 1));
		}
		M[NumPair(0, 0)] = 1;
		NMQ.push_back(NumPair(0, 0));
		while(! NMQ.empty()) {
			NumPair& p = NMQ.front();
			unsigned mmp = M[p];
			if(p.first + 1 < h && p.second + 2 < w) {
				NumPair q(p.first + 1, p.second + 2);
				if(BP.find(q) == BP.end()) {
					add_move(q, mmp);
				}
			}
			if(p.first + 2 < h && p.second + 1 < w) {
				NumPair q(p.first + 2, p.second + 1);
				if(BP.find(q) == BP.end()) {
					add_move(q, mmp);
				}
			}
			// M.erase(p);
			NMQ.pop_front();
		}
		MovesMap::iterator jj = M.find(NumPair(h-1, w-1));
		unsigned res = jj != M.end() ? (*jj).second : 0;
		printf("Case #%d: %d\n", test_it, res);
	}
	return 0;
}
