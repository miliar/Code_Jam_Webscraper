#include <cstdio>
#include <iostream>
#include <cstring>
#define N 110
using namespace std;
int matrix[N][N];
int win[N],lose[N];
double owp[N],rp[N];
int main()
{
    int t;
    freopen(".\\a.txt","r",stdin);
    freopen(".\\aout.txt","w",stdout);
    cin>>t;
    for(int cas = 1; cas <= t; ++cas){
        int n;
        cin>>n;
        getchar();
        memset(matrix,0,sizeof(matrix));
        memset(win,0,sizeof(win));
        memset(lose,0,sizeof(lose));
        for(int i = 1; i <= n; ++i){
            for(int j = 1; j <= n; ++j){
                char c = getchar();
                if(c == '.'){
                    matrix[i][j] = -1;
                }
                else if(c == '0'){
                    matrix[i][j] = 0;
                }
                else{
                    matrix[i][j] = 1;
                }
                //cout<<matrix[i][j];
            }
            getchar();
            //cout<<endl;
            for(int j = 1; j <= n; ++j){
                if(matrix[i][j] == 0){
                    ++lose[i];
                }
                else if(matrix[i][j] == 1){
                    ++win[i];
                }
            }
        }
        for(int i = 1; i <= n; ++i){
            rp[i] = (double)win[i]/(double)(lose[i]+win[i]);
            //cout<<i<<" "<<rp[i]<<endl;
            rp[i] *= 0.25;
            //cout<<win[i]<<" "<<lose[i]<<endl;
            double tmp = 0;
            for(int j = 1; j <= n; ++j){
                if(matrix[i][j] >= 0){
                    tmp = tmp + (double)(win[j] - matrix[j][i])/(double)(win[j] + lose[j] - 1);
                }
            }
            tmp = tmp / (double)(win[i]+lose[i]);
            owp[i] = tmp;
            rp[i] += owp[i]*0.5;
            //cout<<i<<" "<<owp[i]<<endl;
        }
        for(int i = 1; i <= n; ++i){
            double tmp = 0;
            for(int j = 1; j <= n; ++j){
                if(matrix[i][j] >= 0){
                    tmp += owp[j];
                }
            }
            tmp = tmp/(win[i]+lose[i]);
            rp[i] += tmp*0.25;
        }
        printf("Case #%d:\n",cas);
        for(int i = 1; i <= n; ++i){
            printf("%.8f\n",rp[i]);
        }
    }
    return 0;
}
