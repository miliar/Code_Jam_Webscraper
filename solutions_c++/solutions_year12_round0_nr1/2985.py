#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <ctime>
#define MAXN
using namespace std;
const int INF = 0x3f3f3f3f;
const double eps = 1e-9;
typedef long long LL;
typedef pair<int, int> pii;

const char *hints[] = {
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

const char *answers[] = {
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"
};

char mapping[1<<8];

int main() {
#ifndef ONLINE_JUDGE
//    freopen("in", "r", stdin);
//    freopen("out", "w", stdout);
#endif

    for(int i=0; i<(1<<8); ++i) {
    	mapping[i] = i;
    }
    for(int i=0; i<3; ++i) {
    	for(int j=0; hints[i][j]; ++j) {
        	mapping[ hints[i][j] ] = answers[i][j];
    	}
    }
    mapping[ 'z' ] = 'q';
    mapping[ 'q' ] = 'z';


    int dataset;
    scanf("%d", &dataset);
    char str[103];
    gets(str);
    for(int cas=1; cas<=dataset; ++cas) {
    	gets(str);
    	for(int i=0; str[i]; ++i) {
    		str[i] = mapping[ str[i] ];
    	}
    	printf("Case #%d: %s\n", cas, str);
    }

    return 0;
}
