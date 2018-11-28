#include <cstdio>
#include <string>
#include <set>
#include <algorithm>
#include <iostream>
const int c=1000;
using namespace std;
multiset<int> s,t;
struct rec {int x,y; bool q;};
bool operator <  (const rec &a, const rec &b) {
	return a.x<b.x;
}
rec a[c+1];
int kd,na,nb,m,ra,rb;
void solve(int ii) {
	int i;
	ra=0;
	rb=0;
	s.clear();
	t.clear();
	sort(&a[1],&a[na+nb+1]);
	for (i=1; i<=na+nb; ++i) {	
		if (!a[i].q) {
			if (s.size()==0 || *s.begin()>a[i].x) ++ra; else s.erase(s.begin());
			t.insert(a[i].y+m);
		} else {
			if (t.size()==0 || *t.begin()>a[i].x) ++rb; else t.erase(t.begin());
			s.insert(a[i].y+m);
		}
		cerr << s.size() << ' ' << t.size() << '\n';
	}
	printf("Case #%d: %d %d\n",ii,ra,rb);
}
int main() {
	int i,ii,j,k,o;
	char s[10];
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kd);
	for (ii=1; ii<=kd; ++ii) {
		scanf("%d%d%d\n",&m,&na,&nb);
		for (i=1; i<=na; ++i) {
			scanf("%d:%d",&k,&o);
			a[i].x=k*60+o;
			scanf("%d:%d",&k,&o);
			a[i].y=k*60+o;
			a[i].q=0;
		}
		for (i=1; i<=nb; ++i) {
			scanf("%d:%d",&k,&o);
			a[i+na].x=k*60+o;
			scanf("%d:%d",&k,&o);
			a[i+na].y=k*60+o;
			a[i+na].q=1;
		}
		for (i=1; i<=na+nb; ++i) cerr << a[i].x << ' ' << a[i].y << ' ' << a[i].q << '\n';
		solve(ii);
	}
	return 0;
}
