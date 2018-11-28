#include <algorithm>

using namespace std;
FILE *in, *out;

int main(){
	in = fopen("D.in", "r");
	out = fopen("D.out", "w");
	int n;
	fscanf(in, "%d", &n);
	int Map[102][102], Rest[102][102];
	int move[2][2] = {{-1, -2}, {-2, -1}};
	for(int t=1;t<=n;t++){
		int H, W, R;
		fscanf(in, "%d %d %d", &H, &W, &R);
		for(int i=1;i<=H;i++)
			for(int j=1;j<=W;j++){
				Map[i][j] = 0;
				Rest[i][j] = 0;
			}
		for(int i=0;i<R;i++){
			int x, y;
			fscanf(in, "%d %d", &x, &y);
			Rest[x][y] = 1;
		}
		Map[1][1] = 1;
		for(int i=1;i<=H;i++)
			for(int j=1;j<=W;j++){
				if(Rest[i][j]) continue;
				for(int k=0;k<2;k++){
					int x = i+move[k][0];
					int y = j+move[k][1];
					if(x < 1 || y < 1) continue;
					Map[i][j] = (Map[i][j] + Map[x][y]) % 10007;
				}
			}
		fprintf(out, "Case #%d: %d\n", t, Map[H][W]);
	}
	fclose(in);
	fclose(out);
	return 0;
}
