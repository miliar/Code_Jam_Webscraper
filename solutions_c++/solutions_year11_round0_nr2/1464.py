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

int C,D,N;

char inC[40][5];
char inD[40][5];

char p[105];

list<char>L;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int Test;
    scanf("%d",&Test);
    for(int t=0;t<Test;t++){
        L.clear();
        scanf("%d",&C);
        for(int i=0;i<C;i++) scanf("%s",inC[i]);
        scanf("%d",&D);
        for(int i=0;i<D;i++) scanf("%s",inD[i]);
        scanf("%d",&N);
        scanf("%s",p);
        
        
        list<char>::iterator p1,p2,p3;
        int ch=1;
        
        for(int i=0;i<N;i++){
            ch=0;
            L.push_back(p[i]);
            if(L.size()>1){
                p2=p1=L.end();    
                p1--;
                p2--;
                p1--;
                
                for(int j=0;j<C;j++){
                    if((*p1==inC[j][0] && *p2==inC[j][1]) || (*p1==inC[j][1] && *p2==inC[j][0])){
                        L.insert(p1,inC[j][2]);
                        L.erase(p1);
                        L.erase(p2);
                        ch=1;
                        break;
                    }
                }
                if(ch) continue;
                p1=L.begin();
                
                while(p1!=p2){
                    for(int j=0;j<D;j++){
                    if((*p1==inD[j][0] && *p2==inD[j][1]) || (*p1==inD[j][1] && *p2==inD[j][0])){
                        L.clear();
                        ch=1;
                        break;
                    }
                    }
                    if(ch) break;
                    p1++;
                }
            }
        }       
        int ss=L.size();
        printf("Case #%d: ",t+1);
        if(ss==0) printf("[]");
        else {
            printf("[");
            for(p1=L.begin();p1!=L.end();p1++){
                printf("%c",*p1);
                p2=p1;
                p2++;
                if(p2!=L.end()) printf(", ");
            }
            printf("]");
        }
        printf("\n"); 
    }
return 0;
}
