#include<iostream>
#include<cstdio>
#include<string.h>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

int n;
string s;

int main(){
    cin >> n;
    getchar();
    for(int i=0;i<n;i++){    
        getline(cin,s);
        for(int j=0;j<s.size();j++){
            if(s[j]=='a') s[j]='y';//q z
            else if(s[j]=='b') s[j]='h';
            else if(s[j]=='c') s[j]='e';
            else if(s[j]=='d') s[j]='s';
            else if(s[j]=='e') s[j]='o';
            else if(s[j]=='f') s[j]='c';
            else if(s[j]=='g') s[j]='v';
            else if(s[j]=='h') s[j]='x';
            else if(s[j]=='i') s[j]='d';
            else if(s[j]=='j') s[j]='u';
            else if(s[j]=='k') s[j]='i';
            else if(s[j]=='l') s[j]='g';
            else if(s[j]=='m') s[j]='l';
            else if(s[j]=='n') s[j]='b';
            else if(s[j]=='o') s[j]='k';
            else if(s[j]=='p') s[j]='r';
            else if(s[j]=='q') s[j]='z';
            else if(s[j]=='r') s[j]='t';
            else if(s[j]=='s') s[j]='n';
            else if(s[j]=='t') s[j]='w';
            else if(s[j]=='u') s[j]='j';
            else if(s[j]=='v') s[j]='p';
            else if(s[j]=='w') s[j]='f';
            else if(s[j]=='x') s[j]='m';
            else if(s[j]=='y') s[j]='a';
            else if(s[j]=='z') s[j]='q';
        }
        printf("Case #%d: ",i+1);
        cout << s << endl;
    }
    return  0;
}
