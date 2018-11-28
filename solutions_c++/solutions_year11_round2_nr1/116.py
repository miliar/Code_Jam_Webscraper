#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <sstream>
using namespace std;


const int maxn = 128;
double WP[maxn];
double OWP[maxn];
double OOWP[maxn];
int n;
char board[maxn][maxn];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("ans.txt","w",stdout);
	
	int T; scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++){
		scanf("%d",&n);
		for(int i = 0; i < n; i++)scanf("%s",board[i]);

		for(int i = 0; i < n; i++){
			int win = 0, all = 0;
			for(int j = 0; j < n; j++){
				if(board[i][j]=='.')continue;
				if(board[i][j]=='1')win++;
				all++;
			}
			WP[i] = 1.0 * win / all;
		}

		for(int i = 0; i < n; i++){
			double p = 0, d = 0;
			for(int j = 0; j < n; j++){
				if( board[i][j]=='.' )continue;

				int win = 0, all = 0;
				for(int k = 0; k < n; k++){
					if(k == i || board[j][k]=='.')continue;
					if(board[j][k]=='1')win++;
					all++;
				}
				p +=  1.0 * win / all;
				d += 1;
			}
			OWP[i] = p / d;
		}

		for(int i = 0; i < n; i++){
			double p = 0, all = 0;
			for(int j = 0; j < n; j++){
				if(board[i][j]=='.')continue;
				p += OWP[j];
				all += 1;
			}
			OOWP[i] = p / all;
		}
		printf("Case #%d:\n",cas);
		for(int i = 0; i < n; i++){
			printf("%.9lf\n",0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
		}
		
	}
}