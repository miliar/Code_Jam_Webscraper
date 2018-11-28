#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;


//#define SMALL
#define LARGE
void shiftRight(int &n)
{
	int cnt = 1;
	int right = n % 10;
	while(!right)
	{
		n /= 10;
		cnt *= 10;
		right = n%10;
	}
	n /= 10;
	int ret = n;

	while(n)
	{
		cnt *= 10;
		n /= 10;
	}
	n = ret + cnt*right;

}
int main() {
	freopen("C.in", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif
	int A,B,t,T,cnt;
	cin >> T;
//	bool vis[2000001];

	for(int t = 1 ; t <= T ; t++ ) {
//		memset(vis, 0, sizeof vis);
		cin >> A >> B;
		cnt = 0;
		for (int i = A; i <= B; ++i) {
//			if(!vis[i])
//			{
//				vis[i] = 1;
				int tmp = i;

				do{
					shiftRight(tmp);

					if(tmp <= i || tmp < A || tmp > B)
						continue;
//					vis[tmp] = 1;
					cnt++;
//					cout << tmp <<endl;
				}while(tmp != i);
			}
//		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}
