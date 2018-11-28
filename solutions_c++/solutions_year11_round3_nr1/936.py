#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <climits>
#define REP(i,n) for(int (i)=0, _n=(n); (i) < (_n); i++)
#define REPD(i,n) for(int (i)=(n-1); i >= 0; i--)
#define FOR(i,a,n) for(int (i)=(a),_n=(n); (i) <= (_n); (i)++)
#define FORD(i,a,n) for(int (i)=(a),_n=(n); (i) >= (_n); (i)--)
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(cs,1,test){
		char grid[100][100];
		int row,col;
		scanf("%d %d",&row,&col);
		REP(i,row)
			scanf("%s",grid[i]);
			
		bool pos=1;
		REP(i,row)
			REP(j,col){
				if(grid[i][j] == '#'){
					if(i!=row-1 && j!=col-1 && grid[i][j+1]=='#' && grid[i+1][j] == '#' && grid[i+1][j+1] == '#'){
						grid[i][j] = '/';
						grid[i][j+1] = '\\';
						grid[i+1][j] = '\\';
						grid[i+1][j+1]= '/';
					}
						else pos = 0;	
				}
			}
		
		printf("Case #%d:\n",cs);
		if(!pos)
			puts("Impossible");
		else{
			REP(i,row)
				puts(grid[i]);	
		}
	}
	//system("pause");
    return 0;
}
