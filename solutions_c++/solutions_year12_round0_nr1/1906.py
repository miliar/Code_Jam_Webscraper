#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <math.h>
#include <iostream>
#include <string>
using namespace std;
char ys[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char s[1100];
int main()
{
    int t;
    
   // freopen("in.in","r",stdin);
    //freopen("out.out","w",stdout);
    scanf("%d",&t);
    //printf("%d ",t);
    getchar();
    int num=0;    
    while (t--)
    {
          printf("Case #%d: ",++num);
          gets(s);
          int i;
          for (i=0;i<strlen(s);i++)
          if (s[i]==' ')
          printf(" ");
          else
          printf("%c",ys[s[i]-'a']);
          printf("\n");
    }
}
