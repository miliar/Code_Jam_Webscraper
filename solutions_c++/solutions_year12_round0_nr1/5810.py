#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char decode(char ch){
    switch(ch){
        case 'a':
        return 'y';
        case 'b':
        return 'h';
        case 'c':
        return 'e';
        case 'd':
        return 's';
        case 'e':
        return 'o';
        case 'f':
        return 'c';
        case 'g':
        return 'v';
        case 'h':
        return 'x';
        case 'i':
        return 'd';
        case 'j':
        return 'u';
        case 'k':
        return 'i';
        case 'l':
        return 'g';
        case 'm':
        return 'l';
        case 'n':
        return 'b';
        case 'o':
        return 'k';
        case 'p':
        return 'r';
        case 'q':
        return 'z';
        case 'r':
        return 't';
        case 's':
        return 'n';
        case 't':
        return 'w';
        case 'u':
        return 'j';
        case 'v':
        return 'p';
        case 'w':
        return 'f';
        case 'x':
        return 'm';
        case 'y':
        return 'a';
        case 'z':
        return 'q';
    }
}
int main(){
    int t,len[31];
    scanf("%d",&t);
    //cin>>t;
    //fflush(stdin);
    getchar();
    char s[31][101],g[31][101];
    int i,j;
    for(i=0;i<t;i++){
        gets(s[i]);
        //cout<<"111"<<"\n";
    }
    for(i=0;i<t;i++){
        for(j=0;j<strlen(s[i]);j++){
            if(s[i][j]=='.' || s[i][j]==' ')
                g[i][j]=s[i][j];
            else{
                g[i][j]=decode(s[i][j]);
            }
        }
        g[i][j]='\0';
    }
    for(i=0;i<t;i++){
        cout<<"Case #"<<i+1<<": "<<g[i];
        cout<<"\n";
    }
    return 0;
}
