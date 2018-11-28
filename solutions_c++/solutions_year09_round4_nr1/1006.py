/*
   NAME : Siwakorn Srisakaokul
   ID : ping128
   LANG : C++
   CONTEST : CodeJam -- Round 2
   TASK : Crazy Rows
*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int R,T,ch,num;
    char in[100][100];
    char swap[100];
    scanf("%d",&T);
    for(int tt=0;tt<T;tt++){
        num=0;
        scanf("%d",&R);
        for(int i=0;i<R;i++) scanf("%s",in[i]);
        for(int i=0;i<R-1;i++){
            ch=1;
            for(int j=i+1;j<R;j++){
                if(in[i][j]=='1') ch=0;
            }
            if(ch) continue;
            else {
                for(int j=i+1;j<R;j++){
                    ch=1;
                    
                    for(int k=i+1;k<R;k++){
                        if(in[j][k]=='1'){ ch=0; break; }
                    }
                    if(ch){
                        for(int p=j-1;p>=i;p--){
                            for(int k=0;k<R;k++){ swap[k]=in[p][k]; in[p][k]=in[p+1][k]; }
                            for(int k=0;k<R;k++) in[p+1][k]=swap[k];
                            num++;
                        }
                        
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",tt+1,num);
    }
return 0;
}
