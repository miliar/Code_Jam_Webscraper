#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<cstring>
using namespace std;

char w[200][200];
double wp[200],wp2[200][200],owp[200],oowp[200];
//wp2[i][j] := team i's wp without playing wf team j
int main(){
        int t,cnt = 1;
        scanf("%d", &t);
        while(t--){
                int n;
                scanf("%d", &n);
                for(int i=0; i<n;i++){
                        getchar();
                        double tot = 0,win = 0;
                        for(int j=0;j<n;j++){
                                w[i][j] = getchar();
                                if(w[i][j]!='.') tot++;
                                if(w[i][j]=='1') win++;
                        }
                        wp[i] = win/tot;
                        for(int j=0; j<n;j++){
                                double tot2=0, win2 = 0;
                                for(int k=0; k < n;k++){
                                        if(k==j) continue;
                                        if(w[i][k]!='.') tot2++;
                                        if(w[i][k]=='1') win2++;
                                }
                                wp2[i][j] = win2/tot2;
                        }
                }
                for(int i=0; i<n;i++){
                        double sum_wp2 = 0, tot3 = 0;
                        for(int j=0; j<n;j++){
                                if(i==j) continue;
                                if(w[j][i]!='.') {tot3++;sum_wp2 += wp2[j][i];}
                        }
                        owp[i] = sum_wp2 / tot3;
                }

                for(int i=0; i<n;i++){
                        double sum_wp3=0,tot4=0;
                        for(int j=0; j<n;j++){
                                if(w[i][j]!='.') {tot4++; sum_wp3+= owp[j];}
                        }
                        oowp[i] = sum_wp3/tot4;
                }
                printf("Case #%d:\n", cnt++);
                for(int i=0; i<n;i++)
                        printf("%.12f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25*oowp[i]);
        }
        return 0;
}
