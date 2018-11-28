#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
 
using namespace std;
 
#define pb push_back
#define mp make_pair
#define vs vector<string>
#define vi vector<int>
#define pii pair<int,int>
#define vvi vector< vector<int> >
#define vpi vector< pair<int,int> >
#define LL long long

int R,C,D;
int W[11][11];

int main() {
        int T; cin >> T;
        for(int iter=0;iter<T;iter++) {
			cin >>R>>C>>D;
			for(int i=0;i<R;++i)  {
				string t;
				cin >> t;
				for(int j=0;j<C;++j)
				W[i][j] = t[j]-'0';
			}
			int ans = -1;
			for(int i=0;i<R;++i)
			for(int j=0;j<C;++j)
			for(int s = 3; s <= min(R-i,C-j); ++s) {
				int xw = 0;
				int yw = 0;
				for(int y=0;y<s;++y)
				for(int x=0;x<s;++x) {
				if(x==0 && y==0) continue;
				if(x==s-1 && y==0) continue;
				if(x==0 && y==s-1) continue;
				if(x==s-1 && y==s-1) continue;
				if(s%2==0) { 
					xw += (-1+s-2*x)*W[i+y][j+x];
					yw += (-1+s-2*y)*W[i+y][j+x];
				}				else {
					xw += (s/2-x)*W[i+y][j+x];
					yw += (s/2-y)*W[i+y][j+x];
				}
				}
				if(xw==0 && yw==0) ans = max(ans, s);
			}
			if(ans==-1)
			cout<<"Case #"<<(iter+1)<<": IMPOSSIBLE\n";
			else
			cout<<"Case #"<<(iter+1)<<": "<<ans<<"\n";
	}
}

