#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <vector>

using namespace std;
const int Max = 128;
char mp[Max][Max];
int Total[Max];
double WP[Max],nWP[Max][Max];
double OWP[Max],OOWP[Max];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t = 1;t <= T;t++){
        int N;
        scanf("%d",&N);
        for (int i = 0;i < N;i++){
            scanf("%s",mp[i]);
            WP[i] = 0;
            Total[i] = 0;
            for (int j = 0;j < N;j++)
                if (mp[i][j] != '.'){
                    if (mp[i][j] == '1')
                        ++WP[i];
                    ++Total[i];
                }
            for (int j = 0;j < N;j++)
                if (mp[i][j] != '.')
                    nWP[i][j] = (WP[i]-(mp[i][j] == '1')) / (Total[i]-1);
            WP[i] /= Total[i];
        }
        for (int i = 0;i < N;i++){
            OWP[i] = 0;
            for (int j = 0;j < N;j++)
                if (mp[i][j] != '.')
                    OWP[i] += nWP[j][i];
            OWP[i] /= Total[i];
        }
        printf("Case #%d:\n",t);
        for (int i = 0;i < N;i++){
            OOWP[i] = 0;
            for (int j = 0;j < N;j++)
                if (mp[i][j] != '.')
                    OOWP[i] += OWP[j];
            OOWP[i] /= Total[i];
            double R = 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
            printf("%.9f\n",R);//,WP[i],OWP[i],OOWP[i]);
        }
    }
    fclose(stdout);
	return 0;
}
