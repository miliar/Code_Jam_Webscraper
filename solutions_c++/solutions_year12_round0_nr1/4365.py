#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAXM=26;

char c[1000];
int word[MAXM]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,cas;
    scanf("%d",&t);
    getchar();
    for(cas=1;cas<=t;cas++)
    {
        gets(c);
        printf("Case #%d: ",cas);
        int len=strlen(c);
        for(int i=0;i<len;i++)
        {
            if(c[i]>='a' && c[i]<='z') printf("%c",word[c[i]-'a']+'a');
            else printf("%c",c[i]);
        }
        puts("");
    }
    return 0;
}
/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities
de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
*/
