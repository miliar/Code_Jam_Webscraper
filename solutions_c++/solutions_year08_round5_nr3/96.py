#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <fstream>
using namespace std;
static const double EPS = 1e-8;
typedef long long ll;

int createMask(int base, int width)
{
	int mask = 0;
	for (int i = 0; i < width; ++i){
		if (!(base & (1 << i))){
			continue;
		}

		if (i){
			mask |= (1 << (i - 1));
		}
		if (width - 1 != i){
			mask |= (1 << (i + 1));
		}
	}

	return mask;
}

int countBits(int x)
{
	int result = 0;
	for (int i = 0; i < 16; ++i){
		if (x & (1 << i)){
			++result;
		}
	}
	return result;
}

int main() {
	//ifstream cin("c.in.txt");

	int C;
	cin >> C;

	for (int testCase = 1; testCase <= C; ++testCase){
		int height, width;
		cin >> height >> width;
		cin.ignore();

		int table[16];
		for (int y = 0; y < height; ++y){
			int value = 0;
			for (int x = 0; x < width; ++x){
				char c;
				cin >> c;
				if (c == 'x'){
					value |= (1 << x);
				}
			}
			table[y] = value;
		}

		int prev[1 << 10];
		memset(prev, 0, sizeof(prev));
		for (int y = 0; y < height; ++y){
			int current[1 << 10];
			memset(current, 0, sizeof(current));

			for (int state = 0; state < (1 << width); ++state){
				if (table[y] & state){
					continue;
				}

				if (createMask(state, width) & state){
					continue;
				}

				const int bitCount = countBits(state);
				for (int prevState = 0; prevState < (1 << width); ++prevState){
					if (createMask(prevState, width) & prevState){
						continue;
					}

					if (createMask(prevState, width) & state){
						continue;
					}

					current[state] = max(current[state], prev[prevState] + bitCount);
				}
			}

			memcpy(prev, current, sizeof(prev));
		}

		const int answer = *max_element(prev, prev + (1 << width ));
		printf("Case #%d: %d\n", testCase, answer);
	}
}
