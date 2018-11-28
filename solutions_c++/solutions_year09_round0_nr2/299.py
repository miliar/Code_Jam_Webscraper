// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <set>
#include <map>

/////////////////////////
///@author: sakar2003 ///
///@lang: C++         ///
/////////////////////////

using namespace std;

const int MAXN = 100010;

int T;

int det[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

char label[128][128];
int mm[128][128];
int H,W;

void solve(){
	memset(label, 0, sizeof(label));
	char start = 'a';
	for(int i = 0; i < H; ++i){
		for(int j = 0; j < W; ++j){
			if(!label[i][j]){
				vector<pair<int, int> > vp;
				vp.push_back(make_pair(i, j));

				int sx = i, sy = j;
				bool brk = false;
				while(!brk){
					int minHeight = mm[sx][sy];
					bool found = false;
					int x = sx, y = sy;
					for(int k = 0; k < 4; ++k){
						int tx = det[k][0] + x;
						int ty = det[k][1] + y;
						if(tx >= 0 && ty >= 0 && tx < H && ty < W && mm[tx][ty] < minHeight){
							sx = tx; sy = ty; found = true; minHeight = mm[tx][ty];
						}
					}
					if(found){
						vp.push_back(make_pair(sx, sy));
						if(label[sx][sy]) brk = true;
					}
					else{
						break;
					}

				}
				char lb = start;
				if(brk) lb = label[vp[vp.size()-1].first][vp[vp.size()-1].second];
				else{
					++start;
				}
				for(int k = 0; k < vp.size(); ++k){
					label[vp[k].first][vp[k].second] = lb;
				}
			}
		}
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("Bl.txt", "w", stdout);
	scanf("%d", &T);
	
	for(int tt = 1; tt <= T; ++tt)
	{
		scanf("%d%d", &H, &W);
		for(int i = 0; i < H; ++i){
			for(int j = 0; j < W; ++j){
				scanf("%d", &mm[i][j]);
			}
		}
		solve();
		printf("Case #%d:\n", tt);
		for(int i = 0; i < H; ++i){
			for(int j = 0; j < W; ++j){
				printf("%c ", label[i][j]);
			}
			printf("\n");
		}
	}

	return 0;
}

