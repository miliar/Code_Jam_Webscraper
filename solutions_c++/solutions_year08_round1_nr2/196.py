#include <cstdio>
#include <vector>
#include <sstream>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>



using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FRR(i,a,b) for(int i=b-1;i>=0;i--)
#define VI vector<int>
#define VVI vector< VI >
#define VS vector<string>
#define pii pair<int, int>
#define INF 2000000000
#define sz size()
#define pb push_back
#define mp make_pair
#define ll long long int
#define eps 1e-9
#define print(v,n) {FOR(i,0,n)cout<<v[i]<<" ";cout<<endl;}
#define SORT(x) sort((x).begin(), (x).end())





int main(){
	int cases; cin >> cases;

	FOR(T,1,cases+1){
		cout << "Case #" << T << ": ";
		int n,m; cin >> n >> m;
		VVI maltList(n), unmaltList(n); 
		VI custMalt(m,-1), custUnCount(m,0);
		FOR(cust,0,m){
			int t; 
			cin >> t;
			FOR(i,0,t){
				int shake, likes; 
				cin >> shake >> likes;
				shake--;
				if(likes){
					custMalt[cust] = shake;
					maltList[shake].pb(cust);
				}
				else{
					custUnCount[cust]++;
					unmaltList[shake].pb(cust);
				}
			}
		}
		bool flag = true;
		VI done(m,0);
		VI chosen(n,0);
		while(flag){
			flag = false;
			FOR(i,0,m){
				if(done[i])continue;
				if(!custUnCount[i]){
					int malt = custMalt[i];
					if(malt != -1){
						chosen[malt] = 1;
						FOR(j,0,unmaltList[malt].sz){
							custUnCount[unmaltList[malt][j]]--;
						}
						FOR(j,0,maltList[malt].sz)done[maltList[malt][j]] = 1;	
						flag = true;
						break;
					}
					else{
						cout << "IMPOSSIBLE" << endl;
						goto here;	
					}	
				}
			}
		}
		print(chosen,n);
here:	;
	}
}


