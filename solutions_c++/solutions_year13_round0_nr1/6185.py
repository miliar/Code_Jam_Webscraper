#include<stdio.h>
#include<iostream>
using namespace std;
int main(){
char arr[4][4];
int store[4][4];
int i,j,t,c,test,sum,sum1,flag,flag1,flag2;
cin>>t;
for(test=1;test<=t;test++){
    flag=0;
    flag1=0;
    flag2=0;
    sum=0;
    sum1=0;
for(i=0;i<4;i++){
scanf("%s",&arr[i]);
}

for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(arr[i][j]=='.'){
store[i][j]=-1;
}
if(arr[i][j]=='O'){
store[i][j]=1;
}
if(arr[i][j]=='T'){
store[i][j]=100;}
if(arr[i][j]=='X'){
store[i][j]=9;
}
}}
/*for(i=0;i<4;i++){
for(j=0;j<4;j++){
printf("%d ",store[i][j]);
}
printf("\n");}*/
for(i=0;i<4;i++){
    sum=0;
for(j=0;j<4;j++){
    sum=sum+store[i][j];
    }
    if(sum==36 || sum==127 ){
    printf("Case #%d: X won\n",test);
    flag=1;
    }
    if(sum==4 || sum==103){
    printf("Case #%d: O won\n",test);
    flag=1;
    }
    }if(flag==1){
    continue;
    }
    for(i=0;i<4;i++){
    sum=0;
for(j=0;j<4;j++){
sum=sum+store[j][i];}
if(sum==36 || sum==127 ){
    printf("Case #%d: X won\n",test);
    flag=1;
    }
    if(sum==4 || sum==103){
    printf("Case #%d: O won\n",test);
    flag=1;
    }}if(flag==1){
    continue;
    }
    if((store[0][0]+store[1][1]+store[2][2]+store[3][3])==36 || (store[0][0]+store[1][1]+store[2][2]+store[3][3])==127 || (store[0][3]+store[1][2]+store[2][1]+store[3][0])==36  || (store[0][3]+store[1][2]+store[2][1]+store[3][0])==127 ){
     printf("Case #%d: O won\n",test);
    flag=1;
    }if(flag==1){
    continue;
    }

     if((store[0][0]+store[1][1]+store[2][2]+store[3][3])==4 || (store[0][0]+store[1][1]+store[2][2]+store[3][3])==103 || (store[0][3]+store[1][2]+store[2][1]+store[3][0])==4  || (store[0][3]+store[1][2]+store[2][1]+store[3][0])==103 ){
     printf("Case #%d: O won\n",test);
    flag=1;
    }
    if(flag==1){
    continue;
    }
    else{
    for(i=0;i<4;i++){
for(j=0;j<4;j++){
    if(store[i][j]==-1){
    printf("Case #%d: Game has not completed\n",test);
flag1=1;
break;
    }
    }
    if(flag1==1){
    break;
    }
    }
    if(flag1==0){
    printf("Case #%d: Draw\n",test);
    }

    }

}
return 0;
}
