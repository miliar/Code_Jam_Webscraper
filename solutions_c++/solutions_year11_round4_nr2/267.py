#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 600;
char str[MAXN][MAXN];

int main()
{
    freopen("bin.in", "r", stdin);
    freopen("outb_s.txt", "w", stdout);
    int T, N, R, D, C;
    scanf("%d", &T);
    
    for(int t = 1; T--; ++t)
    {
        scanf("%d %d %d", &R, &C, &D);
        
        for(int i = 0; i < R; i++)
            scanf("%s", str[i]);
        
        int upper = min(R, C), ans = 0;        
        
        for(int k = 3; k <= upper; k++)
        {
            bool found = false;
            for(int i = 0; i < R && !found; i++)
                for(int j = 0; j < C && !found; j++)
                    if(i+k<=R && j+k<=C)
                    {
                        long long sumx = 0, sumy = 0;
                        if(k&1) //odd
                        {
                            for(int a = 0; a < k; a++)
                                for(int b = 0; b < k; b++)
                                {
                                    bool flag = (a==0&&b==k-1) || (a==k-1&&b==0) || (a==0&&b==0) || (a==k-1&&b==k-1);
                                    if(!flag)
                                    {
                                        sumx += (a-k/2)*(long long)(str[i+a][j+b]-'0');
                                        sumy += (b-k/2)*(long long)(str[i+a][j+b]-'0');
                                    }
                                }                      
                        }
                        else //even
                        {
                            for(int a = 0; a < k; a++)
                                for(int b = 0; b < k; b++)
                                {
                                    bool flag = (a==0&&b==k-1) || (a==k-1&&b==0) || (a==0&&b==0) || (a==k-1&&b==k-1);
                                    if(!flag)
                                    {
                                        sumx += (a*2-k+1)*(long long)(str[i+a][j+b]-'0');
                                        sumy += (b*2-k+1)*(long long)(str[i+a][j+b]-'0');
                                    }
                                }
                        }
                        
                        if(sumx == 0 && sumy == 0)
                        {
                            ans = k;
                            found = true;
                        }
                    }
            }
        if(ans)
            printf("Case #%d: %d\n", t, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", t);
    }
    
    return 0;
}
