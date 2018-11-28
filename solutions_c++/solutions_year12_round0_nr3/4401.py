#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

#define FOR(A,B) for(A=0;A<B;A++)
using namespace std;

int dig(int x)
{
	int ans = 0;
	while(x > 0) {
		x /= 10;
		ans++;
	}
	return ans;
}
int main(int argc, char *argv[])
{
	int t,T;
	scanf("%d", &T);
	FOR(t, T) {
		vector< pair<int, int> > res;
		int A, B;
		scanf("%d %d", &A, &B);
		int ans = 0;
		for(int x=A; x <= B; x++) {
			int y = x;
			vector<int> poss;
			int digits[10],d=0;
			while(y > 0) {
				digits[d++] = y%10;
				y /= 10;
			}
			for(int k = 0; k < d; k++) {
				int num = 0;
				for(int j = 0; j < d; j++) {
					num = num*10 + digits[(k-j+d)%d];
				}
// < C				printf("%d %d\n", x, num);
				if(num >= A && num <= B && num > x && dig(num) == dig(x)) {
//					poss.push_back(num);
					res.push_back(make_pair(x, num));
				}
			}
		}
		unique(res.begin(), res.end());
		printf("Case #%d: %d\n", t+1, res.size());
	}
	return 0;
}
