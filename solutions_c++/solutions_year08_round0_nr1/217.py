#include <cstdio>
#include <map>
#include <string>

using namespace std;

char NAME[100][1001];
int searchN, queryN;
int QUERY[10000];
int DP[100][1001];
enum{MAX = 10000};

map<string, int> M;

int main()
{
	int i;
	int caseN;
	char nameTmp[1002];

	scanf("%d",&caseN);

	for(int x=0;x < caseN; x++){
		M.clear();
		scanf("%d\n",&searchN);
		for(i=0;i<searchN;i++){
			scanf("%[^\n]\n", NAME[i]);
			M[ string(NAME[i]) ] = i;
		}
		scanf("%d\n",&queryN);
		for(i=0;i<queryN;i++){
			scanf("%[^\n]\n", nameTmp);
			QUERY[i] = M[ string(nameTmp) ];
		}
		for(i=0;i<queryN+1;i++)
			for(int j=0;j<searchN;j++)
				DP[j][i] = MAX;
		for(i=0;i<searchN;i++)
			DP[i][0] = 0;

		for(i=0;i<queryN;i++){
			for(int j=0;j<searchN;j++){
				for(int k=0;k<searchN;k++){
					if(j != k)
						DP[k][i+1] = min(DP[k][i+1], DP[j][i] + 1);
					else
						DP[k][i+1] = min(DP[k][i+1], DP[j][i]);
				}
			}
			DP[QUERY[i]][i+1] = MAX;
#if 0
			for(int j=0;j<searchN;j++){
				printf("%d ", DP[j][i+1]);
			}
			printf("\n");
#endif
		}
		int m = MAX;
		for(i=0;i<searchN;i++)
			m = min( m, DP[i][queryN] );
		printf("Case #%d: %d\n", x+1, m);
	}
}

