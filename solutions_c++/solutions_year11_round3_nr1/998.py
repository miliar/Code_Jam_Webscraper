#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <cctype>
#include <fstream>
#include <numeric>
#include <map>
#include <iterator>
#include <cstdlib>
#include <cstdio>
using namespace std;

#define INF 99999999
#define EPS 1e-7
#define MIN(a,b) ((a)<(b))?(a):(b)
#define MAX(a,b) ((a)>(b))?(a):(b)
#define REP(i,n) for(i=0; i<(n); i++)
#define FOR(i,a,b) for(i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()

#define SIZE 100+10
#define IN freopen("A-large.in","r",stdin);
#define OUT freopen("out","w",stdout);

int T,R,C;
char grid[SIZE][SIZE];
bool flag;

int main()
{
	IN
	OUT
	int t,i,j;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d:\n",t);
		scanf("%d %d",&R,&C);
		REP(i,R) scanf("%s",grid[i]);
		flag = true;
		REP(i,R){
			REP(j,C){
				if(grid[i][j] == '#'){
					if(j==C-1 || grid[i][j+1]!='#') flag = false;
					j++;
				}
			}
		}
		
		REP(i,C){
			REP(j,R){
				if(grid[j][i] == '#'){
					if(j==R-1 || grid[j+1][i]!='#') flag = false;
					j++;
				}
			}
		}
		
		if(flag){
			REP(i,R){
				REP(j,C){
					if(grid[i][j] == '#'){
						grid[i][j] = '/';
						grid[i][j+1] = '\\';
						grid[i+1][j] = '\\';
						grid[i+1][j+1] = '/';
					}
				}
			}
			REP(i,R) {printf("%s\n",grid[i]);}
		}else printf("Impossible\n");
	}
}	
	
