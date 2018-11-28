/*#include<stdio.h>
#define FILENAME "small"
int T, M, N;
char inp_grid[520][520];
int grid[520][520];
int answer[520];
void gridClear(int si, int ei, int sj, int ej)
{
	int i, j;
	for(i=si;i<=ei;i++) for(j=sj;j<=ej;j++){
		grid[i][j] = -1;
	}
}
bool can_make_chess(int si, int sj, int ei, int ej)
{
	if(si<1 || sj<1 || ei>M || ej>N) return false;
	int i, j;
	for(i=si;i<=ei;i++) for(j=sj;j<=ej;j++){
		if(grid[i][j] == -1) return false;
		if(j!=sj && grid[i][j] == grid[i][j-1]) return false;
		if(i!=si && grid[i][j] == grid[i-1][j]) return false;
	}
	return true;
}
int main()
{
	freopen(FILENAME ".in","r",stdin);
	freopen(FILENAME ".out","w",stdout);
	int t, i, j, k, min, size, outputCount;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d %d",&M,&N);
		for(i=1;i<=M;i++){
			scanf("%s",inp_grid[i]);
			for(j=0;j<N/4;j++)
			{
				if('0' <= inp_grid[i][j] && inp_grid[i][j] <= '9') k = inp_grid[i][j] - '0';
				else k = inp_grid[i][j]-'A'+10;
				grid[i][j*4+1] = ((k>>3) & 1);
				grid[i][j*4+2] = ((k>>2) & 1);
				grid[i][j*4+3] = ((k>>1) & 1);
				grid[i][j*4+4] = (k & 1);
			}
		}


		if(M<N) size = M;
		else size = N;

		int si, ei, sj, ej;
		outputCount = 0;
		for(;size>=1;size--)
		{
			answer[size] = 0;
			for(i=1;i<=M;i++) for(j=1;j<=N;j++)
			{
				if(grid[i][j] == -1) continue;
				si = i-size+1; ei = i;
				sj = j-size+1; ej = j;
				if(can_make_chess(si,sj,ei,ej)){
					answer[size]++;
					gridClear(si,ei,sj,ej);
				}
			}
			if(answer[size]) outputCount ++;
		}

		printf("Case #%d: %d\n",t,outputCount);
		
		if(M<N) size = M;
		else size = N;
		for(;size>=1;size--){
			if(answer[size]) printf("%d %d\n",size,answer[size]);
		}
	}

	return 0;
}

*/

#include<stdio.h>
#define FILENAME "large"
int T, M, N;
char inp_grid[520][520];
int grid[520][520];
int topBottomMax[520][520];
int squareMax[520][520];
int answer[520];
void gridClear(int si, int ei, int sj, int ej)
{
	int i, j;
	for(i=si;i<=ei;i++) for(j=sj;j<=ej;j++){
		grid[i][j] = -1;
	}
}
bool check(int si, int ei, int sj, int ej)
{
	int i, j;
	for(i=si;i<=ei;i++) for(j=sj;j<=ej;j++){
		if(grid[i][j] == -1) return true;
	}
	return false;
}
int main()
{
	freopen(FILENAME ".in","r",stdin);
	freopen(FILENAME ".out","w",stdout);
	int t, i, j, k, min, size;
	int outputCount;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d %d",&M,&N);
		for(i=1;i<=M;i++){
			scanf("%s",inp_grid[i]);
			for(j=0;j<N/4;j++)
			{
				if('0' <= inp_grid[i][j] && inp_grid[i][j] <= '9') k = inp_grid[i][j] - '0';
				else k = inp_grid[i][j]-'A'+10;
				grid[i][j*4+1] = ((k>>3) & 1);
				grid[i][j*4+2] = ((k>>2) & 1);
				grid[i][j*4+3] = ((k>>1) & 1);
				grid[i][j*4+4] = (k & 1);
			}
		}

		for(i=1;i<=M;i++) for(j=1;j<=N;j++)
		{
			topBottomMax[i][j] = 1;
			for(k=i-1;k>=1;k--)
			{
				if(grid[k][j] != grid[k+1][j]) topBottomMax[i][j] ++;
				else break;
			}

			squareMax[i][j] = 1;
			min = topBottomMax[i][j];
			if(i==6 && j==19){
				i=i;
			}
			for(k=1;k<j;k++)
			{
				min = min > topBottomMax[i][j-k] ? topBottomMax[i][j-k] : min;
				if(grid[i][j-k] != grid[i][j-k+1] && min >= k+1) squareMax[i][j] = k+1;
				else break;
			}
		}

		if(M<N) size = M;
		else size = N;

		int si, ei, sj, ej;
		outputCount = 0;
		for(;size>=1;size--)
		{
			answer[size] = 0;
			for(i=1;i<=M;i++) for(j=1;j<=N;j++)
			{
				if(squareMax[i][j] < size) continue;
				if(grid[i][j] == -1) continue;
				si = i-size+1; ei = i;
				sj = j-size+1; ej = j;
				if(si < 1 || sj < 1 || ei > M || ej > N) continue;
				if(grid[si][sj] == -1 || grid[si][ej] == -1 || grid[ei][sj] == -1 || grid[ei][ej] == -1) continue;
				if(check(si,sj,ei,ej)){
					i=i;
				}
				answer[size]++;

				gridClear(si,ei,sj,ej);
			}
			if(answer[size]) outputCount ++;
		}

		printf("Case #%d: %d\n",t,outputCount);
		
		if(M<N) size = M;
		else size = N;
		for(;size>=1;size--){
			if(answer[size]) printf("%d %d\n",size,answer[size]);
		}
	}

	return 0;
}