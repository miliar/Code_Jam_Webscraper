/*
 * B.cpp
 *
 *  Created on: Sep 3, 2009
 *      Author: Amr
 */


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

int mp[101][101], nmp[101][101];

int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
		int h,w,cur;


int FF(int i, int j){
	if(nmp[i][j]!=-1)
		return nmp[i][j];
	int mn = 1<<29;
	for (int k = 0; k < 4; ++k) {
		if(i+dx[k]>=0&& i+dx[k]<h&&j+dy[k]>=0&&j+dy[k]<w&&mp[i+dx[k]][j+dy[k]]<mp[i][j])
			mn = min(mn,mp[i+dx[k]][j+dy[k]]);
	}
	for (int k = 0; k < 4; ++k) {
		if(i+dx[k]>=0&& i+dx[k]<h&&j+dy[k]>=0&&j+dy[k]<w&&mp[i+dx[k]][j+dy[k]]==mn)
			return nmp[i][j] = FF(i+dx[k],j+dy[k]);
	}
	return nmp[i][j] = cur++;
}

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("B.out","wt",stdout);
	int t;
	scanf("%d",&t);
	int ii = 1;
	while(t--){
		cur = 0;
		scanf("%d%d",&h,&w);
		memset(mp,-1,sizeof mp);
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				scanf("%d",&mp[i][j]);
			}
		}
		memset(nmp,-1,sizeof nmp);
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				FF(i,j);
			}
		}
		char c = 'a';
		map<int,char> found;
		printf("Case #%d:\n",ii++);
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				if(j)
					printf(" ");
				if(found.find(nmp[i][j])==found.end()){
					found[nmp[i][j]] = c++;
				}
				printf("%c",found[nmp[i][j]]);
			}
			printf("\n");
		}
	}
	return 0;
}
