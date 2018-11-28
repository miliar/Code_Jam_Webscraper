#include<stdio.h>
#include<string.h>
#include<vector>
#include<math.h>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<conio.h>
using namespace std;
#define MAX 55
#define valid(a,b) (a>=0 && a<r && b<c && b>=0 && mat[a][b]=='#')
char mat[MAX][MAX];
int r,c;
bool check(int a,int b){
    if(valid(a,b)) mat[a][b]='/';
    else return false;
    
    if(valid(a,b+1)) mat[a][b+1]=92;
    else return false;
    
    if(valid(a+1,b)) mat[a+1][b]=92;
    else return false;
    
    if(valid(a+1,b+1)) mat[a+1][b+1]='/';
    else return false;
    
    return true;
}
void slash(){
    int i,j,add=0;
    bool fou=true;
    for(i=0;i<r;i++){
           for(j=0;j<c;j++){
                        if(mat[i][j]=='#'){
                             if(check(i,j)) continue;
                             else {
                                 fou=false;
                                 break;
                             }
                        }
           }
           if(fou==false) break;
       }
       if(fou==false){
            printf("Impossible\n");
       	//for(i=0;i<r;i++)
            //        printf("%s\n",mat[i]);
       }
       else{
              for(i=0;i<r;i++)
                    printf("%s\n",mat[i]);
       }
}
int main(){
    int t,i,j,k=0;
    //freopen("A-small.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d%d",&r,&c);
        for(i=0;i<r;i++) scanf("%s",mat[i]);
        printf("Case #%d:\n",++k);
        slash();    
    }
    getch();
    return 0;    
}
