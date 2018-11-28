#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>

using namespace std;
int cn;
int num[150];
int N,L,H,R;

int main() {
	int cases;
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d%d%d",&N,&L,&H);
		for (int i=0; i < N; ++i) {
			scanf("%d",&num[i]);
		}
		bool ok = false;
		bool pode;
		
		for (int i=L; i <= H; ++i) {
			pode=true;
			for (int j=0; j < N; ++j) {
				if ( num[j]%i == 0 || i%num[j] == 0 ) continue;
				pode=false;
				break;
			}
			if (pode) {
				ok=true;
				R=i;
				break;
			}
		}
		
		end:
		printf("Case #%d: ",++cn);
		if (pode) printf("%d",R);
		else printf("NO");
		printf("\n");
	}


	return 0;
}
