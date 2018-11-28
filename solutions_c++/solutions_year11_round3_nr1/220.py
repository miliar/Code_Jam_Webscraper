#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>
#include<set>
#include<map>
#include<vector>
using namespace std;
char aa[100][100],bb[100][100];
bool used[100][100];
int n,m;
bool check(int i,int j){
     if(j+1>=m)return 0;
     if(i+1>=n)return 0;
     if(!aa[i][j]||!aa[i][j+1]||!aa[i+1][j]||!aa[i+1][j+1])return 0;   
     if(used[i][j]||used[i][j+1]||used[i+1][j]||used[i+1][j+1])return 0;
     used[i][j]=used[i][j+1]=used[i+1][j]=used[i+1][j+1]=1;
     bb[i][j]='/';
     bb[i][j+1]='\\';
     bb[i+1][j]='\\';
     bb[i+1][j+1]='/';
     return 1;
}
int main()
{
    freopen("A-large(2).in","r",stdin);
    freopen("a.big.out","w",stdout);
    int Total;
    int i,j;
    scanf("%d",&Total);
    for(int Case=1;Case<=Total;Case++){
        printf("Case #%d:\n",Case);
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                scanf(" %c",&aa[i][j]); 
                bb[i][j]=aa[i][j];
                if(aa[i][j]=='#')aa[i][j]=1;
                else aa[i][j]=0;                
            }                 
        }
        bool ok=1;
        memset(used,0,sizeof(used));
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                check(i,j);               
            }                 
        }
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if(aa[i][j]&&!used[i][j])ok=0;             
            }                 
        }
        if(!ok)puts("Impossible");
        else {
            for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                printf("%c",bb[i][j]);             
            }  puts("");               
        }     
        }
        
        
        
    }
        
}
