#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;

int i,j,k,l,h;
int t,T;
int n,m;
double a[200][200];
int c[200][200];
int f[200][200];
int s;
int d;

const double EPS = 1e-10;
double INF = 1e20;
double INFD = 2e20;

int dc[] = {1, 0, -1, 0};
int dr[] = {0, 1, 0, -1};

pair<int, int> mpi(int a, int b)
{
	return make_pair<int, int>(a,b);
}

double enterWaitTime(int sr, int sc, int dr, int dc, double time, bool moveTime)
{
	if(sr<0 || sr >= n || sc<0 || sc>=m)
	{
		return INFD;
	}
	if(c[dr][dc] - f[sr][sc] < 50 || c[dr][dc] - f[dr][dc] < 50 || c[sr][sc]-f[dr][dc]<50)
	{
		return INFD;
	}
	double w = h-10*time;
	double res;
	if (c[dr][dc]-w >= 50)
	{
		res = 0;
	}
	else
	{
		res = (50 - (c[dr][dc]-w))/10.0;
	}

	if(moveTime)
	{
		w = h-10*(time+res);
		if (w - f[sr][sc] >= 20)
		{
			res +=1;
		}
		else
		{
			res +=10;
		}
	}

	return res;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &T);
	for(t=1; t<=T; t++)
	{
		memset(a, 127, sizeof(a));
		
		scanf("%d%d%d", &h, &n, &m);
		for (i=0; i<n; i++)
		{
			for (j=0; j<m; j++)
			{
				scanf("%d", &c[i][j]);
			}
		}
		for (i=0; i<n; i++)
		{
			for (j=0; j<m; j++)
			{
				scanf("%d", &f[i][j]);
			}
		}

		/*printf("-------------------------------------\n");
		for (i=0; i<n; i++)
		{
			for (j=0; j<m; j++)
			{
				printf("%4d", c[i][j]-f[i][j]);
			}
			printf("\n");
		}
		printf("-------------------------------------\n");*/


		queue<pair<int, int>> q;
		queue<pair<int, int>> qq;
		pair<int, int> p;
		q.push(mpi(0,0));
		a[0][0]=0;
		int nr,nc;
		double dt;

		bool found = true;
		while(!q.empty())
		{
			p = q.front();
			q.pop();

			for (int d = 0; d<4; d++)
			{
				nr = p.first + dr[d];
				nc = p.second + dc[d];
				dt = enterWaitTime(p.first, p.second, nr, nc, 0, false);
				if(dt<EPS && a[nr][nc]>0)
				{
					a[nr][nc]=0;
					q.push(mpi(nr, nc));
					found = true;
				}
			}
		}

		for(i=0; i<n; i++)
		{
			for(j=0; j<m; j++)
			{
				if(a[i][j]<EPS)
				{
					q.push(mpi(i,j));
				}
			}
		}

		while(!q.empty())
		{
			p = q.front();
			q.pop();
			for (int d = 0; d<4; d++)
			{
				nr = p.first + dr[d];
				nc = p.second + dc[d];
				dt = enterWaitTime(p.first, p.second, nr, nc, a[p.first][p.second], true);
				if(dt < INF && a[nr][nc]>a[p.first][p.second]+dt)
				{
					a[nr][nc]=a[p.first][p.second]+dt;
					q.push(mpi(nr, nc));
				}
			}
		}

		/*printf("======================================\n");
		for (i=0; i<n; i++)
		{
			for (j=0; j<m; j++)
			{
				if(a[i][j]<INF)
				{
					printf("%5.1lf", a[i][j]);
				}
				else
				{
					printf("  INF");
				}
			}
			printf("\n");
		}
		printf("-------------------------------------\n");*/


		printf("Case #%d: %lf\n", t, a[n-1][m-1]);
    }
	return 0;
}

/*
1
630 10 10
891 924 925 533 393 908 597 739 228 264
822 644 819 936 802 971 643 835 276 917
938 480 987 948 500 790 771 731 989 966
463 955 845 980 856 645 418 968 629 106
778 671 327 900 841 976 655 993 820 722
890 657 755 287 860 554 352 886 782 705
795 343 953 612 959 867 957 570 817 991
939 900 892 953 915 648 680 608 549 345
275 869 687 826 534 762 901 824 403 423
378 761 921 754 477 941 558 831 943 775
782 38 222 113 306 738 364 380 148 95
323 281 76 394 713 925 598 817 50 863
523 226 96 895 494 548 548 724 905 965
63 892 769 80 696 524 349 398 347 58
131 657 246 654 780 561 288 978 71 499
557 571 268 62 212 454 248 725 194 528
699 64 361 589 553 843 118 203 732 693
248 637 608 701 442 250 578 496 145 73
129 421 679 667 266 705 857 541 47 314
172 691 881 390 132 898 81 552 807 305
*/