#include<stdio.h>
#include<utility>
#include<stack>

using namespace std;

#define SIZE 109

int arr[SIZE][SIZE];
int mark[SIZE][SIZE];

int dx[] = {-1, 0, 0, 1}, dy[] = {0, -1, 1, 0};

int main(){
	int T, x, i, j, k, R, C, cnt, curmin, r, c, val;
	pair<int,int> pp, pp1;
	stack< pair<int, int> > st;

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &T);
	for(x = 1; x<=T; ++x){
		scanf("%d%d", &R, &C);

		for( i=0; i<R; ++i){
			for( j=0; j<C; ++j){
				scanf("%d", &arr[i][j]);
			}
		}

		memset( mark , -1, sizeof(mark));

		cnt = 0;
		for( i=0; i<R; ++i){
			for( j=0; j<C; ++j){
				if( mark[i][j] == -1){
					pp = make_pair(i,j);
					while(!st.empty()) st.pop(); 
					while(1){
						st.push(pp);
						curmin = 100000009;

						for( k=0; k<4; ++k){
							r = pp.first+dx[k]; c=pp.second + dy[k];
							if(r<0 || r>=R || c<0 || c>=C || arr[r][c] >= arr[pp.first][pp.second]) continue;
							if( arr[r][c] < curmin){
								curmin = arr[r][c];
								pp1 = make_pair(r, c);
							}
						}
						
						if(curmin >= 100000009){
							val = cnt++;
							break;
						}
						if(mark[pp1.first][pp1.second] != -1){
							val = mark[pp1.first][pp1.second];
							break;
						}
						//mark[pp1.first][pp1.second] = 1;
						pp = pp1;
					}

					while(!st.empty()){
						pp = st.top(); st.pop();
						mark[pp.first][pp.second] = val;
					}
				}
			}
		}

		printf("Case #%d:\n", x);
		for(i=0; i<R; ++i){
			for( j=0; j<C; ++j){
				if( j ) putchar(' ');
				putchar(mark[i][j] + 'a');
			}
			puts("");
		}
	}

	return 0;
}