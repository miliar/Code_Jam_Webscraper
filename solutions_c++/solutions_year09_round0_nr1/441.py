#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
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
#include <utility> 
#include <valarray>
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int L, D, N;
set<string> words;

vector<char> groups[32];

int getcnt(string prefix, int len)
{
	if (len == L) {
		if (words.find(prefix) != words.end())
			return 1;
		return 0;
	}

	set<string>::iterator it = words.lower_bound(prefix);
	if (it == words.end() || prefix != it->substr(0, len))
		return 0;

	int cnt = 0;
	for (int i = 0; i < SZ(groups[len]); ++i) {
		cnt += getcnt(prefix + groups[len][i], len+1);
	}
	return cnt;
}

int main()
{
	scanf("%d %d %d", &L, &D, &N);
	for (int i = 0; i < D; ++i) {
		char word[32];
		scanf("%s", word);
		words.insert(word);
	}

	for (int TC = 1; TC <= N; ++TC) {
		fprintf(stderr, "%d\n", TC);
		char word[1024];
		scanf("%s", word);
		int p = 0;
		for (int i = 0; i < L; ++i) {
			groups[i].clear();
			if (word[p] != '(') {
				groups[i].push_back(word[p]);
				p += 1;
			} else {
				p += 1;
				while (word[p] != ')') {
					groups[i].push_back(word[p]);
					p += 1;
				}
				p += 1;
			}
		}
		printf("Case #%d: %d\n", TC, getcnt("", 0));
	}
	return 0;
}
