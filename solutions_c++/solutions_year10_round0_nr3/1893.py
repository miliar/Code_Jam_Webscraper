#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define FR(i, n) for (int i=0; i<n; i++)
#define SZ(a) ((int)a.size())
#define MOD 1000000000 

typedef pair<int, int> II;
typedef vector<II> VII;
typedef long long LL;

int ntest;
int R, k, n;
LL ret;
int a[1111], next[1111];
LL f[1111];

void process() {
     ret = 0;
     // n^2 + R
     for (int i=0; i<n; i++) {
         f[i] = 0;
         int j = i;
         while (true) {           
           if (f[i] + a[j] > k) break;
           f[i] += a[j];
           
           j = (j+1) % n;
           next[i] = j;  
           if (j==i) break;         
         }
         
         
     }
     
     int st = 0;
     FR(i, R) {
       ret += f[st];
       st = next[st];
     }
}

int main() {
	//freopen("C-small-attempt1.in", "rt", stdin);
	freopen("C-large.in", "rt", stdin);
    //freopen("c.in", "rt", stdin);
	freopen("c2.out", "wt", stdout);
	
	// 50 tests
	//R = so lan chay
    //k = tong so nguoi tren xe
    //n = so group
	scanf("%d", &ntest);
	
	FR(test, ntest) {             
      scanf("%d%d%d", &R, &k, &n);
      //cout << R << " " <<k << " " << n << endl;
      FR(i, n) scanf("%d", &a[i]);
      process();
      cout << "Case #" << test+1 << ": " << ret << endl;
    }

	return 0;
}
