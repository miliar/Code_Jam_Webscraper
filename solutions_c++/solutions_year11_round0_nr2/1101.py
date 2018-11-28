#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <cstring>
#include <stack>
using namespace std;

int ma[260][260];
int z[260][260];

int main()
{
    int T;
    scanf("%d",&T);
    for(int I=0;I<T;I++)
    {
        memset(ma,-1,sizeof(ma));
        memset(z,-1,sizeof(z));
        char s[300];
        int c;
        scanf("%d",&c);
        for(int i=0;i<c;i++)
        {
            scanf("%s",s);
            ma[s[0]][s[1]]=s[2];
            ma[s[1]][s[0]]=s[2];
        }

        int d;
        scanf("%d",&d);
        for(int i=0;i<d;i++)
        {
            scanf("%s",s);
            z[s[0]][s[1]]=1;
            z[s[1]][s[0]]=1;
        }

        int n;
        scanf("%d",&n);
        scanf("%s",s);

        vector<int> res;

        for(int i=0;i<n;i++)
        {
            res.push_back(s[i]);
            if(res.size()>1)
            {
                if(ma[res[res.size()-2]][res[res.size()-1]]!=-1)
                {
                    int temp=ma[res[res.size()-2]][res[res.size()-1]];
                    res.pop_back();
                    res.pop_back();
                    res.push_back(temp);
                }else
                {
                    for(int k=0;k<res.size()-1;k++)
                    {
                        if(z[res[k]][res[res.size()-1]]==1)
                        {
                            res.clear();
                            break;
                        }
                    }
                }
            }
            /*
            printf("%d> ",I+1);
            for(int k=0;k<res.size();k++)
            {
                printf("%c ",res[k]);
            }
            printf("\n");
             */
        }

        printf("Case #%d: [",I+1);
        if(res.size()==0)
        {
            printf("]\n");
            continue;
        }
        for(int i=0;i<res.size()-1;i++)
        {
            printf("%c, ",(char)(res[i]));
        }
        if(res.size()>0)
            printf("%c]\n",(char)(res[res.size()-1]));
    }
}