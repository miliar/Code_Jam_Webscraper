#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main()
{
    freopen("test.out","w",stdout);
    char ans[30]="yhesocvxduiglbkrztnwjpfmaq";
    char str[10000];
    //cout<<strlen(str);
    int t, i, j;
    scanf("%d", &t);gets(str);
    for(i=1; i<=t; i++)
    {
        gets(str);
        printf("Case #%d: ", i);
        for(j=0; str[j]; j++)
        {
            if(str[j]==' ') putchar(' ');
            else putchar(ans[ str[j]-'a' ]);
        }
        printf("\n");
    }
	return 0;
}
