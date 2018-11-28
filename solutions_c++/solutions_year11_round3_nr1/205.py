#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

int r,c;
char map[55][55];

bool solve() {
	for (int i=0;i<r-1;i++)
		for (int j=0;j<c-1;j++) if (map[i][j]=='#') {
			if (map[i][j+1]=='#'&&map[i+1][j]=='#'&&map[i+1][j+1]=='#') {
				map[i][j]='/';
				map[i][j+1]='\\';
				map[i+1][j]='\\';
				map[i+1][j+1]='/';
			}
			else return false;
		}
	for (int i=0;i<r;i++)
		for (int j=0;j<c;j++) if (map[i][j]=='#') return false;
	return true;
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>r>>c;
		for (int i=0;i<r;i++)
			scanf("%s",map[i]);
		printf("Case #%d:\n",++kase);
		if (solve()) {
			for (int i=0;i<r;i++) printf("%s\n",map[i]);
		}
		else cout<<"Impossible"<<endl;
//		printf("\n");
	}
	return 0;
}
