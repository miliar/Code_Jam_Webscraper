#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

#include<vector>
#include<iostream>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<stack>

using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    int T; scanf("%d",&T);
    
    for(int t = 1; t <= T; ++t)
    {
        int n, k;
        scanf("%d%d",&n,&k);
        
        printf("Case #%d: ",t);
        
        if(  (k & ((1<<n)-1)) == ((1<<n)-1) )        
        puts("ON");
        else
        puts("OFF");
        
    }
    
    return 0;
}
