#include <stdio.h>
#include <vector>
#include<string>
#include <set>

using namespace std;

int qq;
int memo[101][1001];
vector<string> sarch;
vector<string> que;


int bt(int se,int act, int c){
     if(act==qq)
          return 0;
     if(memo[se][act]!=-1) return memo[se][act];
   
     if(sarch[se]==que[act]){ 
                               int min=200000;
                                int i; 
                                for(i=0;i<sarch.size();i++) if(i!=se){ int t=bt(i,act+1,c+1); if(t<min) min=t; }
                                memo[se][act]=min+1;
                                return min+1;
                                }  

     int x=bt(se,act+1,c);
     memo[se][act]=x;
     return x;
     
}

int main(){
 //   freopen("hola.txt","w",stdout);
//    freopen("hola2.txt","r",stdin);
    int n,s,q,i,j,k,z;
    scanf("%d", &n);
    
    for(z=0;z<n;z++){                   
        sarch.clear(); que.clear();        
        scanf("%d\n",&s);
        memset(memo,-1,sizeof(memo));
        for(i=0;i<s;i++){ 
                          char t; j=0; 
                          char tmp[110]={}; 
                          do{  
                               scanf("%c", &t); 
                                   if(t=='\n') 
                                       break; 
                               tmp[j++]=t;
        
                          }while(t!='\n');  

                          sarch.push_back(tmp);         }
        
 //       for(i=0;i<s;i++)printf("%s\n", search[i].c_str()); printf("\n");

        scanf("%d\n",&q);        
        for(i=0;i<q;i++){ char t; j=0; char tmp[110]={}; do{  scanf("%c", &t); if(t=='\n') break; tmp[j++]=t; }while(t!='\n');  que.push_back(tmp);         }
        qq=q;
   //     for(i=0;i<q;i++)printf("%s\n", que[i].c_str()); printf("\n");
        
        int min=2000000;
        for(i=0;i<s;i++){ int r=bt(i,0,0); if(r<min) min=r; }        
        printf("Case #%d: %d\n", z+1,min);
 
    }
    
    system("pause");
//    fclose(stdout);
//    fclose(stdin);
     return 0;   
    
}
