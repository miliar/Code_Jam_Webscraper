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
string s;
int n;
int arr[10];
int permut()
{
    string t = s;
    int f = t.SZ / n;
    FORZ(i,f)
    {
	int val =  n*i;
	for(int j = val, ss = 0; ss < n; ss++, j++)
	{
	    t[j] = s[arr[ss]+val];
	}
    }
    int ret = 1;
    FOR(i,1,t.SZ)
	if(t[i] != t[i - 1])
	    ret++;
    return ret;
}
int main()
{
    int nC = GI;
    FORZ(i,10)
	arr[i] = i;
    for(int nc = 1; nc <= nC; ++nc)
    {
	n = GI;
	cin >> s;
	sort(arr, arr + n);	
	int ret = INT_MAX;
	do
	{
	    int val = permut();
	    ret <?= val;
	}while(next_permutation(arr, arr + n));
	printf("Case #%d: %d\n",nc,ret);
    }
}
