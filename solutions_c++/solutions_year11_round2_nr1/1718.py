#include<iostream>
#include<string>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int T,N;
    int i, j, k;
    double WP[100], OWP[100], OOWP[100];
    string game[100];
    double win[100], lose[100];
    double temp;
    cin>>T;
    for(i = 1; i <= T; i++){
          cin>>N;
          for(j = 0; j < N; j++){
                cin>>game[j];
          }
          for(j = 0; j < N; j++){
                win[j] = 0;
                lose[j] = 0;
                for(k = 0; k < N; k++){
                      if(game[j][k] == '0')
                                    lose[j]++;
                      else if(game[j][k] == '1')
                                         win[j]++;
                }
                WP[j] = win[j] / (win[j] + lose[j]);
          }
          for(j = 0; j < N; j++){
                OWP[j] = 0;
                for(k = 0; k < N; k++){
                      temp = WP[k];
                      if(game[j][k] != '.'){
                                    if(game[j][k] == '1'){
                                                  temp = win[k]  / (lose[k] + win[k] - 1);
                                    }
                                    else{
                                                  temp = (win[k] - 1) / (lose[k] + win[k] - 1);
                                    }
                                    OWP[j] += temp;
                      }
                }
                OWP[j] = OWP[j] / (win[j] + lose[j]);
          }
          for(j = 0; j < N; j++){
                OOWP[j] = 0;
                for(k = 0; k < N; k++){
                      if(game[j][k] != '.'){
                                    OOWP[j] += OWP[k];
                      }
                }
                OOWP[j] = OOWP[j] / (win[j] + lose[j]);
          }
          cout<<"Case #"<<i<<":"<<endl;
          for(j = 0; j < N; j++){
                cout<<(WP[j]*0.25 + OWP[j]*0.5 + OOWP[j]*0.25)<<endl;     
          }
    }
    return 0;
}
