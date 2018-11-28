//Google_A

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;




bool Test(int n,int k)
{
    int res = 1;
    while(--n){
        res = (res<<1) + 1;
    }
    
    
    //printf("res = %d  k&res=%d\n",res,k&res);
    
    return  ((k&res) ^ res) == 0;
}



int main()
{
    
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int n,k;
    int t;
    scanf("%d",&t);
    int cs=0;
    while(++cs <=t ){
        scanf("%d%d",&n,&k);
        

        
        if( Test(n,k) )printf("Case #%d: ON\n",cs);
        else printf("Case #%d: OFF\n",cs);
    }
    
    return 0;    
}
