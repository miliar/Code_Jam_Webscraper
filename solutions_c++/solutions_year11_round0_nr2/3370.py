#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<queue>
#include<stack>

using namespace std;

char cs[100][5];
char ds[100][5];
char ns[1000];

int checkConvert(char a, char b, int c)
{
    int ret = -1;
    for(int i = 0; i<c; i++)
    {
        if(cs[i][0] == a && cs[i][1] == b)
        {
            ret = i;
            break;
        }
        else if(cs[i][0] == b && cs[i][1] == a)
        {
            ret = i;
            break;
        }
    }
    
    return ret;
}

int checkClear(char a, char b, int d)
{
    int ret = -1;
    for(int i = 0; i<d; i++)
    {
        if(ds[i][0] == a && ds[i][1] == b)
        {
            ret = i;
            break;
        }
        else if(ds[i][0] == b && ds[i][1] == a)
        {
            ret = i;
            break;
        }
    }
    return ret;
}

int main(void){
    int T;
    
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d",&T);
    for(int t = 0; t<T; t++)
    {
        int c;
        scanf("%d",&c);
        for(int i = 0; i<c; i++)
        {
            scanf("%s",cs[i]);  // c strings each of 3 elements, first tow converts to 3rd one 
        }
        int d;
        scanf("%d",&d);
        for(int i = 0; i<d; i++)
        {
            scanf("%s",ds[i]);  // d strings each of 2 elements oppose
        }
        int n;
        scanf("%d %s",&n,ns); // n char in ns arr, these are base chars
        
        string ans = "";
        //char lastChar = ns[0];
        for(int i = 0; i<n; i++)
        {
            ans += ns[i];
            int sz = ans.size();
            if(sz > 1)
            {
                int x = checkConvert(ans[sz - 1], ans[sz - 2], c);
                if(x >= 0)
                {
                    ans.erase(sz - 2,2);
                    ans += cs[x][2];
                }
                else
                {
                    for(int j = 0; j<sz; j++)
                    {
                        for(int k = 0; k<sz; k++)
                        {
                            if(j == k)
                                continue;
                            int y = checkClear(ans[j], ans[k], d);
                            if(y > -1)
                            {
                                ans = "";
                                break;
                            }
                        }
                        if(ans == "")
                            break; 
                    }
                }
            }
        }
        
        printf("Case #%d: [",t+1);
        if(ans.size()>0)
        {
            for(int i = 0; i < ans.size() - 1; i++)
            {
                printf("%c, ",ans[i]);
            }
            printf("%c",ans[ans.size() - 1]);
        }
        puts("]");
    }
    return 0;
}
