#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <string.h>
#include <bitset>
#include <math.h>
#include <time.h>
#include <list>
#include <stack>

using namespace std;

typedef long long LL;
//typedef __int64 LL;
#define move(i) (1<<i)
#define take(a,b) (((a)>>(b))&1)
#define mp make_pair
#define pb push_back
#define VI vector<int>
#define MX vector<vector<int> >
#define PII pair<int,int>
#define SZ(X) ((int)(X.size()))
#define LEN(X) ((int)(X.length()))
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
//template<class T> inline T max(T a,T b){return a > b ? a : b;}
//template<class T> inline T min(T a,T b){return a < b ? a : b;}

// template by tracyzhu
vector<pair<char,int> > List;
VI O,B;
int main(){
	int i,j;
	int t,n,cas = 0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		List.clear();O.clear();B.clear();
		scanf("%d",&n);
		for(i = 1;i <= n;i++){
			int x;char cmd;
			cin>>cmd>>x;
			List.pb(mp(cmd,x));
			if(cmd == 'O') O.pb(x);
			else B.pb(x);
		}
		int ans = 0;
		int pos1 = 1,pos2 = 1,x1 = 0,x2 = 0;
		for(i = 0;i < SZ(List);i++){
			if(List[i].first == 'O'){
				x1++;
				int T = abs(List[i].second - pos1) + 1;
				ans += T;
				pos1 = List[i].second;
				if(x2 >= SZ(B)) continue;
				if(abs(B[x2] - pos2) <= T) pos2 = B[x2];
				else{
					if(B[x2] > pos2){
						pos2 += T;	
					}else{
						pos2 -= T;
					}
				} 	
			}else{
				x2++;
				int T = abs(List[i].second - pos2) + 1;
				ans += T;
				pos2  = List[i].second;
				if(x1 >= SZ(O)) continue;
				if(abs(O[x1] - pos1) <= T) pos1 = O[x1];
				else{
					if(O[x1] > pos1)pos1 += T;
					else pos1 -= T;
				}
			}
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
