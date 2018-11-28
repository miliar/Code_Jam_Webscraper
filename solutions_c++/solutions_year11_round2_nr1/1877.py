#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int n, t;
int Case = 0;
char M[100][105];
char c;

int win[100], win2[100];
int los[100], los2[100];
double WP[100], OWP[100], OOWP[100], RPI[100];

int main() {
	scanf("%d", &t);
	while(t--) {
        ++Case;
		scanf("%d", &n);
        for(int i = 0; i < n; ++i) {
            scanf("%s\n", M[i]);
            //printf("%s\n", M[i]);
        }
        
        for(int i = 0; i < n; ++i) {
            win[i] = los[i] = 0;
            for(int j = 0; j < n; ++j) {
                if(M[i][j] == '1') ++win[i];
                else if(M[i][j] == '0') ++los[i];
            }
            WP[i] = ((double)win[i] / (win[i] + los[i]));
            //printf("WP[%d]=%f\n", i, WP[i]);
        }

        for(int i = 0; i < n; ++i) {
            int cnt = 0; OWP[i] = 0.0;
            int wi, lo;
            for(int j = 0; j < n; ++j) {
                if(j == i || M[i][j] == '.') continue;
                wi = win[j];
                lo = los[j];
                if(M[j][i] == '0') {
                    lo--;
                } else if(M[j][i] == '1') {
                    wi--;
                }
                OWP[i] += ((double)wi/(wi+lo));
                ++cnt;
            }
            OWP[i] /= cnt;
            //printf("OWP[%d]=%f\n", i, OWP[i]);
        }
        for(int i = 0; i < n; ++i) {
            double sum = 0.0; int cnt = 0;
            for(int j = 0; j < n; ++j) {
                if(j == i || M[i][j] == '.') continue;
                sum += OWP[j];
                ++cnt;
            }
            OOWP[i] = sum / cnt;
            //printf("OOWP[%d]=%f\n", i, OOWP[i]);
        }

        printf("Case #%d:\n", Case);
        for(int i = 0; i < n; ++i) {
            RPI[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
            printf("%.12f\n", RPI[i]);
        }

	}
	return 0;
}
