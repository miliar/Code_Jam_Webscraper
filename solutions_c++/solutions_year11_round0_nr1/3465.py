#include  <stdio.h>
#include <cmath>
#include <vector>
#include <cstdlib>

using namespace std;

#define PB push_back
#define ST first
#define ND second
#define ALL(v) v.begin(),v.end()
#define RALL(v) v.rbegin(),v.rend()
#define SZ size()
#define FOR(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define REP(i,m) for(int i=0;i<(int)(m);i++)
#define REP2(i,n,m) for(int i=n;i<(int)(m);i++)
#define MP make_pair

void print_result(int x, int y) {
	printf("Case #%d: %d\n", x, y);
}

void solve(int nr, vector<pair<int, int> > v){
	int st = 1;
	int moves = 0;	
	int pos1 = 1;
	int pos2 = 1;
	int omoves = 0;
	int prev = 0;
	int step = 0;
	FOR(it, v){
		pair<int,int> p = *it;		
		if(p.ST == 1){
			step = abs(p.ND - pos1); // +1 move button
			pos1 = p.ND;
			if(prev == 1 || prev == 0){
				omoves += step+1; 
				moves += step+1;
			} else {
				if(step > omoves){
					step = step - omoves;
				} else {
					step = 0;
				}
				omoves = step+1;
				moves += step+1;		
			}	
			prev = 1;	
		} else {
			step = abs(p.ND - pos2); // +1 move button
			pos2 = p.ND;
			if(prev == 2 || prev == 0){
				omoves += step+1; 
				moves += step+1;
			} else {
				if(step > omoves){
					step = step - omoves;
				} else {
					step = 0;
				}
				omoves = step+1;
				moves += step+1;		
			}	
			prev = 2;	
		}
	}
	print_result(nr, moves);
}


int main(){
	int T, N;
	scanf ("%d", &T);
	int i, j, pos;
	char c;
	for(i=1; i<=T; i++){
		vector<pair<int, int> > v;
		scanf("%d",  &N);
		for(j=0; j<N; j++){
			c = getchar();
			c = getchar();
//			printf("char : %c\n", c);
			scanf("%d", &pos);
//			printf("read: %d\n", pos);
			if(c == 'O')
				v.push_back(MP(1,pos));
			else
				v.push_back(MP(2,pos));
		}
		solve(i, v);
	}
	return 0;
}
