#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int inf=(1<<30);
#define mset(a,x) memset(a,x,sizeof(a))
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define dbg(x) cerr<<#x<<" : "<<x<<endl

bool flag[105];
int q;
int n;
int a[105];
int main() 
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T,cnt=0;
	scanf("%d", &T);
	while (T--) {
	       cin >> q >> n;
		   mset(flag, 0);
		   vector<int> vec;
		   for (int i = 0; i < n; i++) {
		        scanf("%d", &a[i]);
				a[i]--;
                vec.push_back(i);
		   }
		   int res = inf;
		   do {
			    int cost = 0;
				mset(flag, 0);
                for (int i = 0; i < n; i++) {
				     flag[a[vec[i]]] = 1;
                     for (int j = a[vec[i]]-1; j >= 0; j--) {
					      if (!flag[j]) {
						      cost++;
						  }
						  else break;
					 }
					 for (int j = a[vec[i]]+1; j < q; j++) {
					      if (!flag[j]) {
						      cost++;
						  }
						  else break;
					 }
					 
				}
				//puts("");
				if (cost < res) res = cost;
		   }while (next_permutation(vec.begin(), vec.end()));
		   printf("Case #%d: ", ++cnt);
		   cout << res << endl;
	}
    return 0;
}
