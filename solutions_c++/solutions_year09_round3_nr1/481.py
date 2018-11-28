#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <queue>
#include <list>
#include <vector>

#define REP(i,n) for (int i = 0; i < n; i++)
#define FOR(i,n,m) for (int i = n; i <= m; i++)
#define FORD(i,n,m) for (int i = n; i >= m; i--)
#define FOREACH(a,c) for (typeof((c).begin()) a = (c).begin(); a != (c).end(); a++)

typedef long long int LL;
//typedef set<int> SI;
//typedef list<int> LI;

char msg[100];
LL map[200];
int T;

void init(){
	REP(i,200)
		map[i] = -1;
}

int main(){
	scanf ("%d", &T);
	REP(i, T){
		init();
		scanf ("%s", msg);
		int len = strlen(msg);
		int ze = 0;
		REP(j,len){
			if (j == 0)
				map[msg[j]] = 1;
			else if (ze == 0)
				if (map[msg[j]] == -1){
					map[msg[j]] = 0;
					ze = 2;
				}
				else ;
			else{
				if (map[msg[j]] == -1){
					map[msg[j]] = ze;
					ze++;
				}
			}
			//printf ("%d\n", ze);
		}
		if (ze == 0)
			ze = 2;
		LL number = 0;
		REP(j,len){
			number = ze*number + map[msg[j]];
		}	
		/*REP(j,200)
			printf ("%c %d\n", j, map[j]);*/
		printf ("Case #%d: %lld\n",i+1, number);
		
	}

	return 0;
}
