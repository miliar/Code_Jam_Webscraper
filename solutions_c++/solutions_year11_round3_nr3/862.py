#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int num[105];

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int c,n,l,h,i,j,k=1;
    bool f;
    scanf("%d",&c);
    while(c--)
    {
        scanf("%d%d%d",&n,&l,&h);
        for( i=0; i<n; ++i)
        {
            scanf("%d",&num[i]);
        }
        f=0;
        for( i=l; i<=h; ++i)
        {
            f=1;
            for( j=0; j<n; ++j)
            {
                if(num[j]>=i && num[j]%i!=0) f=0;
                if(num[j]<i && i%num[j]!=0) f=0;
            }
            if(f) break;
        }
        printf("Case #%d:",k++);
        if(f==0) 
        {
            printf(" NO\n");
        }    
        else
        {
            printf(" %d\n",i);
        }
    }
    return 0;
}















