#include <iostream>
#include <map>
#include <string>
#include <stdio.h>
using namespace std;

map<string,char> combine;
bool oppose[256][256];

int main()
{
  //  freopen("B-large.in","r",stdin);
  //  freopen("b.out","w",stdout);
    int n, i, j, k;
    scanf("%d",&n);
    char str[256];
    char newstr[256];
    char temp[3];
    int newPos;
    char c;
    for(i=0; i<n; i++)
    {
        combine.clear();
        memset(oppose,0,sizeof(oppose));
        int m;
        scanf("%d",&m);
        for(j=0; j<m; j++)
        {
            scanf("%s",str);
            c = str[2];
            str[2] = 0;
            combine[str] = c;
            swap(str[0],str[1]);
            combine[str] = c;
        }
        scanf("%d",&m);
        for(j=0; j<m; j++)
        {
            scanf("%s",str);
            oppose[str[0]][str[1]] = true;
            oppose[str[1]][str[0]] = true;
        }
        scanf("%d",&m);
        scanf("%s",str);
        newPos = -1;
        for(j=0; j<m; j++)
        {
            newstr[++newPos] = str[j];
            if(newPos >= 1)
            {
                temp[0] = newstr[newPos-1];
                temp[1] = newstr[newPos];
                temp[2] = 0;
                map<string,char>::iterator it;
                it = combine.find(temp);
                if(it != combine.end())
                {
                    newPos--;
                    newstr[newPos]= it->second ;
                }
            }
            if(newPos >= 1)
            {
                for(k=0; k<newPos;k++)
                {
                    if(oppose[newstr[newPos]][newstr[k]] == true)
                    {
                        newPos = -1;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: [",i+1);
        if(newPos >= 0)
            printf("%c",newstr[0]);
        for(k=1; k<=newPos;k++)
        {
            printf(", %c",newstr[k]);
        }
        printf("]\n");
    }
    return 0;
}