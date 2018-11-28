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

using namespace std;

typedef pair<int,int>PII;
typedef pair<PII,int>PII2;


char in[105];
int pos[105];

int OO[105],numO;
int BB[105],numB;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int Test;
    int n;
    scanf("%d",&Test);
    for(int t=0;t<Test;t++){
        scanf("%d",&n);
        int time=0;
        int O=1,B=1;
        for(int i=0;i<n;i++) scanf(" %c %d",&in[i],&pos[i]);
        
        numB=numO=0;
        for(int i=0;i<n;i++){
            if(in[i]=='O') OO[numO++]=pos[i];
            else BB[numB++]=pos[i];
        }
        int x=0,y=0;
        int dis=0,move;
        
        
        for(int i=0;i<n;i++){
            if(in[i]=='O'){
                move=abs(OO[x]-O)+1;
                time+=move;
                O=OO[x++];
                dis=abs(BB[y]-B);
                if(B>=BB[y]) B-=min(dis,move);
                else B+=min(dis,move);
            } else {
                move=abs(BB[y]-B)+1;
                time+=move;
                B=BB[y++];
                dis=abs(OO[x]-O);
                if(O>OO[x]) O-=min(dis,move);
                else O+=min(dis,move);
                
            }
        }
        printf("Case #%d: %d\n",t+1,time);

        
    }
return 0;
}
