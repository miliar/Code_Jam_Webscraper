#include <iostream>
#include <tr1/unordered_set>
#include <algorithm>
#include <utility>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <cassert>

using namespace std;
#define printf(...)

int R,C,B;

typedef pair<int,int> IP;
const int dx[]={0,1,0,-1};
const int dy[]={1,0,-1,0};

struct S {
	IP p[6];

	bool operator==(const S& s) const {
		for(int i=0; i<5; ++i)
			if (p[i]!=s.p[i]) return 0;
		return 1;
	}
};
struct H {
	tr1::hash<int> h;
	unsigned operator()(const S& s) const {
		unsigned r=0;
		for(int i=0; i<5; ++i)
			r = r*131 + 331*h(s.p[i].first) + h(s.p[i].second);
		return r;
	}
};
tr1::unordered_set<S,H> used;

char area[64][64];

bool has(const S& s, int x, int y)
{
	for(int i=0; i<B; ++i)
		if (s.p[i].first==y && s.p[i].second==x) return 1;
	return 0;
}
bool pairr(IP a, IP b)
{
	int y=abs(a.first-b.first);
	int x=abs(a.second-b.second);
	return (y==0 && x==1) || (y==1 && x==0);
}
bool suse[8];
void sdfs(const S& s, int n)
{
	suse[n]=1;
	for(int i=0; i<B; ++i)
		if (!suse[i] && pairr(s.p[n], s.p[i]))
			sdfs(s, i);
}
bool safe(const S& s)
{
	memset(suse, 0, sizeof(suse));
	sdfs(s,0);
	for(int i=0; i<B; ++i) if (!suse[i]) {/*cout<<"asd\n";*/return 0;}
	return 1;
}

void dump(const S& s)
{
	for(int i=1; i<=R; ++i) {
		for(int j=1; j<=C; ++j) {
			if (has(s,j,i)) putchar('o');
			else if (area[i][j]=='o') putchar('.');
			else putchar(area[i][j]);
		}
		putchar(10);
	}
	putchar(10);
}

int solve(S start, S end)
{
	if (start==end) return 0;
	vector<S> cur,next;
	cur.push_back(start);
	used.insert(start);
	int step=0;
	while(!cur.empty()) {
		++step;
		printf("rnd %d\n", step);
		for(unsigned i=0; i<cur.size(); ++i) {
			S& s = cur[i];
			//dump(s);
			bool sf = safe(s);
			printf("safe: %d\n",sf);
			for(int j=0; j<B; ++j) {
				for(int k=0; k<4; ++k) {
					int y=s.p[j].first+dy[k], x=s.p[j].second+dx[k];
					int yy=s.p[j].first+dy[(k+2)%4], xx=s.p[j].second+dx[(k+2)%4];
//					printf("trying %d %d ; %c %c\n", x,y,area[y][x],area[yy][xx]);
					assert(area[y][x]=='#' || area[y][x]=='.' || area[y][x]=='x' || area[y][x]=='o');
					if (area[y][x]=='#' || area[yy][xx]=='#') continue;
					if (has(s, x, y) || has(s,xx,yy)) continue;
//					printf("ok\n");
					S s2=s;
					s2.p[j].first=y;
					s2.p[j].second=x;
					if (!sf && !safe(s2)) continue;
					sort(s2.p,s2.p+B);
					if (s2==end) return step;
					if (used.count(s2)) continue;
					used.insert(s2);
					next.push_back(s2);
				}
			}
		}
		cur.clear();
		cur.swap(next);
	}
	return -1;
}

int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>R>>C;
		B=0;
		used.clear();
		memset(area, '#', sizeof(area));
		S start={};
		S end={};
		int si=0,ei=0;
		for(int i=0; i<R; ++i) {
			cin>>&area[i+1][1];
			for(int j=0; j<C; ++j) {
				char c=area[i+1][j+1];
				if (c=='.' || c=='#') continue;
				if (c=='x') ++B, end.p[ei++]=IP(i+1,j+1);
				if (c=='o') start.p[si++]=IP(i+1,j+1);
				if (c=='w') ++B, start.p[si++]=end.p[ei++]=IP(i+1,j+1), area[i+1][j+1]='x';
			}
			area[i+1][C+1]=area[i+1][0]='#';
		}
		sort(start.p,start.p+B);
		sort(end.p,end.p+B);
		cout<<"Case #"<<a<<": "<<solve(start,end)<<'\n';
	}
}
