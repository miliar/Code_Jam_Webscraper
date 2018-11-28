#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
char c[150];
int t;
int m[300];
string s1="qzejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string s2="zqour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

int main(){
    for(int i=0;i<s1.length();++i)m[s1[i]]=s2[i];
    scanf("%d\n",&t);
    for(int i=1;i<=t;++i){
        gets(c);
        printf("Case #%d: ",i);
        string s(c);
        for(int i=0;i<s.length();++i)putchar(m[s[i]]);
        printf("\n");
        }
    }
