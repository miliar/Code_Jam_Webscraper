#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>

using namespace std;


char m[30];
string inp[3]={
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};
string oup[3]={
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"
};

int t;
char buf[1000];

int main(){
    for(int i=0;i<26;++i) m[i]='q';
    for(int i=0;i<3;++i){
        cerr<<inp[i].length()<<endl;
        for(int j=0;j<inp[i].length();++j){
            if(inp[i][j]!=' ') m[inp[i][j]-'a'] = oup[i][j];
        }
    }
    m['y'-'a']='a';
    m['e'-'a']='o';
    m['q'-'a']='z';
    m[26]=0;
//    printf("%s\n",m);
    cin >> t; gets(buf);
    for(int i=0;i<t;++i){
        gets(buf);
        cerr<<buf<<endl;
        cout<<"Case #"<<i+1<<": ";
        for(int j=0;j<strlen(buf);++j) putchar(buf[j]==' '?' ':m[buf[j]-'a']);
        cout<<endl;
    }
    return 0;
}

