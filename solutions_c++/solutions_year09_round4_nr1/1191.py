#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<ctype.h>
#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>

using namespace std;

#define vs vector<string> 

int n;

bool ok(vs x)
{
    for(int i = 0; i < n; ++i)
    for(int j = i+1; j < n; ++j)
    if(x[i][j]=='1')
    return false;
    
    return true;
}

int main()
{
    freopen("A_small.in","r",stdin);
    freopen("A_small.out","w",stdout);
    
    char in[50];
    int T;
    scanf("%d",&T);
    
    for(int t = 1; t <= T; ++t)
    {
        scanf("%d",&n);
        vs mat;
        for(int i = 0; i < n; ++i)
        {
            scanf("%s",in);
            mat.push_back(string(in));   
        }    
        
        queue< vs > Q;
        
        Q.push(mat);
        
        map< vs, int > dist;
        
        dist.clear();
        
        dist[mat] = 0;
        
        int ans = -1;
        
        while(!Q.empty())
        {
            vs u = Q.front();
            int d = dist[u];
            
            if(ok(u))
            {
                ans = d;       
                break;
            }
            
            Q.pop();
            
            for(int i = 0; i < n-1; ++i)
            {
                vs tmp = u;
                
                string t = tmp[i]; // swaping...
                tmp[i] = tmp[i+1]; // ....
                tmp[i+1] = t;      //.....
                
                if(dist.find(tmp)==dist.end())
                {
                    dist[tmp] = d + 1;
                    Q.push(tmp);
                }         
            }
        }
        
        printf("Case #%d: %d\n",t,ans);
    }
    
    return 0;
}
