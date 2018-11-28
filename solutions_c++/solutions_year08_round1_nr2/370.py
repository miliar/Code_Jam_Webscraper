/*
	Author : Vinay Emani
	Contact : VinayEmani AT gmail DOT com
*/
#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <utility>
using namespace std;
#define lint long long
#define SZ(s) ((int)(s.size()))
#define PB push_back
#define MP make_pair
#define FORN(i,a,b) for(i=(int)(a);i<(int)(b);i++)
#define FOR(i,n) FORN(i,0,n)
#define FOREACH(it,S) for(typeof(S.begin()) it = S.begin();it != S.end();it++)
#define SET(x,a) memset(x,a,sizeof x)
#define BEG(a) a.begin()
#define END(a) a.end()
#define ALL(a) BEG(a),END(a)

int n,m;
int like[128][16];
int spec[128];

int main(){
	int t=0,cas;
	cin >> cas;
	while(cas--){
		t++;
		cin >> n >> m;
		SET(like,0);SET(spec,-1);
		int ans = 1024,i,j;
		FOR(i,m){
			int p;
			cin >> p;
			while(p--){
				int x,y;
				cin >> x >> y;
				x--;
				if(y==0)like[i][x]=1;
				else spec[i]=x;
			}
		}
		int take = -1;
		FOR(i,1<<n){
			int ans2=0;
			FOR(j,n)if(i&(1<<j))ans2++;
			int yes=1;
			FOR(j,m)if(spec[j]>=0 && i&(1<<spec[j])){
			}else{
				int f=0,k;
				FOR(k,n)if(!(i&(1<<k)) && like[j][k])f=1;
				if(!f)yes=0;
			}
			if(yes && ans>ans2){
				ans = ans2;
				take = i;
			}
		}
		if(ans==1024){
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << t << ": ";
			FOR(i,n-1)if(take&(1<<i))cout << 1 << " ";
			else cout << 0 << " ";
			if(take&(1<<i))cout << 1 << endl;
			else cout << 0 << endl;
		}
	}
	return 0;
}
