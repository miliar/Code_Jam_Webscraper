#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>    
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits.h>
using namespace std;

int ans, state;
char str[1000];
char machine[100] = "welcome to code jam";
int sz;

void rec(int n, int state){
	if(machine[state] == '\0'){
		ans += 1;
		if(ans >= 10000)
			ans -= 10000;
		return;
	}
	if(n == sz)
		return;

	for(int i=n;i<sz;i++){
		if(machine[state] == str[i])
			rec(i+1,state+1);
	}
}

int main(){
    int ts, l, d, n;

	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);

	scanf("%d\n", &ts);
	for(int i=0;i<ts;i++){
		ans = 0; state = 0;
		scanf("%[^\n]\n",str);
		sz = strlen(str);

		rec(0,0);

		printf("Case #%d: %04d\n",i+1,ans);
	}
	
    return 0;
}
