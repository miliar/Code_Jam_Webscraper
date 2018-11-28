
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <stdlib.h>
#include <string.h>
using namespace std;
map<string,int>mp;
int i,j,k,y,ans,n,len,test,kase,m;
char str[200],strin[120],ch;


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>test;
    while(test--)
    {
        mp.clear();
        cin>>n>>m;ans = 0;
        for(i=0;i<n;i++)
        {
            scanf("%s",str);
            mp[str]=1;
        }
        for(i=0;i<m;i++)
        {
            scanf("%s",strin);
            len = strlen(strin);
            k = j = y=0;

            //str[k++]='/';
            for(j=0;j<len;j++)
            {
                //putchar(ch);
                ch = strin[j];
                if(ch!='/')
                {
                    str[k++] = ch;
               //     printf("%c",ch);
                }

                else if(j)
                {
                 //   cout<<i<<endl;
                    str[k]=NULL;
                 //   puts(str);
                    if(mp[str])
                        y=0;
                    else
                    {
                        mp[str]=1;
                        y++;
                    }
                 //   cout<<"ji"<<endl;
                    str[k++]='/';
                 //   cout<<"y = "<<y<<endl;
                }
                else str[k++]='/';
            }
            //cout<<"ans = "<<ans<<endl;
            str[k]=NULL;
            if(mp[str])y=0;
            else mp[str] = 1,y++;
            ans+=y;
        }
        printf("Case #%d: %d\n",++kase,ans);
    }
    return 0;
}


