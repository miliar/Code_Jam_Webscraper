#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>


#define SZ(x) ((int)(x).size())

#define MAXS 101
#define MAXQ 1001

#define INF 1000000

using namespace std;

int sol[MAXS][MAXQ];

int main(){
	int tcc = 0, tc = 0;
	for(cin >> tc; tc; tc--){
		int s, q;
		scanf("%d\n", &s);

		vector<string> se;

		for (int i = 0; i < s; i++){
			char buff[1000];
			gets(buff);
			se.push_back(string(buff));
		}

		scanf("%d\n", &q);
		
		vector<string> qa;

		for (int i = 0; i < q; i++){
			char buff[1000];
			gets(buff);
			qa.push_back(string(buff));
		}

		memset(sol, -1, sizeof(sol));

		for (int i = 0; i < s; i++) sol[i][0] = 0;
		int cm = 0;

		for (int i = 0; i < q; i++){
			int rm = INF;
			for (int j = 0; j < s; j++){
				if ( qa[i] == se[j] ) sol[j][i + 1] = INF;
				else {
					sol[j][i + 1] = sol[j][i];
					if ( cm + 1 < sol[j][i + 1] ) sol[j][i + 1] = cm + 1;
				}
				if ( sol[j][i + 1] < rm ) rm = sol[j][i + 1];
			}
			cm = rm;
		}

		printf("Case #%d: %d\n", ++tcc, cm);
	}
	return 0;
}
