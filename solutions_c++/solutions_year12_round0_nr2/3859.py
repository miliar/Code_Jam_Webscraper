#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <cmath>
#include <bitset>
using namespace std;

#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
typedef vector<int> VI;
typedef pair<int,int> pII;
typedef vector<string> VS;
typedef long long LL;

bool isCorrect (int a, int b, int c, int t) {
	if (a + b + c != t)
		return false;
	if (abs(a - c) > 2 || abs(a - b) > 2 || abs(b - c) > 2)
		return false;
	return true;
}

bool valid (int score, int p, int sur) {
	if (sur == 0) {
		FORZ (a, 11) {
			FORZ (b, 11) {
				FORZ (c, 11) {
					if ( (abs(a - c) < 2 && abs(a - b) < 2 && abs(b - c) < 2) && (a >= p || b >= p || c >= p) ) {
						if (isCorrect(a, b, c, score)) {
							//cout << "Non Sur: " << a << "\t" << b << "\t" << c << "\n";
							return true;
						}
					}
				}
			}
		}
	}
	else {
		FORZ (a, 11) {
			FORZ (b, 11) {
				FORZ (c, 11) {
					if ( (abs(a - c) == 2 || abs(a - b) == 2 || abs(b - c) == 2) && (a >= p || b >= p || c >= p) ) {
						if (isCorrect(a, b, c, score)) {
							//cout << "Sur " << a << "\t" << b << "\t" << c << "\n";
							return true;
						}
					}
				}
			}
		}
	}
	return false;
}

int main () {
	int T;
	cin >> T;
	
	for (int t = 1 ; t <= T ; t ++) {
		int N, S, p;
		cin >> N >> S >> p;
		VI sc(N);
		FORZ (i, N)
			cin >> sc[i];
		
		int ret = 0;
		
		FORZ (i, 1 << N) {
			bitset <32> bit (i);
			if (bit.count() != S)
				continue;
			string s = bit.to_string< char, char_traits<char>, allocator<char> >();
			s = s.substr(s.sz - N);
			//cout << "S = " << s << "\n";
			int val = 0;
			FORZ (j, N) {
				int score = sc[j];
				int sur = (s[j] == '0') ? 0 : 1;
				if (valid(score, p, sur)) {
					val ++;
					//cout << "P# " << j + 1 << "\n";
				}
			}
			ret = max(val, ret);
		}
		cout << "Case #" << t << ": " << ret << "\n";
		//cout << "\n\n";
	}
	
	return 0;
}
