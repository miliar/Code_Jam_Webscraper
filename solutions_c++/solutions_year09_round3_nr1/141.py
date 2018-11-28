#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{

    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int T;
    scanf("%d",&T);
    int C=1;
    while(T--){
        
        char str[100];
        scanf("%s",str);
        int base=1;
        int len=strlen(str);
        int m[256];
        memset(m,0,sizeof(m));
        m[str[0]]=1;
        for(int i=1;i<len;i++){
            int j;
            for( j=i-1;j>=0;j--){
                if(str[i]==str[j])break;
            }
            if(j<0){
             
                if(base==1)
                    m[str[i]]=0;
                else 
                    m[ str[i] ]=base;
//                 printf("%c %d ",str[i],m[str[i]]);
                base++;
            }
        }
        if(base==1)base++;
        long long ans=0;
        for(int i=0;i<len;i++){
            ans*=base;
            ans+=m[str[i]];
//            printf("%d ",m[ str[i]]);
            
        }
        printf("Case #%d: %lld\n",C,ans);
        C++;
    }

    return 0;
}










