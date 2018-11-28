#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(v) (int(v.size()))

#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

int d[50];

int main() {
	int n, nTest;
	scanf("%d",&nTest);
	for (int curTest = 1; curTest<=nTest; curTest++) {
		scanf("%d\n",&n);
		for (int i=1; i<=n; i++) {
			d[i] = 0;
			for (int j=1; j<=n; j++)
				if (getchar() == '1') d[i] = j;
			getchar();
//			cerr << d[i] << " ";
		}

		int res = 0;
		for (int i=1; i<=n; i++) {
			for (int j=i; j<=n; j++) if (d[j]<=i) {
				for (int k=j-1; k>=i; k--) {
					res++; swap(d[k],d[k+1]);
				}
				break;
			}
		}
		printf("Case #%d: %d\n",curTest,res);
	}
	
}
