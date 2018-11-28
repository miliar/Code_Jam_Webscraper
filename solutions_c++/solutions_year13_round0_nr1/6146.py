#include<stdio.h>
#include<stdlib.h>
int n;
char a[5][5];
int check(int x,int y){

    if(x==0){
        int sum=0;
        for(int i=x;i<4;i++){
            if(a[i][y]==a[x][y]||a[i][y]=='T')sum++;
        }
        if(sum==4){
            if(a[x][y]=='X'||a[x+1][y]=='X')return 0;
            if(a[x][y]=='O'||a[x+1][y]=='O')return 1;
        }
    }
    if(y==0){
        int sum=0;
        for(int i=y;i<4;i++){
            if(a[x][i]==a[x][y]||a[x][i]=='T')sum++;
        }
        //printf("SUM %d %d %d %c\n",sum,x,y,a[x][y]);
        if(sum==4){
            if(a[x][y]=='X'||a[x][y+1]=='X')return 0;
            if(a[x][y]=='O'||a[x][y+1]=='O')return 1;
        }
    }
    if(x==0&&y==0){
        int sum=0;
        for(int i=0;i<4;i++){
            if(a[x+i][y+i]==a[x][y]||a[x+i][y+i]=='T')sum++;
        }
        if(sum==4){
            if(a[x][y]=='X'||a[x+1][y+1]=='X')return 0;
            if(a[x][y]=='O'||a[x+1][y+1]=='O')return 1;
        }
    }
    if(x==0&&y==3){
        int sum=0;
        for(int i=0;i<4;i++){
            if(a[x+i][y-i]==a[x][y]||a[x+i][y-i]=='T')sum++;
        }
        //printf("SUM %d %d %d %c\n",sum,x,y,a[x][y]);
        if(sum==4){
            if(a[x][y]=='X'||a[x+1][y-1]=='X')return 0;
            if(a[x][y]=='O'||a[x+1][y-1]=='O')return 1;
        }
    }
    return -1;
}
int calc(){
    int re=-1;
    for(int i=0;i<4;i++)
        scanf("%s",a[i]);
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(i==0||j==0&&a[i][j]!='.')re = check(i,j);
            if(re!=-1)return re;
        }
    }
    if(re==-1){
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[i][j]=='.')return 2;
            }
        }
    }
    return 3;
}

int main(){
    freopen("in1.in","r",stdin);
    freopen("out1.out","w",stdout);
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        int result=-1;
        result = calc();
        if(result==0)printf("Case #%d: X won\n",i+1);
        if(result==1)printf("Case #%d: O won\n",i+1);
        if(result==2)printf("Case #%d: Game has not completed\n",i+1);
        if(result==3)printf("Case #%d: Draw\n",i+1);
        //printf("KUY %d\n",result);
    }
}
