#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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

using namespace std;

double p[99999 + 20];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,a,b;
	double error,right,ans;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas ++){
		scanf("%d %d",&a,&b);
		for(int i = 0; i < a; i ++){
			scanf("%lf",&p[i]);
		}
		ans = 2.0 + b;
		right = 1;
		double now;
		for(int i = 0; i < a; i ++){
			right *= p[i];
			now = a + 2 * b - right * b - right - 2 * i;
			if(ans > now) ans = now;
		}
		printf("Case #%d: %.6lf\n",cas,ans);
	}
	return 0;
}