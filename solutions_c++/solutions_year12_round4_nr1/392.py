// #includes {{{
#include <algorithm>
#include <numeric>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cmath>
using namespace std;
// }}}
// pre-written code {{{
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define RREP(i,a,b) for(int i=(int)(a);i<(int)(b);++i)
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
//#define IFOR(i,it,c) for(__typeof((c).begin())it=(c).begin();it!=(c).end();++it,++i)
#define ALL(c) (c).begin(), (c).end()
#define MP make_pair
//#define PB push_back
#define TO_STRING(VariableName) # VariableName
//#define DB(c) cout<<TO_STRING(c)<<"="<<(c)<<endl

#define EXIST(e,s) ((s).find(e)!=(s).end())

#define RESET(a) memset((a),0,sizeof(a))
#define SET(a) memset((a),-1,sizeof(a))
#define PB push_back

typedef long long Int;
typedef unsigned long long uInt;
typedef long double rn;

typedef pair<int,int> pii;

#ifdef DEBUG
#include"debug.h"
#include"print.h"
#endif
// }}}

const int N=10010;
int d[N],l[N];
int D;
int capt[N];//maximum length capture i

void main2(){
	int n;
	cin>>n;
	REP(i,n)cin>>d[i]>>l[i];
	cin>>D;
	memset(capt,-1,sizeof(capt));
	capt[0]=d[0];
	REP(i,n){
		int lim=d[i]+capt[i];
		if(lim>=D){
			cout<<"YES"<<endl;
			return;
		}
		for(int j=i+1;j<n;j++){
			if(lim<d[j])break;
			if(l[j]>=d[j]-d[i])capt[j]=max(d[j]-d[i],capt[j]);
			else capt[j]=max(l[j],capt[j]);
		}
	}
	cout<<"NO"<<endl;
}

//{{{ main function
int main() {
	int T;scanf("%d", &T);
	REP(ct, T){
		printf("Case #%d: ",ct+1);
		main2();
	}
	return 0;
}
//}}}
