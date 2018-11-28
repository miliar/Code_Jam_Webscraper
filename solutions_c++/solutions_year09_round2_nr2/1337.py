#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
    freopen("B_easy.in","r",stdin);
    freopen("B_easy.out","w",stdout);
    
    int T;
    
    scanf("%d",&T);
    
    for(int t = 1; t <= T; ++t)
    {
        int n;
        
        scanf("%d",&n);
        
        vector<int> dig;
        
        while(n)
        {
            dig.push_back(n%10);
            n/=10;   
        }   
        
        reverse(dig.begin(),dig.end());
        
        int ans = 0;
        
        if(next_permutation(dig.begin(),dig.end()))
        {
            for(int i = 0; i < dig.size(); ++i)
            {
                ans = ans*10 + dig[i];
            }   
        }
        else
        {
            sort(dig.begin(),dig.end());
            int indx = 0;
            
            while(dig[indx]==0) ++indx;
            
            if(indx > 0)
            {
                dig[0] = dig[indx];
                dig[indx] = 0;   
            }
            
            ans = dig[0]*10;
            
            for(int i = 1; i < dig.size(); ++i)
            {
                ans = ans*10 + dig[i];   
            }   
        }
        
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;   
}
