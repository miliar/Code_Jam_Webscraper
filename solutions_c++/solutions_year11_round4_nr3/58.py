#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int64,int64> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

const int maxn = 1<<25;
int mn,mx;
char isp[maxn];

vector<int64> primes;
int64 getmin(int n){
    if (n==1)return 1;
    int res = 0;
    for (int i = 0; i < primes.size() && primes[i]<=n; i++)
        res++;
    return res;
}

int64 getmin_dfs(int64 n, int k, int cur, int64 mm,int cnt){
    int64 res = n/mm;
    if (cnt&1){
        res = -res;
    }
    for (int i = cur; i < k; i++){
        int64 qq = mm*primes[i];
        if (qq>n)break;
        res += getmin_dfs(n,k,i+1,qq,cnt+1);
    }
    return res;
}

int64 phi(int64 n, int k){
    return getmin_dfs(n,k,0,1,0);
}

int64 getmin_sq(int64 n){
    if (n<1000) return getmin(n);
    int k = 0;
    for (;primes[k]*primes[k]<=n;k++);
    return k-1;
}

int64 getmax(int n){
    int res = 1;
    for (int i = 0; primes[i]<=n;i++){
        int64 z = primes[i];
        for (;z<=n;z*=primes[i],res++);
    }
    return res;
}

int64 getmax_sq(int64 n){
    if (n<1000) return getmax(n);
    int64 res = 0;
    int k = 0;
    for (;primes[k]*primes[k]<=n;k++){
        int64 z = primes[k];
        for (;z<=n;z*=primes[k],res++);
    }
    return res;
}

int main(){
    memset(isp,1,sizeof(isp));
    isp[0]=isp[1]=0;
    for (int i = 2; i*i<maxn; i++){
        if (isp[i])
            for (int j = i*i; j < maxn; j+=i)isp[j]=0;
    }
    for (int i =2; i < maxn; i++) if (isp[i]) primes.push_back(i);
    int T; cin >> T;
    for (int _ = 0; _ < T; _++){
        int64 n; cin >> n;
        printf("Case #%d: %lld\n",_+1,(getmax_sq(n)-getmin_sq(n)));
    }
	return 0;
}

