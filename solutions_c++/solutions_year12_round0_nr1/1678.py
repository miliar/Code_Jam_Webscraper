#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

char buf[1005], hash[256];

void init()
{
        int i;
        char tmp[1005];
        strcpy(buf, "ejp mysljylc kd kxveddknmc re jsicpdrysi");
        strcpy(tmp, "our language is impossible to understand");
        for(i=0;buf[i];i++) hash[buf[i]] = tmp[i];
        strcpy(buf, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
        strcpy(tmp, "there are twenty six factorial possibilities");
        for(i=0;buf[i];i++) hash[buf[i]] = tmp[i];
        strcpy(buf, "de kr kd eoya kw aej tysr re ujdr lkgc jv");
        strcpy(tmp, "so it is okay if you want to just give up");
        for(i=0;buf[i];i++) hash[buf[i]] = tmp[i];
        //for(i='a';i<='z';i++) printf("hash[%c] = %c\n",i, hash[i]);
        hash['q'] = 'z';
        hash['z'] = 'q';


}
int main()
{
        int i,t,cas=0;
        freopen("A-small-attempt3.in","r",stdin);
        freopen("A.out","w",stdout);
        init();
        scanf("%d",&t);
        getchar();
        while(t--){
                gets(buf);
                printf("Case #%d: ",++cas);
                for(i=0;buf[i];i++)
                        if(buf[i]>='a'&&buf[i]<='z') printf("%c",hash[buf[i]]);
                        else printf("%c",buf[i]);
                printf("\n");
        }
        return 0;
}
