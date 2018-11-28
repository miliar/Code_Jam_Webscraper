#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#define eps 1e-8
#define oo 1e9


using namespace std;

int T, m, n, q, w, mi, ma, cnt, s, t, fi, cc, e, r, z, x, wincount, totalcount, play[110], playwin[110];
double win[110], owin[110], oowin[110];
char a[110][110], temp[10];

int main(){
	scanf("%d", &T);
	for (int rr=1; rr<=T; rr++){
		memset(a, 0, sizeof(a));
		memset(win, 0, sizeof(win));
		memset(owin, 0, sizeof(owin));
		memset(oowin, 0, sizeof(oowin));
		printf("Case #%d:\n", rr);
		scanf("%d", &m);
		gets(temp);
		for (int i=0; i<m; i++){
			gets(a[i]);
		}
		for (int i=0; i<m; i++){
			wincount = 0; totalcount = 0;
			for (int j=0; j<m; j++)
				if (a[i][j] == '1')
					wincount++, totalcount++;
				else if (a[i][j] == '0')
					totalcount++;
			play[i] = totalcount;
			playwin[i] = wincount;
			win[i] = (double)wincount/(double)totalcount;
		}

		for (int i=0; i<m; i++){
			double s = 0; int total = 0;
			for (int j=0; j<m; j++)
				if (a[i][j] != '.'){
					if (a[i][j] == '1')
						s += (double)playwin[j]/(double)(play[j]-1);
					else s += (double) (playwin[j]-1) / (double)(play[j]-1);
				}
			owin[i] = s/(double)play[i];
		}
		for (int i=0; i<m; i++){
			double s = 0; int total = 0;
			for (int j=0; j<m; j++)
				if (a[i][j] != '.')
					s += owin[j], total++;
			oowin[i] = s/(double)total;
		}
		for (int i=0; i<m; i++)
			printf("%.11f\n", 0.25*win[i] + 0.5*owin[i] + 0.25*oowin[i]);
	}
	return 0;
}
