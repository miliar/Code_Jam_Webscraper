#include <cstdio>
#include <algorithm>
using namespace std;

const double eps = 1e-9;

int g[505][505];
int r, c, d;

int mymax(int d1, int d2){
	if (d1 > d2)
		return d1;
	return d2;
}

bool ugol(int xc, int yc, int dist, int i, int j){
	return (((i == xc - dist) && (j == yc - dist)) || 
			((i == xc - dist) && (j == yc + dist)) ||
			((i == xc + dist) && (j == yc - dist)) || 
			((i == xc + dist) && (j == yc + dist)));
}

bool goodfield(int xc, int yc, int dist){
	int x = 0, y = 0;
	int i, j;
	for (i = xc - dist;i < xc + dist + 1;i++){
		for (j = yc - dist;j < yc + dist + 1;j++){
			if (!ugol(xc, yc, dist, i, j)){
				x += g[i][j] * (i - xc);
				y += g[i][j] * (j - yc);
			}
		}
	}
	return ((x == 0) && (y == 0));
}

bool gdugol(int xl, int yl, int dist, int i, int j){
	return (((i == xl) && (j == yl)) ||
			((i == xl) && (j == yl + dist - 1)) ||
			((i == xl + dist - 1) && (j == yl)) ||
			((i == xl + dist - 1) && (j == yl + dist - 1)));
}

bool gdfield(int xl, int yl, int dist){
	double xc = xl + ((dist - 1) / 2.0), yc = yl + ((dist - 1) / 2.0);
	int i, j;
	double x = 0, y = 0;
	for (i = xl;i < xl + dist;i++){
		for (j = yl;j < yl + dist;j++){
			if (!gdugol(xl, yl, dist, i, j)){
				x += g[i][j] * (i - xc);
				y += g[i][j] * (j - yc);
			}
		}
	}
	return ((fabs(x) < eps) && (fabs(y) < eps));
}

int game(){
	int max = -1;
	int i, j, k, dim;
	for (i = 0;i < r;i++){
		for (j = 0;j < c;j++){
			dim = min(i + 1, j + 1);dim = min(dim, r - i);dim = min(dim, c - j);
			dim--;
			for (k = 0;(dim - k >= 1);k++){
				if (goodfield(i, j, dim - k)){
					break;
				}
			}
			if (dim - k >= 1){
				max = mymax(max, (dim - k) * 2 + 1);
			}
		}
	}
	for (k = 4;k <= min(r, c);k+=2){
		for (i = 0;i < r;i++){
			for (j = 0;j < c;j++){
				if ((i + k - 1 < r) && (j + k - 1 < c)){
					if ((k > max) && (gdfield(i, j, k))){
						max = k;
					}
				}
			}
		}
	}
	return max;
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test, t, i, j;
	char c1;
	scanf("%d",&test);
	for (t = 0;t < test;t++){
		if (t)
			printf("\n");
		printf("Case #%d: ",t + 1);
		scanf("%d%d%d\n",&r,&c,&d);
		for (i = 0;i < r;i++){
			for (j = 0;j < c;j++){
				scanf("%c",&c1);
				g[i][j] = d + (c1 - '0');
			}
			scanf("\n");
		}
		int vsp = game();
		if (vsp == -1){
			printf("IMPOSSIBLE");
		}else
		{
			printf("%d",vsp);
		}
	}
	return 0;
}