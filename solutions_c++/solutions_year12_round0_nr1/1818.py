#include <cstdio>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

const string src[]={
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    "y qee","z"};

const string dst[]={
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up",
    "a zoo","q"};

int main(){
    int cs;
    char s[200];
    map<char,char> e;
    for(int i=0;i<=4;i++)
        for(size_t o=0;o<src[i].size();o++)
            e[src[i][o]]=dst[i][o];
    sscanf(gets(s),"%d",&cs);
    for(int no=1;no<=cs;no++){
        gets(s);
        for(int i=0;s[i];i++) s[i]=e[s[i]];
        printf("Case #%d: %s\n",no,s);
    }
}
