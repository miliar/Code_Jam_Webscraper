#include <iostream>
#include <sstream>
#include <stdio.h>
#include <string.h>
using namespace std;
int main()
{
    string a;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("a.out", "w", stdout);
    char f1[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
    char f2[]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q',' '};
    int x,w;
    scanf("%d\n",&x);

    for(int y=1;y<=x;y++)
    {
        getline(cin,a,'\n');

        int n=a.size(),c=0;
        printf("Case #%d: ",y);
        for(;c<n;c++)
        {

            for(int b=0;b<27;b++)
            {
                if(a[c]==f2[b]){printf("%c",f1[b]);}
            }
        }
        printf("\n");
    }
}
