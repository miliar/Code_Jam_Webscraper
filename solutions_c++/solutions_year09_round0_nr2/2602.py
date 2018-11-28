#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
 
#define PI 3.1415926535897932384626433832795
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define rep(i,s,n) for(int i=s; i<n; i++)
#define repe(i,s,n) for(int i=s; i<=n; i++)
#define len(s) int((s).length()) 
#define pv(v) tr(v,i) cout << *i << " "; cout << endl
#define pr(i) cout << i << endl

using namespace std;

int xx[4] = {-1, 0, 0, 1 }, yy[4] =  { 0, -1, 1, 0} ;


struct basin_node {
	pair<int,int> b;
	pair<int,int> top_left;
	int id;
	bool operator < ( const basin_node &n) const {	
		return top_left < n.top_left;	
	}
		
};
int h,w;
vector< vector<int> > mybasin;
pair<int, int> solve(vector<vector< vector<pair<int,int> > > > &incoming, pair<int,int> &b, int id) {
	if(incoming[b.first][b.second].size() == 0) return b;
	pair<int,int> ans = make_pair(h,w);
	tr(incoming[b.first][b.second],i) {
		mybasin[i->first][i->second] = id;
		ans = min(ans, solve(incoming,*i,id)); 
	}
	return ans;
}
int main() {
	int t,c=0;
	cin >> t;
	while(t--) {
		c++;
		//cout << "case" << c << endl;
		cin >> h >> w;
		vector< vector<int> > hite(h,vector<int> (w,0));
		rep(i,0,h) rep(j,0,w) { cin >> hite[i][j]; }
		//rep(i,0,h) { rep(j,0,w) { cout << mapp[i][j] << " ";} cout << endl; }
		
		//cout << "1\n";
		vector<basin_node > basins;
		vector<vector< vector<pair<int,int> > > > incoming(h, vector< vector<pair<int,int> > > (w,vector<pair<int,int> >(0)));
		rep(i,0,h) rep(j,0,w) {
			//cout << "i= "<< i << " j=" << j << endl;
			vector<int> ht(4,hite[i][j]);
			rep(k,0,4) {
				int x = i + xx[k], y = j + yy[k];
				if(x >= 0 && x < h && y >= 0 && y < w) { 
					ht[k] = hite[x][y];
				}
				//cout << ht[k] << " ";	
			}
			//cout << endl;
			int mi = *min_element(all(ht));
			//cout << " mi = "<< mi << endl; 
			if(mi < hite[i][j]) {
				int k = 0;
				while(k < 4) { if(ht[k] == mi) break; k++;}
				int x = i + xx[k], y = j + yy[k];
				//cout << "x = "<< x <<  " y=" << y << endl;
				incoming[x][y].pb(make_pair(i,j));
					
			}
			else {
				basin_node bn;	
				bn.b = make_pair(i,j);
				bn.id = basins.size();
				basins.pb(bn);
			}	 	
								
		} 
		//cout << "2\n";
		mybasin.clear();
		mybasin.resize(h,vector<int> (w,-1));
		rep(i,0,sz(basins)) {
			mybasin[basins[i].b.first][basins[i].b.second] = i;
			basins[i].top_left = solve(incoming,basins[i].b,i);
		}
		sort(all(basins));
		//cout << "4\n";
		string x(w,'A');		
		vector<string> layout(h,x);
		rep(i,0,h)  rep(j,0,w) { 
			//cout << "i="<<i << " j="<<j << endl;			
			int id = mybasin[i][j]; 
			//cout << "id = " << id << endl;
			rep(k,0,basins.size()) { if(basins[k].id == id) {  layout[i][j] = char('a' + k); break;} }
			
		}
		
 		cout<<"Case #"<<c<<":\n";
		rep(i,0,h) { rep(j,0,w) { cout << layout[i][j] << " ";} cout << endl; }
		//cout << "6\n";
		incoming.clear();
		hite.clear();
	}	
	return 0;
}
