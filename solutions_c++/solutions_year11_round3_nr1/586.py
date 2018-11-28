#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 100
#define BIT(x) (1<<(x-1))
using namespace std;
#define min(a,b) (((a) < (b)) ? (a) : (b))
int R,C;
char map[MAX][MAX];
int flag;
void readdata()
{
	int i;
	memset(map, 0, sizeof(map));
	flag = 1;
	scanf("%d%d",&R,&C);
	for (i=0; i<R; ++i)
		scanf("%s",map[i]);

}

void solve()
{
	int i,j;
	for (i=0; i<R; ++i){
		for (j=0; j<C; ++j) {
			if (map[i][j] == '#') {
				if (map[i][j+1] == '#' && 
					map[i+1][j] == '#' &&
					map[i+1][j+1] == '#') {
					
					map[i][j]	= '/';
					map[i][j+1] = '\\';
					map[i+1][j] = '\\';
					map[i+1][j+1] = '/';
				}else{
					flag = -1; //can not
				}
			}
		}
	}
}

void output()
{
	int i,j;
	if (flag == 1) {
		for (i=0 ;i<R; ++i){
			for (j=0; j<C; ++j) {
				printf("%c",map[i][j]);
			}
			printf("\n");
		}
	}else {
		printf("Impossible\n");
	}
	
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	int nt, it;
	
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		readdata();
		solve();
		printf("Case #%d:\n",it);
		output();
		
	}
	return 0;
}