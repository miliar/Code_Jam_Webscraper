#include "stdio.h"
#include "math.h"
#include "map"
#include "string"
#include "vector"
#include "algorithm"
#include "float.h"


bool visited[512][512];
bool board[512][512];
int memo[32][32][32][32];
int answer[262144];

int f(int x, int y, int x2, int y2) {

	int &mem = memo[x][y][x2][y2];
	if(mem != -1) return mem;

	bool chess = true;
	for(int i=x; i<=x2 && chess; ++i) {
		for(int j=y; j<=y2 && chess; ++j) {
			int manDist = (i-x) + (j-y);

			if(visited[j][i]) return mem = -1;
			if((manDist%2 == 0) && board[y][x] != board[j][i]) chess = false;
			else if((manDist%2 == 1) && board[y][x] == board[j][i]) chess = false;
		}
	}

	if(!chess) return mem = -1;


	return mem = std::max( f(x, y, x2 + 1, y2 + 1), (x2-x+1)*(y2-y+1));


}

int main() {
	

	freopen("inputC.in", "r", stdin);
	freopen("outsmall.txt", "w", stdout);
	//freopen("outlarge.txt", "w", stdout);
	int numCases;
	scanf("%d", &numCases);
	for(int caseNum=0; caseNum<numCases; ++caseNum) {
		memset(board, 0, sizeof(board));
		memset(memo, -1, sizeof(memo));
		memset(answer, 0, sizeof(answer));
		memset(visited, 0, sizeof(visited));

		printf("Case #%d: ", caseNum+1);
		
		int m, n;
		scanf("%d %d", &m, &n);
		for(int i=0; i<m; ++i) {
			int row;
			scanf("%x", &row);

			for(int j=1; j<n+1; ++j) {
				bool val = row & 1<<(j-1);
				int pos = n-j;
				board[i][n-j] = row & 1<<(j-1);
			}
		}


		int count = 0;
		int numBoard = 0;
		int max_ = 0;
		int a = 0, b = 0;
		while(true) {
			max_ = 0;
			a = 0;
			b = 0;
			for(int i=0; i<n-1; ++i) {
				for(int j=0; j<m-1; ++j) {
					int newval = f(i,j,i,j);
					if(newval > max_) {
						max_ = newval;
						a = i;
						b = j;
					}
					else if(newval == max_) {
						if(j < b) {
							max_ = newval;
							a = i;
							b = j;
						}
						else if(j == b) {
							if(i < a) {
								max_ = newval;
								a = i;
								b = j;
							}
						}
					}
				
				}
			}

			if(max_ == 0 || max_ == 1) break;
			
			count += max_;
			if(answer[max_] == 0) ++numBoard;
			++answer[max_];

			memset(memo, -1, sizeof(memo));
			int sizeBoard = (int)sqrt((double)max_);
			for(int i=a; i<a+sizeBoard; ++i) {
				for(int j=b; j<b+sizeBoard; ++j) {
					visited[j][i] = true;
				}
			}
			

			

		}


		int left = n*m - count;
		printf("%d\n", numBoard + (left>0 ? 1 : 0)); 
		for(int i=n*m; i>=0; --i) {
			if(answer[i] > 0) {
				//count +=  i*answer[i];
				printf("%d %d\n", (int)sqrt((double)i), answer[i]);
			}
		
		}

		
		if(left > 0) printf("%d %d\n", 1, left);


	}
	return 0;
}

