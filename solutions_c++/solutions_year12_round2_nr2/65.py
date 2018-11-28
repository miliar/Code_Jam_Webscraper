#include<stdio.h>
#define DB_MAX 999999999
int T, t;

int H, N, M;
int ceil[200][200], floor[200][200], vis[200][200];
double d[200][200];
int wi[4] = {-1,0,1,0}, wj[4] = {0,1,0,-1};
int main()
{
	int i, j, k, mi, mj, w, ni, nj;
	double min, curr_time;
	freopen("input-large.txt", "r", stdin);
	freopen("output-large.txt", "w", stdout);
	scanf("%d", &T);
	for(t = 1 ; t <= T; t++)
	{
		scanf("%d %d %d", &H, &N, &M);
		for(i = 1; i <= N; i++) for(j = 1; j <= M; j++)
			scanf("%d",&ceil[i][j]);
		for(i = 1; i <= N; i++) for(j = 1; j <= M; j++)
			scanf("%d",&floor[i][j]);
		for(i = 1; i <= N; i++) for(j = 1; j <= M; j++) d[i][j] = DB_MAX, vis[i][j] = 0;
		d[1][1] = 0;

		// �ð��Ҹ���� �����ִ¾ֵ� �ٰ�������
		for(k = N * M; k >= 1; k--)
		{
			if(vis[N][M]) break;
			for(i = 1; i <= N; i++) for(j = 1; j <= M; j++) if(!vis[i][j] && d[i][j] < 1){
				mi = i; mj = j;
			}
			vis[mi][mj] = 1;
			for(w = 0; w < 4; w++){
				ni = mi + wi[w];
				nj = mj + wj[w];
				if(ni < 1 || nj < 1 || ni > N || nj > M) continue;
				// ������ continue
				// 1. ���ʿ� ������ ����ĭ..
				if(ceil[ni][nj] - floor[ni][nj] < 50) continue;
				// 2. ���� floor�� �ʹ� ���� ������ ceil�� �ʹ� ����..
				if(ceil[ni][nj] - floor[mi][mj] < 50) continue;
				// 3. ���� ceil�� �ʹ� ���� ������ floor�� �ʹ� ����..
				if(ceil[mi][mj] - floor[ni][nj] < 50) continue;
				// 4. �̹� �������������� �� �����
				if(H <= ceil[ni][nj] - 50) d[ni][nj] = 0;
				// 5. �ƴϸ� ��
				else continue;
			}
		}
		for(i = 1; i <= N; i++) for(j = 1; j <= M; j++) vis[i][j] = 0;

		for(k = N * M; k >= 1; k--)
		{
			if(vis[N][M]) break;
			min = DB_MAX + 1;
			for(i = 1; i <= N; i++) for(j = 1; j <= M; j++) if(!vis[i][j] && min > d[i][j]){
				min = d[i][j]; mi = i; mj = j;
			}
			vis[mi][mj] = 1;
			for(w = 0; w < 4; w++){
				ni = mi + wi[w];
				nj = mj + wj[w];
				if(ni < 1 || nj < 1 || ni > N || nj > M) continue;
				// ������ continue
				// 1. ���ʿ� ������ ����ĭ..
				if(ceil[ni][nj] - floor[ni][nj] < 50) continue;
				// 2. ���� floor�� �ʹ� ���� ������ ceil�� �ʹ� ����..
				if(ceil[ni][nj] - floor[mi][mj] < 50) continue;
				// 3. ���� ceil�� �ʹ� ���� ������ floor�� �ʹ� ����..
				if(ceil[mi][mj] - floor[ni][nj] < 50) continue;
				// 4. water level�� �̹� ���Ƽ� �������������� �� �����
				if(H - d[mi][mj] * 10 <= ceil[ni][nj] - 50) curr_time = d[mi][mj];
				// 5. �ƴϸ� ��޷� ^^
				else curr_time = d[mi][mj] + ((H - d[mi][mj] * 10) - (ceil[ni][nj] - 50)) / 10.0;

				// 6. ī�� ��? �ȵ�?
				if(H - curr_time * 10 - floor[mi][mj] >= 20){
					if(d[ni][nj] > curr_time + 1) d[ni][nj] = curr_time + 1;
				}
				else {
					if(d[ni][nj] > curr_time + 10) d[ni][nj] = curr_time + 10;
				}
			}

		}
		printf("Case #%d: %.6lf\n", t, d[N][M]);
	}
	return 0;
}