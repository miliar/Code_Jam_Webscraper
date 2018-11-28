#include<iostream>
#include<math.h>
#include<cstdio>
#include<stdlib.h>
#include<cstring>
using namespace std;


int main()
{
    char a[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int T,j=1;
    //freopen("inp.txt","r",stdin);
    //freopen("out.txt","w",stdout);
     char str[105];
    scanf("%d\n",&T);
    while(T--)
    {

        gets(str);
        int i=0;
        while(str[i]!='\0')
        {
            if(str[i]!=' ')
            {
                str[i]=a[str[i]-'a'];
            }


            i++;
        }
         printf("Case #%d: %s\n", j,str);
        j++;
    }
    return 0;
}
