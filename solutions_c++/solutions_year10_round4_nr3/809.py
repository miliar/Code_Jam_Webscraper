#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<stdlib.h>
#include<set>
#include<iostream>
#include<math.h>

#define INF 1000000000

using namespace std;

typedef long long lld;

int bb[155][155];

int aa[155][155];

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int N,x1,x2,y1,y2;
    int Case;
    scanf("%d",&Case);
    for(int test=0;test<Case;test++){
        scanf("%d",&N);
        for(int i=0;i<N;i++){
            scanf("%d %d %d %d",&y1,&x1,&y2,&x2);
            x1+=5;
            x2+=5;
            y1+=5;
            y2+=5;
            for(int q=x1;q<=x2;q++)
                for(int j=y1;j<=y2;j++)
                    bb[q][j]=1;
        }
        
        int time=0;
        while(1){
            int ch=1;
            for(int i=0;i<155;i++)
                for(int j=0;j<155;j++)
                    if(bb[i][j]) ch=0;
            if(ch) break;
            time++;
            for(int i=1;i<155;i++)
                for(int j=1;j<155;j++)
                    if(bb[i][j]==0){
                        if(bb[i-1][j] && bb[i][j-1]) aa[i][j]=1;
                        else aa[i][j]=0;
                    } else {
                        if(bb[i-1][j] || bb[i][j-1]) aa[i][j]=1;
                        else aa[i][j]=0;
                    }
            for(int i=1;i<155;i++)
                for(int j=1;j<155;j++)
                    bb[i][j]=aa[i][j];
            
        }
        printf("Case #%d: %d\n",test+1,time);
    }

}
