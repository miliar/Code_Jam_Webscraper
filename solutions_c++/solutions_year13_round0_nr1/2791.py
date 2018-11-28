#include<stdio.h>
#include<fstream>
int main(){
freopen("A-small-attempt0.txt","r",stdin);
freopen("output1.txt","w",stdout);
int t,i,sum=0,sum1=0,count1=0,j,flag=0,flag1=0,v=0;
char ch[5];
scanf("%d",&t);
int a[4][4]={0};
while(t--){

        flag1=0;
        flag=0;
        sum=0;


for(i=0;i<4;i++){
        fflush(stdin);

        scanf("%s",&ch);
        for(j=0;j<4;j++){
        if(ch[j]=='X')
            a[i][j]=1;
        else if(ch[j]=='O')
            a[i][j]=-1;
        else if(ch[j]=='T')
            a[i][j]=100;
        else if(ch[j]=='.'){
            a[i][j]=0;
            flag1=1;
        }
    }

}

sum1=0;
 v++;
printf("Case #%d: ",v);
for(i=0;i<4;i++){
    sum=0;

        sum1+=a[i][i];




    if(sum1==103||sum1==4){
        printf("X won\n");
        flag=1;
    break;
    }
    else if(sum1==97||sum1==-4){
        printf("O won\n");
        flag=1;
    break;
    }
        sum=0;
    for(j=0;j<4;j++){
        sum+=a[i][j];
    }
    if(sum==103||sum==4){
        printf("X won\n");
        flag=1;
    break;
    }
    else if(sum==97||sum==-4){
        printf("O won\n");
        flag=1;
    break;
    }
    sum=0;
    for(j=0;j<4;j++){
        sum+=a[j][i];
    }
    if(sum==103||sum==4){
        printf("X won\n");
        flag=1;
    break;
    }
    else if(sum==97||sum==-4){
        printf("O won\n");
        flag=1;
    break;
    }

    sum=0;
    for(j=0;j<1;j++){
        sum+=a[0][3]+a[1][2]+a[2][1]+a[3][0];
    }
    if(sum==103||sum==4){
        printf("X won\n");
        flag=1;
    break;
    }
    else if(sum==97||sum==-4){
        printf("O won\n");
        flag=1;
    break;
    }

}
if(flag1==1&&flag==0)
    printf("Game has not completed\n");
else if(flag==0&&flag1==0)
    printf("Draw\n");

}


return 0;
}
