#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;
#define	out(x)	(cout << #x << ": " << x << endl)
template<class T>void show(T a, int l){for(int i = 0; i < l; ++i)cout << a[i] << ' '; cout << endl;}
template<class T>void show(T a, int l, int r){for(int i = 0; i < l; ++i)show(a[i], r); cout << endl;}
int bin[31];

int main(){
	freopen("A-large.in", "r" , stdin);	freopen("out.txt", "w", stdout);
	int T, n, k;
	scanf("%d", &T);
	for(int i = bin[0] = 1; i < 31; ++i)
		bin[i] = bin[i-1]*2;
	for(int ks = 1; ks <= T; ++ks){
		scanf("%d%d", &n, &k);
		k = k%bin[n];
		if(k == bin[n]-1)	printf("Case #%d: ON\n", ks);
		else	printf("Case #%d: OFF\n", ks); 
	}
	return 0;
}
