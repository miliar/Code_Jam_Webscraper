#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    freopen("A_large.in","r",stdin);
    freopen("A_large.out","w",stdout);
    
    int T;
    scanf("%d",&T);
    for(int t = 1; t <= T; ++t)
    {
        char in[80];
        scanf("%s",in);
        
        bool seen[300];
        
        memset(seen,0,sizeof(seen));
        
        int len = strlen(in), base = 0;
        
        for(int i = 0; i < len; ++i)
        {
            if(!seen[in[i]])
            {
                ++base;
                seen[in[i]] = true;   
            }   
        }
        
        if(base < 2) base = 2;
        
        printf("Case #%d: ",t);
        
        __int64 value[300];
        
        memset(value,-1,sizeof(value));
        
        if(len==1)
        {
            puts("1");   
        }
        else
        {
            __int64 ans = 0, b = base, p = 1;
            
            value[in[0]] = 1;
            
            int i = 1;
            
            while(in[i]==in[i-1]) ++i;
            
            if(i < len) value[in[i]] = 0;
            
            ++i;
            
            int dig = 2;
            
            for(; i < len; ++i)
            {
                if(value[in[i]]==-1)
                {
                    value[in[i]] = dig++;   
                }
            }
            
            for(int i = len-1; i >= 0; --i)
            {
                ans += value[in[i]]*p;
                p *= b;
            }
            
            printf("%I64d\n",ans);
        }
    }
    return 0;    
}
