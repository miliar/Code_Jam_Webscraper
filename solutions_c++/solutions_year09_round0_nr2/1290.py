#include <stdio.h>
#include <string.h>
#include <queue>
#include <vector>

using namespace std;

#define maxs (105)

typedef pair <int, int> PII;

const int dr[4] = {-1, 0, 0, 1};
const int dc[4] = {0, -1, 1, 0};
const char DIR[8] = "NWES";
const int inv[4] = {3, 2, 1, 0};

int B[maxs][maxs];
int V[maxs][maxs];
int proc[maxs];

int R, C;

vector <int> edge[maxs][maxs];
queue <PII> Q;

inline int inrange(int r, int c)
{
	return (r >= 0 && r < R && c >= 0 && c < C);
}

int main()
{
	int t11, T;

	scanf("%d", &T);

	for(t11 = 1; t11 <= T; ++t11)
	{
		int i, j, k;

		scanf("%d %d", &R, &C);

		memset(V, 0, sizeof(V));

		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C; ++j)
			{
				int a;
				scanf("%d", &a);
				B[i][j] = a;
			}
		}

		int bc = 0;

		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C; ++j)
			{
				int h = B[i][j];
				int k1 = -1;

				for(k = 0; k < 4; ++k)
				{
					int rr = i + dr[k];
					int cc = j + dc[k];

					if(inrange(rr, cc) && B[rr][cc] < h)
					{
						h = B[rr][cc];
						k1 = k;
					}
				}

				if(k1 == -1)
				{
					V[i][j] = ++bc;
//					printf("%d", bc);
				}
				else
				{
//					printf("%c", DIR[k1]);
					edge[i + dr[k1]][j + dc[k1]].push_back( inv[k1] );
				}
			}
//			printf("\n");
		}

		memset(proc, 0, sizeof(proc));

		proc[0] = 1;

		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C; ++j)
			{
				if(!proc[V[i][j]])
				{
					int id = V[i][j];
					proc[id] = 1;

					Q.push( PII(i, j) );

					while( !Q.empty() )
					{
						PII p = Q.front();
						Q.pop();

						int r = p.first;
						int c = p.second;

						int sz = edge[r][c].size();

						for(k = 0; k < sz; ++k)
						{
							int d = edge[r][c][k];
							int rr = r + dr[d];
							int cc = c + dc[d];

							V[rr][cc] = id;
							Q.push( PII(rr, cc) );
//							printf("%d : %d %d : %d %d -> %d %d\n", t11, i + 1, j + 1, r + 1, c + 1, rr + 1, cc + 1);
						}

						edge[r][c].clear();
					}

/*
					int r, c;

					printf("--\n");

					for(r = 0; r < R; ++r)
					{
						for(c = 0; c < C; ++c)
						{
							printf("%d", V[r][c]);
						}
						printf("\n");
					}

					printf("-----\n");
//*/
				}
			}
		}

		memset(proc, -1, sizeof(proc));

		int cc = 0;

		printf("Case #%d:\n", t11);

/*
		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C; ++j)
			{
				printf("%d", V[i][j]);
			}
			printf("\n");
		}
//*/

		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C; ++j)
			{
				if(proc[V[i][j]] == -1)
				{
					proc[V[i][j]] = cc++;
//					printf("%d : %d\n", V[i][j], proc[V[i][j]]);
				}

				if(j > 0)
					putchar(' ');

				printf("%c", proc[V[i][j]] + 'a');
			}
			printf("\n");
		}
	}

	return 0;
}
