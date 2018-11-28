#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
    int t,n,k,tmp;
    
    scanf("%d", &t);
    
    for(int i = 0; i < t; ++i)
    {
        scanf("%d %d", &n, &k);    
        tmp =(int) pow((double) 2,(double) n);
        while(k > tmp)
        {
            k-= tmp;
            
        }        
        if(k == tmp - 1)
        {
            printf("Case #%d: ON\n",i+1);   
            
        }
        else
        {
            printf("Case #%d: OFF\n",i+1);
        }    
            
    }
    
    
}
