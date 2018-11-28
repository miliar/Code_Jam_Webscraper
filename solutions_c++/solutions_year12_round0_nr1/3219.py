#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int main()
{
    int t,n,i,j;
    char g[200],ans[200],tem;
    int map[26]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    j=0;
    scanf("%d", &t);
    t++;
    while(t--)
    {
        cin.getline(g, 150);
        n=strlen(g);
        for(i=0;i<n&&g[i]!='\n'&&g[i]!='\0';i++)
        {
            if(g[i]==' ')
                ans[i]=' ';
            else
                ans[i]=map[g[i]-'a'];
        }
        ans[i]='\0';
        if(j!=0)
	        printf("Case #%d: %s\n", j, ans);
        j++;
    }
    return 0;
}
