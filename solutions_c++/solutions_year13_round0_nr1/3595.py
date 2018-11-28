//Problem A. Tic-Tac-Toe-Tomek
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <cmath>
#include <cassert>

using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i=x; i<y; i++)
#define FOR(it,A) for(typeof A.begin(); it!=A.end(); it++)
#define quad(x) (x)*(x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second

typedef long long ll;
typedef pair<int,int> pii;

int main(){
	int ncases;
	char m[4][4], c, x, y, xw, ow, np;
	scanf("%d",&ncases);
	f(i,0,ncases){
		xw = 0;
		ow = 0;
		scanf("%c",&c);
		f(p,0,4){
			f(q,0,4){
				scanf("%c",&m[p][q]);
			}
			scanf("%c",&c);
			
		}
		//f(p,0,4){
		//	f(q,0,4){
		//		printf("%c",m[p][q]);
		//	}
		//	cout<<endl;
		//}
		//test
		np = 0;
		f(p,0,4){
			x = 0;
			y = 0;
			f(q,0,4){
				switch(m[p][q]){
					case 'X':
						x++;
						break;
					case 'O':
						y++;
						break;
					case 'T':
						x++;
						y++;
						break;
					case '.':
						np++;
						break;
				}
			}
			if(x==4){
				xw = 1;
				break;
			}
			if(y==4){
				ow = 1;
				break;
			}
		}


		if(xw!=1 && ow!=1){
			f(p,0,4){
				x = 0;
				y = 0;
				f(q,0,4){
					switch(m[q][p]){
						case 'X':
							x++;
							break;
						case 'O':
							y++;
							break;
						case 'T':
							x++;
							y++;
							break;
					}
				}
				if(x==4){
					xw = 1;
					break;
				}
				if(y==4){
					ow = 1;
					break;
				}

			}
		}

		if(xw!=1 && ow!=1){
			x = 0;
			y = 0;
			f(p,0,4){
				switch(m[p][p]){
					case 'X':
						x++;
						break;
					case 'O':
						y++;
						break;
					case 'T':
						x++;
						y++;
						break;
				}
			}
			if(x==4){
				xw = 1;
			}
			if(y==4){
				ow = 1;
			}
		}

		if(xw!=1 && ow!=1){
			x = 0;
			y = 0;
			f(p,0,4){
				switch(m[p][3-p]){
					case 'X':
						x++;
						break;
					case 'O':
						y++;
						break;
					case 'T':
						x++;
						y++;
						break;
				}
			}
			if(x==4){
				xw = 1;
			}
			if(y==4){
				ow = 1;
			}
		}
		
		printf("Case #%d: ",i+1);
		if(xw==1){
			printf("X won\n");
		}else if(ow==1){
			printf("O won\n");
		}else if(np==0){
			printf("Draw\n");
		}else{
			printf("Game has not completed\n");
		}

	}
	return 0;
}
