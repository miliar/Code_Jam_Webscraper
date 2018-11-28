#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

char a[102][102];
int match[102];
int w[102];
float wp[102];
float owp[102];
float oowp[102];
            
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,n;
    cin>>T;
    for(int tt=1;tt<=T;tt++){
            cin>>n;

            for(int i=0;i<n;i++){
                    match[i]=0;
                    w[i]=0;
                    for(int j=0;j<n;j++){
                            cin>>a[i][j];
                            if(a[i][j]=='1'){
                                             match[i]=match[i]+1;
                                             w[i]=w[i]+1;
                            } else if(a[i][j]=='0'){
                                   match[i]++;
                            }
                    }
                    wp[i]=((float)w[i])/((float)match[i]);
            }
            for(int i=0;i<n;i++){
                    owp[i]=0;
                    for(int j=0;j<n;j++){
                            if(a[i][j]=='0'){
                                             owp[i]+=((float)(w[j]-1))/((float)(match[j]-1));
                            } else if(a[i][j]=='1'){
                                                    owp[i]+=((float)w[j])/((float)(match[j]-1));}
                    }
                    owp[i]=owp[i]/((float)match[i]);
            }
            for(int i=0;i<n;i++){
                    oowp[i]=0;
                    for(int j=0;j<n;j++){
                            if((a[i][j]=='0')||(a[i][j]=='1')){
                                                               oowp[i]+=owp[j];
                            }
                    }
                    oowp[i]=oowp[i]/((float)match[i]);
            }
            printf("Case #%d:\n",tt);
            for(int i=0;i<n;i++){
                    printf("%f\n",((0.25*wp[i])+(0.5*owp[i])+(0.25*oowp[i])));
            }
    }
    return 0;        
}
