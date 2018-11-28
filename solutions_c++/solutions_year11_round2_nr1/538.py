#include <iostream>
#include <cstdio>
using namespace std;


int a[101][101];
double f[101], fp[101][101], fow[101], foow[101];
int n;

int main(){

    int ntest;

    cin >> ntest;
    
    for(int test=1;test<=ntest;test++){
        cin>>n;
        string st;
        for (int i=0;i<n;i++){
            cin>>st;
            for(int j=0;j<n;j++){
                if (st[j] == '.') a[i][j] = -1;
                else a[i][j] = (int)(st[j] - '0');
            }
        }

        for(int i=0;i<n;i++){
            int w = 0, t = 0;

            for(int j=0;j<n;j++){
                if (i!=j && a[i][j]>=0){
                    w += a[i][j];
                    t += 1;
                }
            }


            // winning percentage
            f[i] = (w*1.0)/t;

            // winning without counting j
            for(int j=0;j<n;j++){
                if (i!=j && a[i][j]>=0){
                    int wp = w - a[i][j];
                    fp[i][j] = (wp*1.0)/(t-1);
                }
            }
        }

        // computing owp
        for(int i=0;i<n;i++){
            double ow = 0;
            int t=0;
            for(int j=0;j<n;j++){
                if (i!=j && a[i][j]>=0){
                    ow += fp[j][i];
                    t += 1;
                }
            }
            fow[i] = ow / t;
        }

        // coputing oowp
        for(int i=0;i<n;i++){
            double oow = 0;
            int t=0;
            for(int j=0;j<n;j++){
                if (i!=j && a[i][j]>=0){
                    oow += fow[j];
                    t += 1;
                }
            }
            foow[i] = oow / t;
        }

        cout<<"Case #"<<test<<": "<<endl;
        // rpi
        for(int i=0;i<n;i++){
            double rpi = 0.25*f[i] + 0.5 * fow[i] + 0.25*foow[i];
            printf("%.9f\n",rpi);
        }
    }

    return 0;
}
