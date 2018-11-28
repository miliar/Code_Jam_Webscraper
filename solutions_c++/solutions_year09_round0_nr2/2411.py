#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

class pnt
{
public:
	int i;
	int j;
	int a;
	int c[4];
	int comp;
};

pnt mat[128][128];

int h, w;

int aM(int i, int j)
{
	int menor, d;

	d = -1;
	menor = mat[i][j].a;

	if(i > 0 && mat[i-1][j].a < menor)
	{
		d = 0;
		menor = mat[i-1][j].a;
	}

	if(j > 0 && mat[i][j-1].a < menor)
	{
		d = 1;
		menor = mat[i][j-1].a;
	}

	if(j < (w-1) && mat[i][j+1].a < menor)
	{
		d = 2;
		menor = mat[i][j+1].a;
	}

	if(i < (h-1) && mat[i+1][j].a < menor)
	{
		d = 3;
		menor = mat[i+1][j].a < menor;
	}

	return d;
}

int main(void)
{
	int t, c = 1;

	scanf("%d", &t);

	vector<pnt> sinks;
	queue<pnt> qqe;

	char bas[32];
	char nl;

	while(c <= t)
	{
		scanf("%d %d", &h, &w);


		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				scanf("%d", &(mat[i][j].a));
				mat[i][j].c[0] = mat[i][j].c[1] = mat[i][j].c[2] = mat[i][j].c[3] = 0;
				mat[i][j].i = i;
				mat[i][j].j = j;
				mat[i][j].comp = -1;
			}
		}

		for(int i = 0; i < 32; i++) bas[i] = 0;
		nl = 'a';

		sinks.clear();

		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				int menor = aM(i, j);

				switch (menor)
				{
					case 0:
						mat[i-1][j].c[3] = 1;
						break;
					case 1:
						mat[i][j-1].c[2] = 1;
						break;
					case 2:
						mat[i][j+1].c[1] = 1;
						break;
					case 3:
						mat[i+1][j].c[0] = 1;
						break;
					case -1:
						sinks.push_back(mat[i][j]);
						break;
				}
			}
		}

		int tam = sinks.size();
		for(int i = 0; i < tam; i++)
		{
			
			qqe.push(sinks[i]);

			while(!qqe.empty())
			{
				pnt bla = qqe.front();
				qqe.pop();
			
				pnt tmp;

				int a = bla.i;
				int b = bla.j;

				if(mat[a][b].comp != -1) continue;

				mat[a][b].comp = i;

				/*printf("(%d, %d) - (%d,%d,%d,%d) - %d\n", a, b, mat[a][b].c[0], 
										mat[a][b].c[1],
										mat[a][b].c[2],
										mat[a][b].c[3], i);*/

				if(mat[a][b].c[0] == 1)
				{
					tmp = mat[a-1][b];
					qqe.push(tmp);
				}

				if(mat[a][b].c[1] == 1)
				{
					tmp = mat[a][b-1];
					qqe.push(tmp);
				}

				if(mat[a][b].c[2] == 1)
				{
					tmp = mat[a][b+1];
					qqe.push(tmp);
				}

				if(mat[a][b].c[3] == 1)
				{
					tmp = mat[a+1][b];
					qqe.push(tmp);
				}
			}
		}

		printf("Case #%d:\n", c);
		

		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				if(bas[mat[i][j].comp] == 0)
				{
					bas[mat[i][j].comp] = nl;
					//printf("Componente %d tem letra '%c'\n", mat[i][j].comp, nl);
					nl++;
				}

				if(j == 0) printf("%c", bas[mat[i][j].comp]);
				else printf(" %c", bas[mat[i][j].comp]);
			}

			printf("\n");
		}

		c++;
	}

	return 0;
}
