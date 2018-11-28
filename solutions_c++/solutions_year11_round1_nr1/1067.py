#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

typedef long long LL;
#define FOR(i,a,b) for(LL i = (a); i <= (b); i++)

void runCase()
{
    LL n,pd,pg;
    scanf("%I64d%I64d%I64d",&n,&pd,&pg);

    bool res = false;
    for(LL i = 1; i <= n; i++) {
        if(n>100){
            res = true;
            break;
        }
        if(i*pd%100==0) {
            res = true;
        }
    }

    if(pd < 100 && pg == 100) res = false;
    if(pd > 0 && pg == 0) res = false;

    if(res) cout << "Possible" << endl;
    else cout << "Broken" << endl;
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();

	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
	}
}

int main()
{
	solve();
	return 0;
}
