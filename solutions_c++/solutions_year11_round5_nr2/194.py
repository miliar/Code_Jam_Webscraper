#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <cctype>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

const int MAXN = 1001;
int v[MAXN], used[MAXN], gv[MAXN];

int main()
{
    freopen("Bs.in", "r", stdin);
    freopen("outb_s.txt", "w", stdout);
    int T, N;
    scanf("%d", &T);
    
    for(int t = 1; T--; ++t)
    {
        scanf("%d", &N);
        
        for(int i = 0; i < N; i++)
            scanf("%d", &v[i]);
        sort(v, v+N);
        
        int low = 1, up = N, mid, ans = 0;
        
        while(low <= up)
        {
            mid = (low+up)/2;
            
            bool chk = true;
            int cnt, g = 0;
            
            memset(used, 0, sizeof(used));
            for(int i = 0; i < N; i++)
                if(used[i] == 0)
                {
                    used[i] = ++g, gv[g-1] = v[i];
                    cnt = 1;
                    for(int j = i+1; j < N && cnt < mid; j++)
                        if(used[j]==0 && v[j] == gv[g-1]+1)
                        {
                            gv[g-1] = v[j];
                            used[j] = g;
                            ++cnt;
                        }
                    
                    if(cnt < mid) //merge
                    {
                        int gm = -1;
                        
                        for(int j = 0; j < N; j++)//reset
                            if(used[j] == g)
                                used[j] = 0;
                            
                        for(int j = 0; j < g-1; j++) //merge
                            if(gv[j]+1 == v[i])
                            {
                                gm = j;
                                break;
                            }
                            
                        if(gm != -1)
                        {
                            gv[gm] = v[i];                        
                            used[i] = gm;
                            --g;
                        }
                        else
                        {
                            chk = false;
                            break;
                        }
                    }
                }            
            
            if(chk) ans = mid, low = mid+1;
            else up = mid-1;
        }
        
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
