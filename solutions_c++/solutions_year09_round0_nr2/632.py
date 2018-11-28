#include <cstdio>
using namespace std;

#define REP(i,n) for (int i=0;i<n;i++)

int alt[102][102];

// -2, not a basin
// -1, is a basin but unnamed
// 0~ named
int basin[102][102];
int name[102][102];

int dir[4][2]={ {-1,0}, {0,-1}, {0, 1}, {1, 0} };

int main()
{
	int tno;
	scanf("%d", &tno);
	for (int tcase=1;tcase<=tno;tcase++) {
		int h, w;
		scanf("%d %d", &h, &w);

		for (int i=0;i<=h+1;i++)
			for (int j=0;j<=w+1; j++)
				basin[i][j]=-2;

		const int bigv = 1000000;
		for (int i=0;i<=w+1;i++)
			alt[0][i]=alt[h+1][i]=bigv;
		for (int i=1;i<=h;i++)
			alt[i][0]=alt[i][w+1]=bigv;

		for (int i=1;i<=h;i++)
			for (int j=1;j<=w;j++) {
				scanf("%d", &alt[i][j]);
			}

		int basincount=0;
		for (int i=1;i<=h;i++)
			for (int j=1;j<=w;j++) {
				if ( basin[i][j] != -2 ) {
					name[i][j]=basin[i][j];
					continue;
				}

				int cury=i;
				int curx=j;

				while(1) {
					int minalt=alt[cury][curx];
					int mdir=-1;
					REP(k,4) {
						int ny=cury+dir[k][0];
						int nx=curx+dir[k][1];
						if (minalt>alt[ny][nx]) {
							minalt=alt[ny][nx];
							mdir=k;
						}
					}
					if (mdir==-1) {
						if (basin[cury][curx]==-2)
							basin[cury][curx]=basincount++;
						name[i][j]=basin[cury][curx];
						break;
					}

					cury += dir[mdir][0];
					curx += dir[mdir][1];
				}

			}


		printf("Case #%d:\n", tcase);
		for (int i=1;i<=h;i++) {
			for (int j=1;j<=w;j++)
				printf("%c ", name[i][j]+'a');
			printf("\n");
		}
	}
	return 0;
}

