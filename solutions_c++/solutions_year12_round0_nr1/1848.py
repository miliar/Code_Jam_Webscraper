#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    char dict[26];
    dict[0]='y';
    dict[1]='h';
    dict[2]='e';
    dict[3]='s';
    dict[4]='o';
    dict[5]='c';
    dict[6]='v';
    dict[7]='x';
    dict[8]='d';
    dict[9]='u';
    dict[10]='i';
    dict[11]='g';
    dict[12]='l';
    dict[13]='b';
    dict[14]='k';
    dict[15]='r';
    dict[16]='z';
    dict[17]='t';
    dict[18]='n';
    dict[19]='w'; 
    dict[20]='j';
    dict[21]='p';
    dict[22]='f';
    dict[23]='m';
    dict[24]='a';
    dict[25]='q';
    
    int ntest=0;
    string str;
    char tc;
    scanf("%d\n",&ntest);
    for (int test=1;test<=ntest;++test){
        str.clear();
        for (;;){
            scanf("%c",&tc);
            if (tc=='\n') break;
            else str+=tc;
        }
        printf("Case #%d: ",test);
        for (int i=0;i<str.size();++i){
            if (str[i]-'a'>=0 && str[i]-'a'<26) printf("%c",dict[str[i]-'a']);
            else printf("%c",str[i]);
        }
        printf("\n");
    }
    return 0;
}
