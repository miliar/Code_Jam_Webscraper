#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

const int maxn = 110;

char mat[maxn][maxn];
double wp[maxn];
double owp[maxn];
double oowp[maxn];
double ans[maxn];
int n;

void Cal1(){
    for(int i = 0; i < n; i ++){
        int cnt1 = 0;
        int cnt2 = 0;
        for(int j = 0; j < n; j ++){
            if(mat[i][j] == '0')
                cnt2 ++;
            if(mat[i][j] == '1')
                cnt1 ++, cnt2 ++;
        }
//        cout << cnt1 << " " << cnt2 << endl;
        wp[i] = cnt1 * 1.0 / cnt2;
    }
}

void Cal2(){
    for(int i = 0; i < n; i ++){
        int cnt = 0;
        double sum = 0.0;
        for(int j = 0; j < n; j ++){
            if(j == i)
                continue;
            if(mat[i][j] == '.')
                continue;
            cnt ++;
            int cnt1 = 0;
            int cnt2 = 0;
            for(int k = 0; k < n; k ++){
                if(k == i)
                    continue;
                if(mat[j][k] == '0')
                    cnt2 ++;
                if(mat[j][k] == '1')
                    cnt1 ++, cnt2 ++;
            }
            sum += cnt1 * 1.0 / cnt2;
        }
        owp[i] = sum / cnt;
    }
}

void Cal3(){
    for(int i = 0; i < n; i ++){
        double sum = 0.0;
        int cnt = 0;
        for(int j = 0; j < n; j ++){
            if(i == j )
                continue;
            if(mat[i][j] == '.')
                continue;
            cnt ++;
            sum += owp[j];
        }
        oowp[i] = sum / cnt;
    }
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t ++){
        cin >> n;
        for(int i = 0; i < n; i ++){
            scanf("%s", mat[i]);
        }

        Cal1();
        Cal2();
        Cal3();

        for(int i = 0; i < n; i ++){
            ans[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
        }

//        cout << wp[0] << endl;
//        cout << owp[0] << " " << owp[1] << " " << owp[2] << " " << owp[3] << endl;
        printf("Case #%d:\n", t);
        for(int i = 0; i < n; i ++){
            printf("%.9lf\n", ans[i]);
        }
    }

    return 0;
}
