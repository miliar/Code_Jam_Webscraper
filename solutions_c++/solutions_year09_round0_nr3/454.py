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

const int LEN = 19;
char phrase[LEN+1] = "welcome to code jam";
int cnt[LEN+1];

int main()
{
	int N;
	char buf[512];
	fgets(buf, 512, stdin);
	sscanf(buf, "%d", &N);
	for (int TC = 1; TC <= N; ++TC) {
		fgets(buf, 512, stdin);
		memset(cnt, 0, sizeof cnt);
		int line_len = strlen(buf);
		for (int i = 0; i < line_len; ++i) {
			for (int j = LEN-1; j >= 1; --j) {
				if (buf[i] == phrase[j]) {
					cnt[j] += cnt[j-1];
					cnt[j] %= 10000;
				}
			}
			if (buf[i] == phrase[0]) {
				cnt[0] += 1;
				cnt[0] %= 10000;
			}
		}
		printf("Case #%d: %04d\n", TC, cnt[LEN-1]);
	}
	return 0;
}
