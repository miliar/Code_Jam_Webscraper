#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;

char pat[] = "welcome to code jam";
char line[512];

int mod = 10000;
int dp[20];

int main() {

	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out", "w", stdout);

	typedef multimap<char, int>::iterator ITR;
	typedef pair<ITR, ITR> ITR2;
	multimap<char, int> mmap;
	for (int i=0; i<sizeof(pat); ++i) {
		mmap.insert(make_pair(pat[i], i) );
	}

	int T;
	scanf("%d", &T);
	gets(line);
	for (int tid=1; tid<=T; ++tid) {
		gets(line);
		memset(dp, 0, sizeof dp);
		dp[0] = 1;
		for (int cur=0; line[cur]; ++cur) {
			char ch = line[cur];
			if (mmap.count(ch) ) {
				ITR2 itr2 = mmap.equal_range(ch);
				for (ITR it=itr2.first; it != itr2.second; ++it) {
					int proc = it->second;
					dp[proc+1] += dp[proc];
					if (dp[proc+1] >= mod)
						dp[proc+1] -= mod;
				}
			}
		}
		printf("Case #%d: %04d\n", tid, dp[19]);
	}
	return 0;
}