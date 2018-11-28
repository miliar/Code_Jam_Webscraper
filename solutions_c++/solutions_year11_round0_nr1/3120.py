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
	int tc, n, ans, b, o, p;
	char c;
	cin >> tc;
	REP(i,tc){
		cin >> n;
		ans=0;
		b=o=1;
		int bt=0, ot=0;
		char be='x';
		REP(j,n){
			cin >> c >> p; 
			if(c=='B'){
				if(c==be)ans+=abs(p-b)+1;
				else ans+=max(0,abs(p-b)-(ans-bt))+1;
				b=p;
				bt=ans;
			}
			else{
				if(c==be)ans+=abs(p-o)+1;
				else ans+=max(0,abs(p-o)-(ans-ot))+1;
				o=p;
				ot=ans;
			}
			be=c;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
