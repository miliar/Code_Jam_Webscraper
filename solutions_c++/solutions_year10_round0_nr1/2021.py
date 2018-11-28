#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)

int main() {
    freopen("A.in", "rt", stdin);
    freopen("A.out", "wt", stdout);
	int t = 0, T, N;
	long long K;
	cin>>T;
	while (t++ < T) {
		cin>>N>>K;
		long long n = (1<<N) - 1;
		if (K < n)
			printf("Case #%d: OFF\n", t);
		else if(K == n)
				printf("Case #%d: ON\n", t);
		else {
			K-=n;
			n++;
			if ((K%n) == 0)
				printf("Case #%d: ON\n", t);
			else
				printf("Case #%d: OFF\n", t);
		}
	}
	//  system("pause");
	return 0;
}
