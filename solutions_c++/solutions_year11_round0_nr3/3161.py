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
	int tc, n, c[1023];
	scanf("%d",&tc);
	REP(t,tc){
		scanf("%d",&n);
		REP(i,n)scanf("%d",&c[i]);
		int ans=0, ch=0;
		int mt=20000000;
		REP(i,n){
			ch=ch^c[i];
			mt=min(mt,c[i]);
			ans+=c[i];
		}
		bool f=false;
		if(ch==0)f=true;
		printf("Case #%d: ",t+1);
		if(f)printf("%d\n",ans-mt);
		else puts("NO");
	}
	return 0;
}
