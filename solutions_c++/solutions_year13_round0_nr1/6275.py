#include<iostream>
#include<map>
#include<string>
#include<algorithm>
#include<bitset>
#include<cassert>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<queue>
#include<stack>
#include<vector>
#include<ctime>
#include<functional>
#include<set> 
#include<cctype>
#include<cstdlib>
using namespace std;
const double eps=1e-7;
const int BASE = 64;
const int maxn = BASE + 256;
const int maxe = BASE + 100;
const int INF = (1<<30)-1;
typedef unsigned long long ULL;
char bd[6][6];
int main(){
	freopen("A-large.in","r",stdin);
	//freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cs = 1; cs <= T; ++cs){
		printf("Case #%d: ",cs);
		int empty = 0;
		bool xwin = false,owin = false;
		for(int i = 0; i < 4; ++i){
			scanf("%s",bd[i]);
			int rowx = 0,rowo = 0,t=0;
			for(int j = 0;j < 4; ++j){
				if(bd[i][j] =='.') ++empty;
				else if(bd[i][j] =='T') ++t;
				else if(bd[i][j] == 'X') ++rowx;
				else ++rowo;
			}
			if(rowx+t == 4) {xwin = true;}
			else if(rowo+t==4){owin = true;}
		}
		if(xwin == true || owin == true){		
			if(xwin) puts("X won");
			else puts("O won");
		}else{			
			for(int i = 0; i < 4; ++i){
				int colx = 0, colo = 0,t = 0;
				for(int j = 0; j < 4; ++j){
					if(bd[j][i] == 'X') ++colx;
					else if(bd[j][i] =='O') ++colo;
					else if(bd[j][i] == 'T') ++t;
				}
				if(colx+t==4){xwin=true;break;}
				else if(colo+t==4){owin = true;break;}
			}
			if(xwin || owin){
				if(xwin) puts("X won");
				else puts("O won");
			}else{
				int colx = 0,colo = 0,t = 0;
				int cx = 0,cy = 0;
				for(int i = 0; i < 4; ++i){
					if(bd[cx][cy] == 'X') ++colx;
					else if(bd[cx][cy] =='O') ++colo;
					else if(bd[cx][cy] == 'T') ++t;
					++cx; ++cy;
				}
				if(colx+t==4){xwin = true;}
				else if(colo + t == 4){owin = true;}
				if(xwin || owin){
					if(xwin) puts("X won");
					else puts("O won");
				}else{
					colx = 0; colo = 0; t = 0;
					cx = 0; cy = 3;
					for(int i = 0; i < 4; ++i){
						if(bd[cx][cy] == 'X') ++colx;
						else if(bd[cx][cy] =='O') ++colo;
						else if(bd[cx][cy] == 'T') ++t;
						++cx; --cy;
					}
					if(colx+t==4){xwin = true;}
					else if(colo + t == 4){owin = true;}
					if(xwin || owin){
						if(xwin) puts("X won");
						else puts("O won");
					}else{
						if(empty == 0) puts("Draw");
						else puts("Game has not completed");
					}
				}
			}
		}
	}

	return 0;
}
