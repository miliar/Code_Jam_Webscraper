#include <cstdio>
#define N 4
#define DIR 10
enum ChrType {
	T_X,
	T_O,
	T_T,
	T_DOT
};
using namespace std;

char str[4][10];
int dirr[] =	{0, 0, 0, 0, 1, 1, 1, 1, 1, -1};
int dirc[] =	{1, 1, 1, 1, 0, 0, 0, 0, 1, 1};
int startr[] =	{0, 1, 2, 3, 0, 0, 0, 0, 0, 3};
int startc[] =	{0, 0, 0, 0, 0, 1, 2, 3, 0, 0};

int main() {
	int t,tc;
	int i,d;
	int cr, cc;
	scanf("%d\n", &tc);
	for(t=0;t<tc;t++) {
		for(i=0;i<N;i++)
			scanf("%s\n", str[i]);
		scanf("\n");
		bool has_dots = false;
		bool win_X = false;
		bool win_O = false;
		
		for(d=0;d<DIR;d++) {
			int cr = startr[d]; 
			int cc = startc[d];
			int cnt[4] = {0};
			for(int i=0; i<N; i++) {
				switch(str[cr][cc]) {
					case 'X': cnt[T_X]++; break;
					case 'O': cnt[T_O]++; break;
					case 'T': cnt[T_T]++; break;
					case '.': cnt[T_DOT]++; break;
				}
				cr += dirr[d];
				cc += dirc[d];
			}

			if(cnt[T_DOT] > 0) {
				has_dots = true;
				continue;
			}
			
			if(cnt[T_X] + cnt[T_T] == 4)
				win_X = true;
			if(cnt[T_O] + cnt[T_T] == 4)
				win_O = true;
		}
		
		printf("Case #%d: ", t+1);
		if(win_X && !win_O) 
			printf("X won\n");
		else if(win_O && !win_X)
			printf("O won\n");
		else if(has_dots)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	return 0;
}
