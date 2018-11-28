#include <vector>
#include <list>
#include <map>
#include <set>
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
 
typedef long long int lint;
typedef pair<lint,lint> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)

par tree[100010];
void trees(int n,lint A,lint B,lint C,lint D,lint x0,lint y0,lint M) {
	lint X,Y;
	X = x0, Y = y0;
	tree[0].x=X,tree[0].y=Y;
	for (int i = 1;i<=n-1;i++) {
  		X = (A * X + B)%M;
  		Y = (C * Y + D)%M;
		tree[i].x=X,tree[i].y=Y;
	}
}

par center(int a,int b,int c) {
	return par( (tree[a].x + tree[b].x + tree[c].x)/3 ,  (tree[a].y + tree[b].y + tree[c].y)/3 );
}

int main() {
	int t;
	cin >> t;
	rep(i,t) {
		lint n,A,B,C,D,x0,y0,M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		trees(n,A,B,C,D,x0,y0,M);
		//rep(j,n) cout << tree[j].x << " " << tree[j].y << endl;
		lint tot=0;
		rep(j,n)
		Rep(k,j+1,n)
		Rep(l,k+1,n) {
			par c=center(j,k,l);
			//cout << c.x << " " << c.y << endl;
			if (c.x*3 == tree[j].x + tree[k].x + tree[l].x && c.y*3 == tree[j].y + tree[k].y + tree[l].y)
				tot++;
		}
		cout << "Case #" << i+1 << ": " << tot << endl;
	}
	return 0;
}

