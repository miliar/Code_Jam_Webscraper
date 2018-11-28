#include <stdio.h>
#include <assert.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

int T[101];
int M[31][11];
int MS[31][11];
int Memo[101][101];

int main(){
	freopen("B.in", "r",stdin);
	freopen("B.out","w",stdout);
	int ans,N,S,p,s,i,j,z,TST,tst=0;
    bool b0, b1;
    
    for(i=0;i<=10;++i){
      for(j=i;j<min(11,i+3);++j){
        for(z=j;z<min(11,i+3);++z){
          if(abs(i-j)==2||abs(i-z)==2||abs(j-z)==2){
            ++MS[i+j+z][z];
            //fprintf(stderr,"%d %d\n",i+j+z,max(i,max(j,z)));  
          }            
          if(abs(i-j)<2&&abs(i-z)<2&&abs(j-z)<2){
            ++M[i+j+z][z];  
            //fprintf(stderr,"-> %d %d\n",i+j+z,max(i,max(j,z)));  
          }            
        }
      }
    }
    
	scanf("%d",&TST);
	while(TST--){
		scanf("%d %d %d",&N,&S,&p);
		for(i=0;i<N;++i)scanf("%d",&T[i]);
    
        for(i=0;i<=N;++i)for(j=0;j<=S;++j)Memo[i][j]=0;    
    
        ans=0;
        for(i=1;i<=N;++i){
            for(j=p,b0=false;j<=10;++j){
                if(!M[T[i-1]][j])continue;
                b0=true; break;
            }
            for(j=p,b1=false;j<=10;++j){
                if(!MS[T[i-1]][j])continue;
                b1=true; break;
            }
            //fprintf(stderr,"%d %d\n",int(b0),int(b1));
            for(s=0;s<=S;++s){
                Memo[i][s]=Memo[i-1][s];
                if(b0){
                    Memo[i][s]=max(Memo[i][s],
                                   Memo[i-1][s]+1);
                }
                if(b1&&s>0){
                    Memo[i][s]=max(Memo[i][s],
                                   Memo[i-1][s-1]+1);
                }
                //fprintf(stderr,"%d\n",Memo[i][s]);
            }
        }
		printf("Case #%d: %d\n",++tst,Memo[N][S]);
		//fprintf(stderr,"Case #%d: %d\n",tst,Memo[N][S]);
	}
	return 0;
}
