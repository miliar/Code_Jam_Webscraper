#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
char cad[200];
int caso=0,C;
int let[256];
string in ="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string out="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

void doit(){
    gets(cad);
    printf("Case #%d: ",++caso);
    string s(cad);
    for(int i=0;i<s.length();++i)putchar(let[s[i]]);
    printf("\n");
    }
int main(){
    for(int i=0;i<in.length();++i)let[in[i]]=out[i];
    let['z']='q';
    let['q']='z';
    scanf("%d\n",&C);
    for(int i=0;i<C;++i)doit();
    }
