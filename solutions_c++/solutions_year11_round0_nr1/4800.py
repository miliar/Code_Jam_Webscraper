#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<map>

using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_n=(b);i<=_n;i++)
#define PB push_back
#define st first
#define nd second

int n, y;
char x[10];

int main(){
	int tc;
	scanf("%d", &tc);
	REP(_i, tc){
		scanf("%d", &n);
		int posO = 1, posB = 1, res = 0, temp;
		char now;
		REP(i, n){
			scanf("%s %d", &x, &y);
			if(i == 0)now = x[0], temp = 0;
			
			if(now == x[0]){
				int used = abs(((x[0] == 'O') ? posO : posB) - y) + 1;
				res += used;
				temp += used;
			} else{
				now = x[0];
				int move = abs(((x[0] == 'O') ? posO : posB) - y);
				int used = (move <= temp) ? 0 : move - temp;
				
				res += used + 1;	
				temp = used + 1;
			}
			
			if(now == 'O') posO = y;
			else posB = y;
		}
		
		printf("Case #%d: %d\n", _i+1, res);
	}

return 0;
}
