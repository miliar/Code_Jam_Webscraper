#include <map>     
#include <set>     
#include <cmath>    
#include <cstdio>   
#include <vector>     
#include <string>     
#include <sstream>    
#include <iostream>    
#include <algorithm>     
using namespace std;     
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)     
#define FORE(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)     
#define SET(x, v) memset(x, v, sizeof (x))     
#define sz size()     
#define cs c_str()     
#define pb push_back     
#define mp make_pair    
 
typedef long long i64;     
int dat[51][51];
int board[51][51];
int R, C;
int ltd;
void conv(int* row, int x) {
	ltd = 0;
	FOR(i,0,C) {
		if(x & (1<<i)) {
			ltd++;
			row[i] = 1;
		}
		else
			row[i] = 0;
	}
}
bool check() {
	FOR(i,0,R) {
		FOR(j,0,C) {
			int cnt = 0;
			FOR(k,-1,2) {
				FOR(l,-1,2) {
					int px = i + k;
					int py = j + l;
					if(px>=0 && py>=0 && px<R && py<C && board[px][py]) {
						cnt++;
					}
				}
			}
			if(cnt!=dat[i][j]) {
				/*
				FOR(x,0,R) {
					FOR(y,0,C) 
						printf("%d",board[x][y]);
					printf("\n");
				}
				printf("(%d, %d)should be %d(but %d)\n",i,j,dat[i][j],cnt);
				*/
				return false;
			}
		}
	}

	return true;
}
bool chk(int r) {
	FOR(i,0,C) {
		int cnt = 0;
		FOR(k,-1,2) {
			FOR(l,-1,2) {				
				int px = r + k;
				int py = l + i;
				if(px>=0 && px<R && py>=0 && py<C && board[px][py])
					cnt++;
			}			
		}
		if(dat[r][i]!=cnt)return true;
	}
	return false;
}
int main() {
	freopen("C.in", "r",stdin);
	int e=  0, T;
	scanf("%d",&T);
	while(T--) {
		scanf("%d%d",&R,&C);
		FOR(i,0,R)
			FOR(j,0,C)
				scanf("%d",&dat[i][j]);
		int N = (1<<C);
		int ans = 0;
		if(R==3) {
			FOR(i,0,N)
				FOR(j,0,N) 
					FOR(k,0,N) {
						conv(board[0], i);
						conv(board[2], k);
						conv(board[1], j);
						if(ltd <=ans) continue;
						if(check()) {
//							printf("%d %d %d\n",i,j,k);
//							printf("OK\n");
							ans = ltd;
						}
					}
		}
		else if(R==5) {
			FOR(i,0,N)
				FOR(j,0,N) 
					FOR(k,0,N) {
						int now;
						conv(board[2], k);
						if(ltd<=ans) continue;
						now = ltd;
						conv(board[1], i);
						conv(board[3], j);
						if(chk(2)) {
							continue;
						}
						int do0, do4;
						do0= false;
						do4 = false;
						FOR(l,0,N) {
							if(!do0) {
								conv(board[0], l);
								if(!chk(1) && !chk(0))
									do0 = true;
							}
							if(!do4) {
								conv(board[4], l);
								if(!chk(3) && !chk(4))
									do4 = true;
							}
							if(do0 && do4) break;
						}
						if(do0 && do4) {
							ans = now;
						}
				}

		}
		printf("Case #%d: %d\n",++e, ans);
	}


	return 0;
}



