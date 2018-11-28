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
#include <functional>
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
vector<string>V;
int used[1000+5];
int gues[1000+5];
bool has(string x,char y){
	 int i;
	 for(i = 0;i < x.length();i++){
	 	if(x[i] == y) return true;
	 }
	 return false;
}
int cal(string ans){
	int i,x = 0;
	for(i = 0;i < ans.length();i++)
		if(gues[i] == 0) x++;
	return x;
}
int can(string ans,string L){
     int i,j,k;
     memset(used,0,sizeof(used));
     memset(gues,0,sizeof(gues));
	 for(i = 0 ;i < SZ(V);i++){
	 	if(V[i].length() != ans.length())used[i] = 1;
	 }
	 int score = 0;
	 for(i = 0;i < L.length();i++){
	 	int f = 0;
	 	if(cal(ans) == 0) break;
	 	 for(j = 0;j < SZ(V);j++){
		 	if(used[j] == 1) continue;
		 	if(has(V[j],L[i])){f = 1;break;}
	 	 }
		 if(f == 0)continue;
		 if(has(ans,L[i]) == 0){
		 		score++;
		 		for(j = 0;j < SZ(V);j++){
					if(used[j] == 1) continue;
					if(has(V[j],L[i])){used[j] = 1;}  	
		 		}
		 		continue;
		 }
		 for(j = 0;j < ans.length();j++){
		 		if(ans[j] == L[i]){gues[j] = 1;}
		 }
		 for(j = 0;j < SZ(V);j++){
		 	if(used[j] == 1) continue;
		 	int x = 0;
		 	for(k = 0;k < V[j].length();k++){
			 	if(gues[k] == 1 && V[j][k] != ans[k]){x = 1;break;}
			 	if(gues[k] == 0 && V[j][k] == L[i]){x = 1;break;}
		 	}
			if(x == 1){used[j] = 1;} 
		 }	
	 }
	 return score;
}
vector<string>Ans;
int main(){
	int i,j,k,t,cas = 0;
	freopen("B-small-attempt4.in","r",stdin);
	freopen("B-small-attempt4.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		int n,m;
		scanf("%d %d",&n,&m);
		V.clear();
		for(i = 1;i <= n;i++){
			string s;
			cin>>s;
			V.pb(s);
		}
		Ans.clear();
		for(i = 1;i <= m;i++){
			string L;
			cin>>L;
			int ans = -1;
			string anss = "";
			for(j = 0;j < n;j++){
				int k = can(V[j],L);
				if(k > ans){ans = k;anss = V[j];}
			}
			Ans.pb(anss);
		}
		printf("Case #%d:",++cas);
		for(i = 0;i < m;i++){
			cout<<" ";
			cout<<Ans[i];
		}
		cout<<endl;
	}
	return 0;
}