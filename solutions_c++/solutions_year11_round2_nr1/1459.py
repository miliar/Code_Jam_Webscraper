#include <iostream>
using namespace std;
int main(){
    int a[105][105]={0},ntc,n;
    double wp[105],owp[105],oowp[105],total[105];
    cin >> ntc;
    for(int tc =1 ;tc<=ntc;tc++){
            cin >> n;
            char s;
            int i,j;
            for(i=1;i<=n;i++)
              wp[i]=owp[i]=oowp[i]=total[i]=0;
            for(i=1;i<=n;i++)
               for(j=1;j<=n;j++){
                  cin >> s;
                  if(s=='.')
                     a[i][j]=-1;
                  else {
                  total[i]=total[i]+1;
                  if(s=='1') a[i][j]=1,wp[i]=wp[i]+1;
                  else  a[i][j]=0;
                  }
                     
               }


            for(i=1;i<=n;i++){
                 double  tmp = 0 ;
                 for(j=1;j<=n;j++)
                    if(i!=j && a[i][j]>=0){
                       tmp=tmp + (wp[j]-a[j][i])/(total[j]-1);
             //          cout << j << " " << (wp[j]-a[j][i])/(total[j]-1) << endl;
                    }
                 owp[i] = tmp / total[i];
           //      cout << owp[i] <<" " << tmp <<" " << total[i] << endl;
            }
            for(i=1;i<=n;i++){
                 double  tmp = 0 ;
                 for(j=1;j<=n;j++)
                    if(i!=j && a[i][j]>=0)
                       tmp+=owp[j];
                 oowp[i] = tmp / total[i];
            }
            for(i=1;i<=n;i++)
                  wp[i]=wp[i]/total[i];
            printf("Case #%d:\n",tc);
            for(i=1;i<=n;i++){
                  double RPI = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
                  printf("%.12lf\n",RPI);
            }
    }
}

