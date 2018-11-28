// <dEEpEshP> 

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<conio.h>
#define MAX 101
using namespace std;
char arr1[MAX],arr2[MAX];
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

int main(){int test;int i,j,k=0;
freopen("A-small-attempt2.in","r",stdin);
freopen("A-small-attempt2.out","w",stdout);
scanf("%d",&test); test=test+1;
while(test--) {
               gets(arr1);
               for(i=0,j=0;i<strlen(arr1);i++)
               {if(arr1[i]==' ') {arr2[j++]=' ';}
                if(arr1[i]=='a') {arr2[j++]='y';}
                if(arr1[i]=='b') {arr2[j++]='h';}
                if(arr1[i]=='c') {arr2[j++]='e';}
                if(arr1[i]=='d') {arr2[j++]='s';}
                if(arr1[i]=='e') {arr2[j++]='o';}
                if(arr1[i]=='f') {arr2[j++]='c';}
                if(arr1[i]=='g') {arr2[j++]='v';}
                if(arr1[i]=='h') {arr2[j++]='x';}
                if(arr1[i]=='i') {arr2[j++]='d';}
                if(arr1[i]=='k') {arr2[j++]='i';}
                if(arr1[i]=='l') {arr2[j++]='g';}
                if(arr1[i]=='m') {arr2[j++]='l';}
                if(arr1[i]=='n') {arr2[j++]='b';}
                if(arr1[i]=='o') {arr2[j++]='k';}
                if(arr1[i]=='p') {arr2[j++]='r';}
                if(arr1[i]=='q') {arr2[j++]='z';}
                if(arr1[i]=='r') {arr2[j++]='t';}
                if(arr1[i]=='s') {arr2[j++]='n';}
                if(arr1[i]=='t') {arr2[j++]='w';}
                if(arr1[i]=='u') {arr2[j++]='j';}
                if(arr1[i]=='v') {arr2[j++]='p';}
                if(arr1[i]=='w') {arr2[j++]='f';}
                if(arr1[i]=='x') {arr2[j++]='m';}
                if(arr1[i]=='y') {arr2[j++]='a';}
                if(arr1[i]=='z') {arr2[j++]='q';}
                if(arr1[i]=='j') {arr2[j++]='u';}                       
               } 
                arr2[j]='\0';  
               if(strlen(arr2)==0) continue;
               else printf("Case #%d: %s\n",++k,arr2);
              }
getch();
  return 0;
  }

