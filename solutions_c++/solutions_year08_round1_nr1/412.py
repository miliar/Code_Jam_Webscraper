#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <ctime>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;
 
#define GI ({int t;scanf("%d",&t);t;})
#define dbg(x) cout << #x << " -> " << x << "\t" << flush;
#define dbge(x) cout << #x << " -> " << x << "\t" << endl;
#define LET(x,a) typeof(a) x(a)
#define FORI(i,a,b) for(LET(i,a);i!=(b);++i)
#define FOR(i,a,b) for(LET(i,a);i < (b);++i)
#define FORZ(i,n) FOR(i,0,n)
#define EACH(i,v) FOR(i,(v).begin(),(v).end())
#define CS c_str()
#define PB push_back
#define SZ size()
#define INF (int)1e9+1

int main()
{
    int nC = GI;
    for(int nc = 1; nc <= nC; ++nc)
    {
	int n = GI;
	long long arr1[n], arr2[n];
	FORZ(i,n)
	    cin >> arr1[i];
	FORZ(i,n)
	    cin >> arr2[i];
	sort(arr1, arr1+n);
	sort(arr2, arr2+n);
	long long ret = 0;
	FORZ(i,n)
	    ret += arr1[i]*arr2[n - i - 1];
	printf("Case #%d: %lld\n",nc, ret);
    }
}
