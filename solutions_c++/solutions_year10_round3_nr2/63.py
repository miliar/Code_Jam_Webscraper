#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
#define	out(x) 		(cout << #x << ": " << x << endl)
#define	MM(m,what)	(memset(m, what, sizeof(m)))
template<class T>void show(T a, int l){for(int i = 0; i < l; ++i)cout << a[i] << ' '; cout << endl;}
template<class T>void show(T a, int l, int r){for(int i = 0; i < l; ++i)show(a[i], r); cout << endl;}

int main(){
		freopen("B-large.in", "r", stdin);	freopen("B-large.txt", "w", stdout);
	int T;
	long long L, P, C;
	scanf("%d", &T);
    for(int ks = 1; ks <= T; ++ks){
        scanf("%I64d%I64d%I64d",&L,&P,&C);
        int t=0;
        while(L < P){
            t++;
            L *= C;
        }
        int sum = 0;
        if(t > 0)
            sum = ceil(log((double)t)/log(2.0));
        printf("Case #%d: %d\n", ks, sum);
    }
}
