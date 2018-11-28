#include <iostream>
using namespace std;

int T,R,X1,Y1,X2,Y2;
int ca,ans,matrix[105][105],temp[105][105];

void trans(){
    int i,j;
    for(i=1;i<=100;i++){
        for(j=1;j<=100;j++){
            if(!matrix[i][j]){
                if(matrix[i-1][j]&&matrix[i][j-1]){
                    temp[i][j]=1;
                }
                else    temp[i][j]=0;
            }
            else{
                if(!matrix[i-1][j]&&!matrix[i][j-1]){
                    temp[i][j]=0;
                }
                else{
                    temp[i][j]=1;
                }
            }
        }
    }
    memcpy(matrix,temp,sizeof(temp));
}

bool check(){
    int i,j;
    for(i=1;i<=100;i++){
        for(j=1;j<=100;j++){
            if(matrix[i][j])    return false;
        }
    }
    return true;
}

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%d",&R);
        int i,j,k;
        memset(matrix,0,sizeof(matrix));
        for(i=1;i<=R;i++){
            scanf("%d%d%d%d",&X1,&Y1,&X2,&Y2);
            for(j=X1;j<=X2;j++){
                for(k=Y1;k<=Y2;k++){
                    matrix[k][j]=1;
                }
            }
        }
        for(ans=1;;ans++){
            trans();
            if(check()) break;
        }
        printf("Case #%d: %d\n",++ca,ans);
    }
    return 0;
}
        
