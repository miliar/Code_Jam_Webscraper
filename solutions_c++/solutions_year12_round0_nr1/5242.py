#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <map>

#define REP(a,b) for (int a = 0; a < b; a++)
#define FORU(a,b,c) for (int a = b; a <= c; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RESET(a,b) memset(a,b,sizeof a)

#define LOLO long long 
#define PII pair<int,int>
#define FI first
#define SE second
#define MP make_pair
#define PB push_back

using namespace std;

char sc1[1005],sc2[1005],peta[50];
int n,le;

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	/*
	RESET(peta,'.');
	
	scanf("%d", &n);
	gets(sc1);
	REP(i,n){
		gets(sc1);
		gets(sc2);
		
		le = strlen(sc1);
		REP(j,le){
			int a = sc1[j] - 'a';
	
			if (peta[a] == '.'){
				peta[a] = sc2[j];
			}else if (peta[a] != sc2[j]){
				cout << sc1[j] << " doubled\n";	
			}
		}
	}	
	
	REP(i,26){
		printf("peta[%d] = '%c';\n", i, peta[i]);
	}
	*/

peta[0] = 'y';
peta[1] = 'h';
peta[2] = 'e';
peta[3] = 's';
peta[4] = 'o';
peta[5] = 'c';
peta[6] = 'v';
peta[7] = 'x';
peta[8] = 'd';
peta[9] = 'u';
peta[10] = 'i';
peta[11] = 'g';
peta[12] = 'l';
peta[13] = 'b';
peta[14] = 'k';
peta[15] = 'r';
peta[16] = 'z';
peta[17] = 't';
peta[18] = 'n';
peta[19] = 'w';
peta[20] = 'j';
peta[21] = 'p';
peta[22] = 'f';
peta[23] = 'm';
peta[24] = 'a';
peta[25] = 'q';
	
	scanf("%d", &n);
	gets(sc1);
	REP(jt,n){
		gets(sc1);
		
		le=strlen(sc1);
		REP(i,le){
			if (('a' <= sc1[i]) && (sc1[i] <= 'z')){
				sc1[i] = peta[sc1[i] - 'a'];
			}	
		}
		
		printf("Case #%d: %s\n", jt+1, sc1);
	}
	
	return 0;	
}
