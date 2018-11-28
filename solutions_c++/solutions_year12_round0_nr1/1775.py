#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>
#include<cstring>


using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf


char mapper[300];

bool foundInSource[300];
bool foundInDes[300];

void GenMap()
{
    char* source = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    char* des = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

    fill(foundInDes,foundInDes+300,false);
    fill(foundInSource, foundInSource, false);

    int i;
    for(i=0;i<300;i++)
        mapper[i] = 0;
    mapper[32] = 32;
    for(i=0;source[i];i++)
    {
        mapper[ source[i] ] = des[i];

        foundInDes[des[i] ] =  true;
        foundInSource[ source[i] ] = true;
    }
    char top,bot;

   /* for(top='a';top<='z';top++)
        printf("(%c,%c)\n", top, mapper[top]);


    for(top='a';top<='z';top++)
        for(bot='a';bot<='z';bot++)
            if ( foundInDes[top] == false && foundInSource[bot] == false)
                mapper[bot] = top;
   */

   mapper['q'] = 'z';
   mapper['z'] = 'q';

}

int main()
{
    //freopen("sample.in","r",stdin);

    freopen("a.in","r",stdin);
    freopen("a.ans","w",stdout);

    GenMap();
    int t;
    int kase=1;
    sf("%d",&t);
    char line[500];
    gets(line);
    while(t--)
    {
        pf("Case #%d: ",kase++);
        gets(line);
        int i;
        for(i=0;line[i];i++)
            putchar(mapper[line[i]]);
        pf("\n");
    }
    return 0;
}
