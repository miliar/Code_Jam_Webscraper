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
#define PB push_back
#define LL long long
#define VII vector<int>
#define PII pair<int, int>
#define INF 2000000

using namespace std;

int t, n;

int main(){
    scanf("%d", &t);
    for(int testcase = 0; testcase < t; testcase++){
	scanf("%d", &n);
	int din;
	int res = 0;
	int mini = INF;
	int chk = 0;
	for(int i = 0; i < n; i++){
	    scanf("%d", &din);
	    res += din;
	    mini = min(mini, din);
	    chk ^= din;
	}

	printf("Case #%d: ", testcase+1);
	if(chk == 0) printf("%d\n", res - mini);
	else printf("NO\n");
    }
    return 0;
}