#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>


using namespace std;



int main()
{
    int T;

    char a[300] ;
    int i ;
    char str[1000] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    char str2[1000] = "our language is impossible to understand";
    for(i = 0 ; i < strlen(str) ; i++ )
    {
        a[str[i]] = str2[i];
    }

    strcpy(str,"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    strcpy(str2,"there are twenty six factorial possibilities");

    for(i = 0 ; i < strlen(str) ; i++ )
    {
        a[str[i]] = str2[i];
    }

    strcpy(str,"de kr kd eoya kw aej tysr re ujdr lkgc jv");
    strcpy(str2,"so it is okay if you want to just give up");

    for(i = 0 ; i < strlen(str) ; i++ )
    {
        a[str[i]] = str2[i];
    }

    for(i = 0 ; i < 255 ; i++)
    {
//        printf("%c %c\n",(char)(i),char(a[i]));
    }
    a['z'] = 'q';
    a['q'] = 'z';
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int tt = 0;
    while(scanf("%d\n",&T)!=EOF)
    {
        char s[1000];
        gets(s);
        printf("Case #%d: ",++tt);
        for(i = 0 ; i < strlen(s) ; i++)
            printf("%c",(char)a[s[i]]);

        putchar(10);
    }
    return 0;
}

