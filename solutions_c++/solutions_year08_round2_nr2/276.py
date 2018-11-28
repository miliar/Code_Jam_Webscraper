#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <string.h>
#include <algorithm>


using namespace std;

#define maxn 1100000

int maxp[maxn];
int father[maxn];

long long gcd(long long a, long long b){
	if (a == 0) return b;
	if (b == 0) return a;
	return gcd(b % a, a);
}	


int who(int a){
	int res = a;
	while (father[res] != res) res = father[res];
	int i = a;
	while (i != res){
		int tmp = father[i];
		father[i] = res;
		i = tmp;
	}
	return res;
}
void merge(int a, int b){
	if (rand() % 2) father[a] = b; else father[b] = a;
}	

int main(){

	int i;
	memset(maxp, 0, sizeof(maxp));
	maxp[1] = 1;
	for (i = 2; i < maxn; i++) if (maxp[i] == 0){
		maxp[i] = i;
//		cerr << i << endl;
		int j;
		for (j = i; j < maxn; j += i) if (i > maxp[j]) maxp[j] = i;
	}
	int ferlon;
	cin >> ferlon;
	for (int _ = 0; _ < ferlon; _++){
		long long a, b, p;
		cin >> a >> b >> p;
		int n = b - a + 1;
		int i, j;
		for (i = 0; i < n; i++) father[i] = i;
		for (i = 0; i < n; i++)
			for (j = i + 1; j < n; j++) if (who(i) != who(j) && maxp[gcd(a + i, a + j)] >= p) merge(who(i), who(j));
			
		long long ans = 0;
		for (i = 0; i < n; i++) if (father[i] == i) ++ans;
		cout << "Case #" << _ + 1 << ": " << ans << endl;						
	}
	return 0;
}	
