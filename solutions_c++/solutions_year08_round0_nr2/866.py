#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

struct el {
	int time;
	int side;
	int what;
	
	el () {}
	el ( int t , int s , int w ) {
		time = t;
		side = s;
		what = w;
	}
};

int t;
int n , m;
vector < el > a;

int gethour() {
	int x , y;
	
	scanf ("%d:%d",&x,&y);

	return x * 60 + y;
}

void read() {
	int i;
	
	scanf ("%d",&t);
	scanf ("%d%d",&n,&m);
	
	a.clear();
	
	for (i=1;i<=n;i++) {
		a.push_back ( el ( gethour() , 0 , 0 ) );
		a.push_back ( el ( gethour() + t , 1 , 1 ) );
	}
	
	for (i=1;i<=m;i++) {
		a.push_back ( el ( gethour() , 1 , 0 ) );
		a.push_back ( el ( gethour() + t , 0 , 1 ) );
	}
}

int cmp ( el a , el b ) {
	if ( a.time == b.time )
		return a.what > b.what;
	return a.time < b.time;
}

void solve() {
	int i;
	int l , r;
	int ans1 , ans2;
	
	ans1 = ans2 = 0;
	l = r = 0;
		
	sort ( a.begin() , a.end() , cmp );
	
	for (i=0;i<(int)a.size();i++) {
		if ( !a[i].side ) {
			if ( !a[i].what ) -- l;
			else ++ l;
		} else {
			if ( !a[i].what ) -- r;
			else ++ r;
		}
		
		if ( l < ans1 ) ans1 = l;
		if ( r < ans2 ) ans2 = r;
	}
	
	printf ("%d %d\n",-ans1,-ans2);
}

int main() {
	int i , k;
	
	scanf ("%d",&k);
	for (i=1;i<=k;i++) {
		read();
		printf ("Case #%d: ",i);
		solve();
	}
	
	return 0;
}
