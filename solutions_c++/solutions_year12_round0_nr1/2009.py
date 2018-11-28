#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
using namespace std;
int ntest;
string s="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz";
string t="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq";
int trans[256];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d\n",&ntest);
    for(int i=0; s[i]; i++){
        if(isalpha(s[i]))
            trans[s[i]]=t[i];
    }    
    for(int t=0; t<ntest; t++){  
        getline(cin,s);
        printf("Case #%d: ",t+1);
        for(int i=0; s[i]; i++)
            if(isalpha(s[i]))
                printf("%c",trans[s[i]]);
            else 
                printf("%c",s[i]);
        printf("\n");       
    }
    return 0;
}
