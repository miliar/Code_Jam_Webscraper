#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#define MP make_pair
#define ST first
#define ND second
#define PII pair<int,int>
#define PB push_back
#define VII vector<int>
#define VIT vector<int>::iterator
#define LL long long

using namespace std;

int testc;
int n;
LL low, high;

LL tab[10005];

int main(){
    scanf("%d", &testc);
  
    for(int tc = 1; tc <= testc; tc++){
	scanf("%d %lld %lld", &n, &low, &high);
	for(int i = 0; i < n; i++) scanf("%lld", &tab[i]);
	
	sort(tab, tab+n);

	if(low == 1LL){
	    printf("Case #%d: 1\n", tc);
	    continue;
	}

	while(low <= high){
	    bool ok = true;
	    for(int i = 0; i < n; i++){
		if(tab[i] % low != 0 && low % tab[i] != 0){
		    ok = false;
		    break;
		}
	    }
	    if(ok) break;
	    low++;
	}

	if(low <= high) printf("Case #%d: %lld\n", tc, low);
	else{
	    printf("Case #%d: NO\n", tc);
	}
    }
    return 0;
}