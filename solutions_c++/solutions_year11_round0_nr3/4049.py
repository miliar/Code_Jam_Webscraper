#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
typedef long long ll;
int T,n,a[1100],xor1,xor2,sum,ans;
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n",&T); 
	for(int t=1;t<=T;t++){
		scanf("%d\n",&n); 
		for(int i=0;i<n;i++)scanf("%d",&a[i]);
		ans=0;
		for(int mask=1;mask<(1<<n)-1;mask++){
			xor1=xor2=sum=0;
			for(int i=0;i<n;i++)
				if(mask&(1<<i)) xor1^=a[i],sum+=a[i]; else xor2^=a[i];
			if(xor1!=xor2) continue;
			if(sum>=ans) ans=sum;
		}
		                             
		if(!ans){printf("Case #%d: NO\n",t);	continue;}
		printf("Case #%d: %d\n",t,ans);
	}
}
