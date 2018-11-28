#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;


pair<int, int> nodes[10009];
int values[10009];


int table[10009][2];

int go(int n, int v)
{
    if(table[n][v] != -1)
        return table[n][v];
    else if(values[n] == v)
        return table[n][v] = 0;
    else if(nodes[n].first == -1)
        return table[n][v] = -2;
    else if(!nodes[n].second)
    {
        if(nodes[n].first)
        {
            if(v)
            {
                int l = go(n * 2, 1);
                int r = go(n * 2 + 1, 1);
                
                if(l < 0 || r < 0)
                    return table[n][v] = -2;
                else
                    return table[n][v] = l + r;
            }
            else 
            {
                int l, r;
                
                l = go(n * 2, 0);
                r = go(n * 2 + 1, 0);
                                
                if(l < 0)
                    return table[n][v] = r;
                else if(r < 0)
                    return table[n][v] = l;
                else
                    return table[n][v] = min(r, l);                
            }                          
        }
        else
        {
            if(v)
            {
                int l, r;
                
                l = go(n * 2, 1);
                r = go(n * 2 + 1, 1);
                                
                if(l < 0)
                    return table[n][v] = r;
                else if(r < 0)
                    return table[n][v] = l;
                else
                    return table[n][v] = min(r, l);                                                  
            }
            else
            {
                int l = go(n * 2, 0);
                int r = go(n * 2 + 1, 0);
                
                if(l < 0 || r < 0)
                    return table[n][v] = -2;
                else
                    return table[n][v] = l + r;                
            }            
        }                
    }
    else
    {
        int ans;
        
        //if(nodes[n].first)
        {
            if(v)
            {
                int l = go(n * 2, 1);
                int r = go(n * 2 + 1, 1);
                
                if(l < 0 || r < 0)
                    ans = -2;
                else
                    ans = l + r;
            }
            else 
            {
                int l, r;
                
                l = go(n * 2, 0);
                r = go(n * 2 + 1, 0);
                                
                if(l < 0)
                    ans = r;
                else if(r < 0)
                    ans = l;
                else
                    ans = min(r, l);                
            }                          
        }
        
        int ans2;
        {
            if(v)
            {
                int l, r;
                
                l = go(n * 2, 1);
                r = go(n * 2 + 1, 1);
                                
                if(l < 0)
                    ans2 = r;
                else if(r < 0)
                    ans2 = l;
                else
                    ans2 = min(r, l);                                                  
            }
            else
            {
                int l = go(n * 2, 0);
                int r = go(n * 2 + 1, 0);
                
                if(l < 0 || r < 0)
                    ans2 = -2;
                else
                    ans2 = l + r;                
            }            
        }                    
    
        
        
        if(ans >= 0)
            ans += (nodes[n].first != 1);
        if(ans2 >= 0)
            ans2 += (nodes[n].first != 0);
        
        if(ans < 0)
            return table[n][v] = ans2;
        else if(ans2 < 0)
            return table[n][v] = ans;
        else
            return table[n][v] = min(ans, ans2);
        
        
        
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    
    for(int z = 1; z <= N; z++)
    {
        memset(table, -1, sizeof(table));
        int M, V;
        scanf("%d%d", &M, &V);        
            
        for(int i = 1; i <= (M - 1) / 2; i++)
            scanf("%d%d", &nodes[i].first, &nodes[i].second);
        for(int i = (M - 1) / 2 + 1; i <= M; i++)  
            scanf("%d", &nodes[i].second), nodes[i].first = -1, values[i] = nodes[i].second;
        
        
        for(int i = (M - 1) / 2; i > 0; i--)
            if(nodes[i].first)
                values[i] = values[i * 2] && values[i * 2 + 1];
            else
                values[i] = values[i * 2] || values[i * 2 + 1];
        
//        for(int i = 1; i <= M; i++)
  //          printf("%d ", values[i]);
    //    printf("\n");
    
        printf("Case #%d: ", z);
    
        if(values[1] == V)
            printf("0\n");
        else
        {
            int t = go(1, V);
            if(t == -2)
                printf("IMPOSSIBLE\n");
            else
                printf("%d\n", t);    
        }
        
            
    }
    return 0;   
}
