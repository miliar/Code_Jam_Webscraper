#include <iostream>
using namespace std;
#define MAXM 102

int m[MAXM][MAXM];
int n[MAXM][MAXM];
int R;

int main()
{
	int cases, c = 1;
	freopen("test", "r", stdin);
	freopen("out", "w", stdout);

	scanf("%d", &cases);
	while(cases--)
	{
		int x1, x2, y1, y2;

		memset(m, 0, sizeof(m));
		scanf("%d", &R);
		for(int i = 0;i < R; i++){
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);

			for(int j = x1;j <= x2; j++){
				for(int k = y1; k <= y2; k++){
					m[j][k] = 1;
					//printf("%d\n", m[i][j]);
				}
			}
		}

		int ans = 0;
		while(true){
			ans++;
			bool no = false;
			memset(n, 0, sizeof(n));
			for(int i = 1;i <=MAXM; i++){
				for(int j = 1;j <= MAXM; j++){
					//printf("%d", m[i][j]);
					if(m[i][j] == 0){
						if(m[i-1][j] == 1 && m[i][j-1] == 1){
							n[i][j] = 1;
						}
					}else{
						if(m[i-1][j] == 1 || m[i][j-1] == 1){
							n[i][j] = 1;
						}
					}
				}
				//printf("\n");
			}

			for(int i = 1;i <= MAXM; i++){
				for(int j = 1;j <= MAXM; j++){
					m[i][j] = n[i][j];

					if(m[i][j] == 1)no = true;
				}

			}
			//printf("\n");
			if(!no)break;
		}


		printf("Case #%d: %d\n",c++, ans);
	}
	return 0;
}
