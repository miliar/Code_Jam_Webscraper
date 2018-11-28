#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a;i < b;++i)

string grid[51];

int main(){
int test = GI;
FOR(nt, 1, test + 1) {
	int m = GI, n = GI;
	FOR(i,0,m)	cin >> grid[i];

	FOR(i,1,m)
		FOR(j,1,n) {
			string s = string(1,grid[i-1][j-1]) + string(1,grid[i-1][j]) + string(1,grid[i][j-1]) + string(1,grid[i][j]);
			if(s == "####")
				grid[i-1][j-1] = '/', grid[i-1][j] = '\\', grid[i][j-1] = '\\',grid[i][j] = '/';
		}	
	bool isp = 1;
	FOR(i,0,m) FOR(j,0,n) if(grid[i][j] == '#') {isp = 0;break;}
		
	printf("Case #%d:\n", nt);
	if(!isp)
		printf("Impossible\n");
	else {
		FOR(i,0,m)
			cout << grid[i] << endl;
	}
}

return 0;
}
