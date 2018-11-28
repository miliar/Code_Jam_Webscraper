#include <stdio.h>
#include <vector>
#include <stdlib.h>

using namespace std;

vector <long long> ans;
vector <long long> rec;
int g[1005];

int main(void)
{
    freopen("C-large.in", "r", stdin);
    freopen("C-big.out", "w", stdout);
    
    int T,r,n,k;
    bool v[1005];
    long long sum;
    
    scanf("%d", &T);
    for(int i=1; i<=T; i++)
    {
        scanf("%d%d%d", &r, &k, &n);
        for(int j=0; j<n; j++)
        {
            scanf("%d", &g[j]);
            v[j] = false;
        }
        
        //find the point
        int temp,sign;
        int pos = 0;
        int num = 0;
        while(1)
        {
            if(v[pos])
            {
                break;
            }
            else
            {
                v[pos] = true;
            }
            
            num = 0;
            sign = pos;
            while(1)
            {
                if(num + g[pos] <= k)
                {
                   num += g[pos];
                   pos = (pos + 1)%n;
                   if(pos == sign)
                   break;
                }
                else
                {
                   break;
                }
            }
        }
        
        int id = pos;
        
        pos = 0;
        ans.clear();
        ans.push_back(0);
        while(pos != id)
        {
            sign = pos;
            num = 0;
            while(1)
            {
                if(num + g[pos] <= k)
                {
                   num += g[pos];
                   pos = (pos + 1)%n;
                   if(pos == sign)
                   break;
                }
                else
                {
                   break;
                }
            }
            temp = ans.size();
            ans.push_back(ans[temp-1] + num);
        }
        
        rec.clear();
        rec.push_back(0);
        bool ok = false;
        while(1)
        {
            if(pos == id)
            {
                if(ok)
                break;
                else
                ok = true;
            }
            
            temp = rec.size();
            num = 0;
            sign = pos;
            while(1)
            {
                if(num + g[pos] <= k)
                {
                   num += g[pos];
                   pos = (pos + 1)%n;
                   if(pos == sign)
                   break;
                }
                else
                {
                   break;
                }
            }
            rec.push_back(rec[temp-1] + num);
        }
        
        if(r <= ans.size()-1)
        {
            sum  = ans[r];
        }
        else
        {
            sum = ans[ans.size()-1];
            r -= ans.size() - 1;
            temp = rec.size() - 1;
            int x = r / temp;
            int y = r % temp;
            sum += x * rec[temp] + rec[y];
        }
        
        
        /*
        sum = 0;
        int sign,num;
        int pos = 0;
        for(int j=0; j<r; j++)
        {   
            sign = pos;
            num = 0;
            while(1)
            {
                if(num + g[pos] <= k)
                {
                   num += g[pos];
                   pos = (pos + 1)%n;
                   if(pos == sign)
                   break;
                }
                else
                {
                   break;
                }
            }
            sum += num;
        }
        */
        
        printf("Case #%d: %lld\n", i, sum);
    }
    
    return 0;
}
