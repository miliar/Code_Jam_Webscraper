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


int main() {
#ifndef ONLINE_JUDGE
//    freopen("in", "r", stdin);
//    freopen("out", "w", stdout);
#endif

    int dataset;
    scanf("%d", &dataset);
    for(int cas=1; cas<=dataset; ++cas) {
    	int n, s, p;
    	int score[100] = {};
    	scanf("%d %d %d", &n, &s, &p);
    	for(int i=0; i<n; ++i) {
    		scanf("%d", &score[i]);
    	}
    	bool ok[100] = {};
    	bool sp[100] = {};
    	bool ok_sp[100] = {};
    	for(int i=0; i<n; ++i) {
    		for(int a = 0; a<=10; ++a) {
    			for(int b=a; b<=10 && b<=a+2; ++b) {
    				int c = score[i]-a-b;
    				if(c<b) {
    					break;
    				}
    				if(c>a+2) {
    					continue;
    				}
    				if(c==a+2) {
    					if(c>=p) {
    						ok_sp[i] = true;
    					}
    					sp[i] = true;
    				} else {
    					if(c>=p) {
    						ok[i] = true;
    					}
    				}
    			}
    		}
    	}
    	int key = 0;
    	bool checked[100] = {};
    	for(int i=0; i<n; ++i) {
    		if(s == 0) {
    			break;
    		}
    		if(!ok[i] && ok_sp[i]) {
    			++key;
    			checked[i] = true;
    			--s;
    		}
    	}
    	for(int i=0; i<n; ++i) {
    		if(!checked[i] && ok[i]) {
    			++key;
    		}
    	}

    	printf("Case #%d: %d\n", cas, key);
    }

    return 0;
}
