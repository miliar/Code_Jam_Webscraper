#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std;
char place(char a){
    switch(a){
        case 'a':return 'y';
                  break;
        case 'b':return 'h';
                  break;
        case 'c':return 'e';
                  break;
        case 'd':return 's';
                  break;
        case 'e':return 'o';
                  break;
        case 'f':return 'c';
                  break;
        case 'g':return 'v';
                  break;
        case 'h':return 'x';
                  break;
        case 'i':return 'd';
                  break;
        case 'j':return 'u';
                  break;
        case 'k':return 'i';
                  break;
        case 'l':return 'g';
                  break;
        case 'm':return 'l';
                  break;
        case 'n':return 'b';
                  break;
        case 'o':return 'k';
                  break;
        case 'p':return 'r';
                  break;
        case 'q':return 'z';
                  break;
        case 'r':return 't';
                  break;
        case 's':return 'n';
                  break;
        case 't':return 'w';
                  break;
        case 'u':return 'j';
                  break;
        case 'v':return 'p';
                  break;
        case 'w':return 'f';
                  break;
        case 'x':return 'm';
                  break;
        case 'y':return 'a';
                  break;
        case 'z':return 'q';
                  break;
        case ' ':return ' ';
                  break;
    }
}


int main(){
    int n,k;
    string s;
    char r[101];
    while(cin>>n){
    for(int i=0;i<n;i++){
        if(i==0)
        cin.ignore();
        getline(cin,s,'\n');
        for(k=0;k<s.length();k++){
           r[k]=place(s[k]);
        }
       r[k]='\0';
       k=0;
    cout<<"Case #"<<i+1<<": ";
    if(i==n-1)
    cout<<r;
    else
    cout<<r<<endl;
    }
    return 0;
    }
}
