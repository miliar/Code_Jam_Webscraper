#include <iostream>
#include <algorithm>
#include <string>

#define INF 2000000000
//#define acc(mas,i,j,undef_val) ((i >= 0) && (i < H) && (j >= 0) && (j < W))? mas[i][j] : undef_val

using namespace std;

const int max_n = 400;

int att[max_n][max_n];
char bas[max_n][max_n];
int bss, H, W;
int di[4] = {-1,0,0,+1};
int dj[4] = {0,-1,+1,0};

int acc(int i,int j,int undef_val) {
	if ((i >= 0) && (i < H) && (j >= 0) && (j < W)) return att[i][j]; else return undef_val;
}
void xfill(int i, int j, char c){
	int ii, jj, min_att = INF; 
	for (int k = 0; k < 4; k++) min_att = min(min_att,acc(i + di[k],j + dj[k],INF));

	if (min_att >=  acc(i, j, INF) ) {
		if (bas[i][j] == 0) {
			bas[i][j] = c;
			bss++;
		}
		return ; 
	}
	for (int k = 0; k < 4; k++)
		if (min_att == acc(i + di[k],j + dj[k], INF)){
			ii = i + di[k]; jj = j + dj[k];
			break;
		}
	xfill(ii, jj, c);
	bas[i][j] = bas[ii][jj];
}

void sol(int num){
	bss = 0;
	cin >> H >> W;
	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++){
			scanf("%d",&att[i][j]);
			bas[i][j] = 0;
		}
	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++) if (bas[i][j] == 0) {
		xfill(i,j,'a' + bss);	
		}
	cout << "Case #" << num << ": " << endl;
	int j;
	for (int i = 0; i < H; i++){
		for (j = 0; j < W - 1; j++)
			printf("%c ",bas[i][j]);
		printf("%c\n",bas[i][j]);
	}
}


int main(){
	
	freopen("B-small.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
	
	int t, i;
	cin >> t;
	for (int i = 0; i < t; i++) sol(i + 1);


	fclose(stdin); fclose(stdout);
	return 0;
}