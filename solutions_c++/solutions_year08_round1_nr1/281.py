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

long long a[1000],b[1000];

int main(){
	int T,tt;
	scanf("%d",&T);
	for(tt=1;tt<=T;tt++){
		int n,i;
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%I64d",&a[i]);
		}
		for(i=0;i<n;i++){
			scanf("%I64d",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n,greater<long long>());
		long long ret=0;
		for(i=0;i<n;i++){
			ret+=a[i]*b[i];
		}

		//cout<<sizeof(long double)<<endl;
		printf("Case #%d: %I64d\n",tt,ret);
	}
}
