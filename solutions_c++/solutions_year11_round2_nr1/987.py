#include <stdio.h>
#include <iostream>
#include <cstring>

using namespace std;

typedef long double real;
int n;
char vs[128][128];

int vs_team_win[128];
int vs_team_count[128];

real wp[128];
real owp[128];
real oowp[128];

#define D if(0)

int main(int argc, char const* argv[])
{
	int case_count;
	scanf("%d", &case_count);
	for (int case_id = 0; case_id < case_count; case_id++) {
		printf("Case #%d:\n", case_id + 1);
		scanf("%d", &n);
		memset(vs_team_count, 0, sizeof(vs_team_count));
		memset(vs_team_win, 0, sizeof(vs_team_win));

		for (int y = 0; y < n; y++) {
			for (int x = 0; x < n; x++) {
				char c;
				scanf(" %c", &c);
				vs[y][x] = c;
				switch (c) {
				case '1':
					vs_team_win[y]++;
				case '0':
					vs_team_count[y]++;
				}
			}
			wp[y] = (real)vs_team_win[y] / vs_team_count[y];
			D printf("wp[%d]=%Lf\n",y, wp[y]);
		}

		// owp
		for (int i = 0; i < n; i++) {
			real owp_i = 0;
			// team i
			for (int oppo = 0; oppo < n; oppo++) {
				if (vs[i][oppo] != '.') {
					owp_i += 
						(real)(vs_team_win[oppo] - (vs[oppo][i] == '1' ? 1 : 0)) 
						/ (vs_team_count[oppo] - 1);
				}
			}
			owp[i] = owp_i / vs_team_count[i];
			D printf("owp[%d]=%Lf\n",i , owp[i]);
		}

		// oowp
		for (int i = 0; i < n; i++) {
			real oowp_i = 0;
			for (int oppo = 0; oppo < n; oppo++) {
				if (vs[i][oppo] != '.') oowp_i += owp[oppo];
			}
			oowp[i] = oowp_i / vs_team_count[i];
			D printf("oowp[%d]=%Lf\n",i , oowp[i]);
		}

		// output
		for (int i = 0; i < n; i++) {
			printf("%.12Lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
		}
	}
	return 0;
}
