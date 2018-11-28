#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <sstream>
#include <fstream>

#define ll long long int
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define RFOR(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define RREP(i,n) RFOR(i,0,n)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define V(x) vector< x >
#define vi V(int)
#define vs V(string)
#define pb push_back
#define mkp make_pair
#define PII pair <int,int>
#define uli unsigned long long int
#define GI ({int t;scanf("%d",&t);t;})
const int INF = (int)1<<30;

using namespace std;
int getinput() {
	int h,m;
	scanf(" %d:%d",&h,&m);
	return h*60+m;
}
bool Bsort(pair<int,int> A,pair<int,int> B) {
	if(A.second!=B.second) return A.second<B.second;
	return A.first<B.first;
}
int main() {	int t=GI;
	REP(T,t) {
		int x=0,y=0,delay=GI,m=GI,n=GI;
		vector<pair<int,int> > A,B;
		REP(i,m) A.pb(mkp(getinput(),getinput()));
		REP(i,n) B.pb(mkp(getinput(),getinput()));
		sort(A.begin(),A.end());
		sort(B.begin(),B.end(),Bsort);
		//REP(i,m) cout<<A[i].first<<" "<<A[i].second<<endl;cout<<endl;
		//REP(i,n) cout<<B[i].first<<" "<<B[i].second<<endl;cout<<endl;		
		V(bool) B_paired(n,false);
		REP(i,m) {
			REP(j,n) if(!B_paired[j] && A[i].first+delay<=B[j].second) {
				B_paired[j]=true;
				break;
			}
		}
		REP(i,n)y+=!B_paired[i];
		V(bool) A_paired(m,false);
		sort(A.begin(),A.end(),Bsort);
		sort(B.begin(),B.end());
		REP(i,n) {
			REP(j,m) if(!A_paired[j] && B[i].first+delay<=A[j].second) {
				A_paired[j]=true;
				break;
			}
		}
		REP(i,m)x+=!A_paired[i];
		cout<<"Case #"<<T+1<<": "<<x<<" "<<y<<endl;
	}
	return 0;
}
