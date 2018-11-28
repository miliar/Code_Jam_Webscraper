#include <cstdio>
#include <set>
#include <utility>
#include <algorithm>
#include <memory.h>
using namespace std;
#define MP make_pair
#define X first
#define Y second

int main() {
	set<pair<int,int> > maj[2];
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T,r,x1,y1,x2,y2;

	scanf("%d",&T);
	for(int ti = 0;ti < T;ti++) {
		scanf("%d",&r);
		maj[0].clear();
		maj[1].clear();
		for(int i=0;i<r;i++) {
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if(x1 > x2) swap(x1,x2);
			if(y1 > y2) swap(y1,y2);			
			for(int x = x1-1;x < x2;x++)
				for(int y = y1-1;y < y2;y++)			
					maj[0].insert(MP(x,y)); }
					
		int res = 0;
		int RES = 0;
		while(1) {
			maj[res^1].clear();
			for(set<pair<int,int> >::iterator it = maj[res].begin();it != maj[res].end();it++) {
				if(maj[res].count(MP(it->X+1,it->Y - 1)))
					maj[res^1].insert(MP(it->X+1,it->Y));
					
				if(maj[res].count(MP(it->X-1,it->Y)) || maj[res].count(MP(it->X,it->Y - 1)))
					maj[res^1].insert(MP(it->X,it->Y)); }
			RES++;
			if(maj[res^1].size() == 0) break;
			res ^= 1; }
		printf("Case #%d: %d\n",ti+1,RES); }
	return 0; }