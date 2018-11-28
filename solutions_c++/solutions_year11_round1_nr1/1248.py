#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <sstream>
using namespace std;

bool visit[101][101];

int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("ans.txt","w",stdout);
	memset(visit, 0, sizeof(visit) );
	for(int i = 1; i <= 100; i++){
		for(int j = 0; j <= i; j++){
			if(j*100 % i == 0){
				visit[i][j*100/i] = true;
			}
		}
	}

	int T; cin >> T;
	for(int cas = 1; cas <= T; cas++){
		int N, PD, PG;
		cin >> N >> PD >> PG;
		if(N >= 100){
			printf("Case #%d: Possible\n",cas);
			continue;
		}
		if(PD < 100 && PG == 100 || PD > 0 && PG == 0){
			printf("Case #%d: Broken\n",cas);
			continue;
		}

		int res = -1;
		for(int i = 1; i <= N; i++){
			if(visit[i][PD]){		
				res = i;
				break;
			}
		}

		if(res!=-1)
			printf("Case #%d: Possible\n",cas);
		else
			printf("Case #%d: Broken\n",cas);
	}
}