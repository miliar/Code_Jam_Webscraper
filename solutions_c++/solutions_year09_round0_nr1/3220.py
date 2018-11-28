#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

int l,r,d;
char dic[5001][26];

void f(char s[],int p,char s1[]){
     int k=strlen(s1),i;
     char s2[26];
     strcpy(s2,s1);
     if(l==k){
        for(i=0;i<d;i++) if(strcmp(s1,dic[i])==0){r=r+1;return;}
        return;
     }
     if (s[p]=='('){
         int e=p;
         while(s[e++]!=')');
         for(int i=p+1;i<e-1;i++){
             int a=0;
             for(int j=0;j<d;j++) if(strncmp(s1,dic[j],k-1)==0 && dic[j][k]==s[i]){a=a+1;}
             if(a>0 || k<2){
                 strcpy(s2,s1);
                 s2[k]=s[i];
                 s2[k+1]='\0';         
                 f(s,e,s2);
             }
         }
     }
     else{
          s2[k]=s[p];
          s2[k+1]='\0';  
          f(s,p+1,s2);
     }
     return; 
}

int main(){
    int i,n;
    char test[10000];
    fstream fin ,fout;
    fin.open("in.in");
    fout.open("out.txt");
    fin>>l>>d>>n;
    for(i=0;i<d;i++) fin>>dic[i];
    for(i=1;i<=n;i++){
               fin>>test;
               r=0;
               f(test,0,"");
               fout<<"Case #"<<i<<": "<<r<<endl;cout<<r<<endl;
    }
    fin.close();
    fout.close();
    getch();
    return 0;
}
