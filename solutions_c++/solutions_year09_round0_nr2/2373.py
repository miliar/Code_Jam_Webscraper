#include <vector>
#include <queue>
#include <string>
#include <stdio.h>

using namespace std;

int t[102][102], dokad[102][102], comp[102][102];

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

struct para
{
	int a,b;
};

int W, H;

void bfs(int x, int y, int cmp)
{
	int i, nx, ny, px, py;
	queue<para> Q;
	para st = {x, y};
	comp[y][x] = cmp;
	Q.push(st);

	while (Q.size())
	{
		para p = Q.front();
		Q.pop();

		if (dokad[p.b][p.a] != -1) // jezeli nie jestesmy w zlewie
		{
			px = p.a + dx[dokad[p.b][p.a]];
			py = p.b + dy[dokad[p.b][p.a]];
			if (px>=0 && py>=0 && px < W && py < H)
			{
				if (comp[py][px] == -1)
				{
					para q = {px, py};
					comp[py][px] = cmp;
					Q.push(q); // dodajemy miejsce gdzie scieka
				}
			}
		}

		for (i=0; i<4; i++) // dodajemy pola z ktorych scieka na aktualne
		{
			nx = p.a + dx[i];
			ny = p.b + dy[i];
			if (nx < 0 || ny<0 || nx >= W || ny >= H) continue;
			if (comp[ny][nx] != -1) continue; // juz odwiedzone

			// sprawdzamy czy z tego pola scieka na nas
			if (dokad[ny][nx] != -1)
			{
				px = nx + dx[dokad[ny][nx]];
				py = ny + dy[dokad[ny][nx]];
				if (px!=p.a || py!=p.b) continue;
				para np = {nx, ny};
				Q.push(np);
				comp[ny][nx] = cmp;
			}
		}
	}

}

int main()
{
	int i,l,k,j;
	int T;
	string s;
	char word[112];
	vector <string> map;

	int x, y;


	scanf("%d", &T);
	for (k=0; k<T; k++)
	{
		scanf("%d %d", &H, &W);
		for (i=0; i<H; i++)
			for (l=0; l<W; l++)
			{
				scanf("%d", &j);
				t[i][l] = j;
				dokad[i][l] = -1;
			}

		for (i=0; i<H; i++)
			for (l=0; l<W; l++)
			{
				int dir = -1, mina = 10000000;
				for (j=0; j<4; j++)
				{
					x = l + dx[j];
					y = i + dy[j];
					if (x < 0 || y<0 || x >= W || y >= H) continue;
					if (t[y][x] >= t[i][l]) continue;

					if (t[y][x] < mina)
					{
						dir = j;
						mina = t[y][x];
					}
				}
				dokad[i][l] = dir;
			}


			for (i=0; i<H; i++) for (l=0; l<W; l++) comp[i][l] = -1;

			int cmp = 0;
			for (i=0; i<H; i++) for (l=0; l<W; l++) if (comp[i][l] == -1) bfs(l, i, cmp++);
			
			printf("Case #%d:\n", k+1);
			for (i=0; i<H; i++) 
			{
				printf("%c", 'a'+comp[i][0]);
				for (l=1; l<W; l++) printf(" %c", 'a'+comp[i][l]);
				if (k < T-1 || i < H - 1) printf("\n");
			}

	}

	char c;
	scanf("%c", &c);
	return 0;
}
