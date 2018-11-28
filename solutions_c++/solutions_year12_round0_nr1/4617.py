#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
int mp[1000];
char s[200];
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int i,j,k,m,n,l,t,cs=1;
    char s1[200]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    char s2[200]="our language is impossible to understand";
    l=strlen(s1);
    for(i=0;i<l;i++)
    mp[s1[i]]=s2[i];
    char s3[200]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    char s4[200]="there are twenty six factorial possibilities";
    l=strlen(s3);
    for(i=0;i<l;i++)
    mp[s3[i]]=s4[i];
    char s5[200]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char s6[200]="so it is okay if you want to just give up";
    l=strlen(s5);
    for(i=0;i<l;i++)
    mp[s5[i]]=s6[i];
    mp[' ']=' ';
    mp['q']='z';
    mp['z']='q';
    scanf("%d",&t);
    getchar();
    while(t--)
    {
        gets(s);
        l=strlen(s);
        printf("Case #%d: ",cs++);
        for(i=0;i<l;i++)
        printf("%c",mp[s[i]]);
        puts("");
    }
}
