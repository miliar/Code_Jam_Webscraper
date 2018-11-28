#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int n, t[200], sco[200][200], win[200];
char s[200][200];
double wp[200], owp[200], oowp[200];

int main() {
    //freopen("d:\\in.txt","r",stdin);
    //freopen("d:\\out.txt","w",stdout);
	// freopen("d:\\A-small-attempt0.in","r",stdin);freopen("d:\\A-small-attempt0.out","w",stdout);
	//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	  freopen("d:\\A-large.in","r",stdin);freopen("d:\\A-large.out","w",stdout);
	int cse, i, j, g = 1;
	scanf("%d", &cse);
	while(cse--) {
        scanf("%d", &n);
        memset(t, 0, sizeof(t));
        memset(win, 0, sizeof(win));
        for(i = 0; i < n; ++i) {
            scanf("%s", s[i]);
            for(j = 0; j < n; ++j) {
                if(s[i][j] == '.') {
                    sco[i][j] = -1;
                }
                else {
                    t[i]++;
                    if(s[i][j] == '0') {
                        sco[i][j] = 0;
                    }
                    else {
                        sco[i][j] = 1;
                        win[i]++;
                    }
                }
            }
            wp[i] = 1.0*win[i] / (1.0 * t[i]);
            //printf("~%g\n", wp[i]);
        }
        for(i = 0; i < n; ++i) {
            int nn = 0;
            double ss = 0.0;
            for(j = 0; j < n; ++j) {
                if(i == j) continue;
                if(~sco[i][j]) {
                    ss += (1.0 * (win[j] - sco[j][i]) / (1.0 * (t[j] - 1)));
                    nn++;
                }
            }
            owp[i] = ss / (1.0 * nn);
        }
        for(i = 0; i < n; ++i) {
            int nn = 0;
            double ss = 0.0;
            for(j = 0; j < n; ++j) {
                if(~sco[i][j]) {
                    ss += owp[j];
                    nn++;
                }
            }
            oowp[i] = ss / (1.0 * nn );
        }
        printf("Case #%d:\n", g++);
        for(i = 0; i < n; ++i) printf("%.7lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
    }
    //system("PAUSE");
	return 0;
}
