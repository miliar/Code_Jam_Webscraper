#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

char map[27]={0};

string a="our language is impossible to understand";
string b="there are twenty six factorial possibilities";
string c="so it is okay if you want to just give up";

string aa="ejp mysljylc kd kxveddknmc re jsicpdrysi";
string bb="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string cc="de kr kd eoya kw aej tysr re ujdr lkgc jv";

int main (){
    
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    
    for(int i=0; i<a.size(); ++i) if(aa[i]!=' ') map[aa[i]-'a']=a[i];
    for(int i=0; i<b.size(); ++i) if(bb[i]!=' ') map[bb[i]-'a']=b[i];
    for(int i=0; i<c.size(); ++i) if(cc[i]!=' ') map[cc[i]-'a']=c[i];
    map['q'-'a']='z'; map['z'-'a']='q';
    
    int t;
    char s[109];
    scanf("%d", &t);
    gets(s);
    for(int i=0; i<t; ++i) {
        gets(s);
        printf("Case #%d: ", i+1);
        for(int j=0; s[j]; ++j) if(s[j]==' ') printf(" ");
        else printf("%c", map[s[j]-'a']);
        printf("\n");
    }
    
}
