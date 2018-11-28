/*
    ID : ping128
    LANG : C++
*/
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <algorithm>

#define INF (1<<30)

using namespace std;

typedef pair<int,int>PII;
typedef pair<PII,int>PII2;


// first four directions + four diagonal directions + itself
int cx[]={-1,0,0,1,-1,-1,1,1,0},cy[]={0,-1,1,0,-1,1,1,-1,0};

int stdout1 = 0;

int Test;

int N;
char in[105][105];
int play[105];
int win[105];

double WP[105],OWP[105],OOWP[105];

int main(){

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout); stdout1 = 1;

    scanf("%d",&Test);
    for(int t=1;t<=Test;t++){
        // begin here
        scanf("%d",&N);
        for(int i=0;i<N;i++) scanf("%s",in[i]);
        for(int i=0;i<N;i++){
            play[i]=win[i]=0;
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(in[i][j]=='1'){
                    play[i]++;
                    win[i]++;
                } else if(in[i][j]=='0'){
                    play[i]++;
                }
            }
        }
        // output format
        printf("Case #%d:\n",t);
        for(int i=0;i<N;i++)
            WP[i]=OWP[i]=OOWP[i]=0.0;
        
        for(int i=0;i<N;i++){
            WP[i]=(double)win[i]/(double)play[i];
           // printf("%lf\n",WP[i]);
        }
        for(int i=0;i<N;i++){
            double num=0.0;
            for(int j=0;j<N;j++){
                if(in[i][j]!='.'){
                    double w=0,p=0;
                    num+=1.;
                    for(int k=0;k<N;k++){
                        if(k==i) continue;
                        if(in[j][k]=='1'){
                            p+=1.;
                            w+=1.;
                        } else if(in[j][k]=='0'){
                            p+=1.;
                        }
                    }
                    OWP[i]+=w/p;
                }
            }
            OWP[i]/=num;
      //      printf("-- %lf\n",OWP[i]);
        }
        for(int i=0;i<N;i++){
            double num=0.0;
            for(int j=0;j<N;j++){
                if(in[i][j]!='.'){
                    num+=1.;
                    OOWP[i]+=OWP[j];
                }
            }
            OOWP[i]/=num;
        }
        for(int i=0;i<N;i++){
            printf("%lf\n",0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
        }
     
    }

if(!stdout1) while(1);

return 0;
}
