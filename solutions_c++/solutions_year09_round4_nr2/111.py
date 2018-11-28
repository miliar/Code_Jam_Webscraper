#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <complex>
using namespace std;

typedef long long ll;
typedef long double ld;
#define sz ((int)size())

int oo = (int)1e9;

#define SMALL
//#define LARGE

char mp[51][51];
int r,c,f;

struct state{
	int x, y, digs;
	ll curR, nextR;
	bool operator <(const state & s)const{
		if( digs != s.digs )
			return digs > s.digs;
		if( x != s.x )
			return x < s.x;
		if( y != s.y )
			return y < s.y;
		return make_pair(curR,nextR) < make_pair(s.curR,s.nextR);
	}
	state(int a,int b){
		x =a;
		y = b;
		digs = 0;
		curR = nextR = 0;
	}
	state(int a, int b, int d, ll cc,ll nn){
		x=a;
		y=b;
		digs =d;
		curR = cc;
		nextR = nn;

	}
	state(){
		state(0,0);
	}
	void print(){
		cout << digs <<  endl;
		for(int i =0 ;  i< r ; i++ )
		{
			for(int j = 0 ; j < c; j++ ){
				if( i == x ){
					if( j == y )
						cout << "&";
					else{
						if( curR & (1<<j) )
							cout << ".";
						else
							cout << mp[i][j];
					}
				}else if( i == x+1 ){
					if( nextR & (1<<j) )
						cout << ".";
					else
						cout << mp[i][j];
				}else{
					cout << mp[i][j];
				}
			}
			cout << endl;
		}
		cout << endl;
	}
};

priority_queue<state> Q;
set<state> S;

int bfs(){
	Q = priority_queue<state>();
	S.clear();
	state init(0,0),cur,nw;
	Q.push(init);
	S.insert(init);
	if( c == 1 )
		return 0;
	int nx, ny;
	while(!Q.empty()){
		cur = Q.top();
		//cur.print();
		Q.pop();
		if( cur.x == r-1 )
			return cur.digs;
		nx = cur.x;
		ny = cur.y+1;
		int sets;
		//right
		if( ny < c && (mp[nx][ny] == '.' || (cur.curR& (1<<ny)))){
			if( mp[nx+1][ny] == '.' || (cur.nextR&(1<<ny)) ){
				//fall
				int i;
				for(i = 2 ; i+nx < r ; i++ ){
					if( mp[i+nx][ny] == '#' )
						break;
				}
				i--;
				if( i <= f ){
					//can fall
					nw = state(nx+i,ny,cur.digs,(i==1)?cur.nextR:0,0);
					sets = S.size();
					S.insert(nw);
					if( sets != S.size() )
					{
						Q.push(nw);
					}
				}
			}else{
				//move right
				nw = cur;
				nw.y = ny;
				sets = S.size();
				S.insert(nw);
				if( sets != S.size() )
				{
					Q.push(nw);
				}

				//dig right
				nw = cur;
				nw.nextR |= (1<<ny);
				nw.digs++;
				S.insert(nw);
				if( sets != S.size() )
				{
					Q.push(nw);
				}
			}
		}
		nx = cur.x;
		ny = cur.y-1;
		if( ny >= 0 && (mp[nx][ny] == '.' || (cur.curR& (1<<ny)))){
			if( mp[nx+1][ny] == '.' || (cur.nextR&(1<<ny)) ){
				//fall
				int i;
				for(i = 2 ; i+nx < r ; i++ ){
					if( mp[i+nx][ny] == '#' )
						break;
				}
				i--;
				if( i <= f ){
					//can fall
					nw = state(nx+i,ny,cur.digs,(i==1)?cur.nextR:0,0);
					sets = S.size();
					S.insert(nw);
					if( sets != S.size() )
					{
						Q.push(nw);
					}
				}
			}else{
				//move left
				nw = cur;
				nw.y = ny;
				sets = S.size();
				S.insert(nw);
				if( sets != S.size() )
				{
					Q.push(nw);
				}

				//dig left
				nw = cur;
				nw.nextR |= (1<<ny);
				nw.digs++;
				S.insert(nw);
				if( sets != S.size() )
				{
					Q.push(nw);
				}
			}
		}
	}
	return -1;
}

int main()
{
	freopen("a.txt","rt",stdin);
	#ifdef SMALL
	freopen("B-small-attempt1.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
	#endif
	#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
	#endif

	int t;
	scanf("%d ",&t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ",i+1);
		scanf("%d%d%d",&r,&c,&f);
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				scanf(" %c",mp[i]+j);
			}
		}
		int res = bfs();
		if( res == -1 )
			printf("No\n");
		else
			printf("Yes %d\n",res);
	}
	return 0;
}
