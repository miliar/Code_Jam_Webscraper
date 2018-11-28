#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <sstream>
using namespace std;

typedef unsigned long long ULL;
typedef long long LL;

#define REP(i,n)      FOR(i,0,n)
#define FOR(i,a,b)    for(int i = a; i < b; i++)
#define ROF(i,a,b)    for(int i=a;i>b;i--)
#define min(a,b)      (a<b?a:b)
#define max(a,b)      (a>b?a:b)
#define GI 		      ({int t;scanf("%d",&t);t;})
#define GL 		      ({LL t;scanf("%lld",&t);t;})
#define GD 		      ({double t;scanf("%lf",&t);t;})
#define pb 	          push_back
#define fii 	      freopen("input.txt","r",stdin)
#define fio 	      freopen("output.txt","w",stdout)
#define MOD 	      1000000007
#define INF	          (int)1e9
#define EPS	          1e-9
#define TR(a,it)      for (typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

int digits[2000005], tens[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
void PreComputeDigits()
{
    digits[0] = 0;
    for (int i=1; i<=2000000; i++)
        digits[i] = digits[i/10] + 1;
}

int NextNum(int i, int iCopy, int iTens)
{
    if (digits[i] != digits[iCopy])
        iCopy = iCopy * 10;
    else {
        int firstDigit = iCopy/iTens;
        iCopy = (iCopy % iTens) * 10 + firstDigit;
    }
    return iCopy;
}

int main()
{
	fii; fio;

	PreComputeDigits();
	int T, t = 0, a, b;
	scanf("%d", &T);
	while (T--) {
	    map<pair<int, int>, bool> mp;
		scanf("%d %d", &a, &b);
		for (int i=a; i<=b; i++) {

            int iDigits = digits[i], iTens = tens[iDigits - 1], iCopy = i, firstDigit;
            for (int j=0; j<iDigits-1; j++) {

                iCopy = NextNum(i, iCopy, iTens);
                if (iCopy >= a && iCopy <= b  && digits[i] == digits[iCopy] && iCopy > i) {
                    mp[make_pair(i, iCopy)] = true;
                }
            }
		}

		printf("Case #%d: %d\n", ++t, (int)mp.size());
	}

	fprintf(stderr, "Time execute: %.3lf\n", clock() / (double)CLOCKS_PER_SEC);
	return 0;
}
