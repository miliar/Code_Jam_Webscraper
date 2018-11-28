#include<iostream>
#include<string.h>
#include<stdio.h>

using namespace std;
char conv(char a){
     char ch;
     switch(a){
               case 'y':ch='a';
               break;
               case 'n':ch='b';
               break;
               case 'f':ch='c';
               break;
               case 'i':ch='d';
               break;
               case 'c':ch='e';
               break;
               case 'w':ch='f';
               break;
               case 'l':ch='g';
               break;
               case 'b':ch='h';
               break;
               case 'k':ch='i';
               break;
               case 'u':ch='j';
               break;
               case 'o':ch='k';
               break;
               case 'm':ch='l';
               break;
               case 'x':ch='m';
               break;
               case 's':ch='n';
               break;
               case 'e':ch='o';
               break;
               case 'v':ch='p';
               break;
               case 'z':ch='q';
               break;
               case 'p':ch='r';
               break;
               case 'd':ch='s';
               break;
               case 'r':ch='t';
               break;
               case 'j':ch='u';
               break;
               case 'g':ch='v';
               break;
               case 't':ch='w';
               break;
               case 'h':ch='x';
               break;
               case 'a':ch='y';
               break;
               case 'q':ch='z';
               break;
               default:ch=a;
               break;
               }
     return ch;
}
               
int main(){
    char str[100],ch,ans[30][100];
    int n;
    cin>>n;
    cin.get(ch);
    for(int i=0;i<n;i++){
            int j=0;
            while(str[i]!='\n'){
            cin.get(str[i]);
            
            ans[i][j]=conv(str[i]);
            j++;
            }
    }
            for(int i=0;i<n;i++){
            cout<<"Case #"<<i+1<<": ";
            puts(ans[i]);}
     return 0;
}
                                                            
            
    
