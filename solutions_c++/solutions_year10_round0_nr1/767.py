#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;
   
int main(){	
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int k, n, m;
	
	scanf("%d", &k);
	
	for (int i=0; i<k; ++i){
		printf("Case #%d: ", i+1);
		scanf("%d%d", &n, &m);
		int a = (1 << n);
		if ((m+1) % a == 0) printf("ON\n");
		else printf("OFF\n");	
	}	

    return 0;
}