#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
 
typedef long long LL;
typedef vector<int> vi;
typedef vector< pair<int, int> > vii;
#define MP(x,y) make_pair(x, y)

int p[1000005], np=0;
int a[1000005];
vector< pair<long long, int> > csn;
int ans[100005];
int main(void) {
    int T, cs, i, j, k;
	for(i=2;i<=1000;i++)
		if(!a[i]){
			p[np++] = i;
			for(j=i*i;j<=1000000;j+=i)
				a[j]=1;
		}
	for(;i<=1000000;i++)
		if(!a[i])
			p[np++] = i;
	fprintf(stderr, "np=%d\n", np);
    scanf("%d", &T);
	LL n;
    for(cs=1;cs<=T;cs++) {
		scanf("%lld", &n);
		csn.push_back(MP(n, cs));
	}
	sort(csn.begin(), csn.end());
	for(i=0;i<csn.size();i++)
		if(csn[i].first == 1)
			--ans[csn[i].second];
	for(j=0;j<np;j++) {
		long long prime = (long long) p[j], QQ = 1LL;
		int pc = 0;
		for(i=0;i<csn.size();i++) {
			while(QQ <= csn[i].first) {
				pc++, QQ *= prime;
			}
			if(pc>=2)
			ans[csn[i].second] += pc-2;
		}
	}

	for(cs=1;cs<=T;cs++) {
        printf("Case #%d: %d\n", cs, ans[cs] + 1);
    }
    return 0;
}

