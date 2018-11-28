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

using namespace std;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back


int main(){
	int tc, ans, n, low, high, p[15000];
	scanf("%d",&tc);
	REP(t,tc){
		scanf("%d%d%d",&n,&low,&high);
		REP(i,n)scanf("%d",&p[i]);
		ans=0;
		for(int i=low;i<=high;i++){
			bool f=true;
			REP(j,n){
				if(p[j]==1||p[j]==i)continue;
				int a=min(i,p[j]), b=max(i,p[j]);
				if(b%a!=0){
					f=false;
					break;
				}
			}
			if(f){
				ans=i;
				break;
			}
		}
		printf("Case #%d: ",t+1);
		if(ans==0)puts("NO");
		else printf("%d\n",ans);
	}
	return 0;
}
