#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <functional>
#include <utility>//pair
#include <iomanip>
using namespace std;

int num[3],m[3];
vector <int> v[3];

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int t,n,p,s,i,j,ca = 1,ans,cou;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&n,&s,&p);
        for( i = 0; i < 3; ++i) v[i].clear();
        ans = 0;
        for( i = 0; i < n; ++i)
        {
            scanf("%d",&num[i]);
            if(num[i] % 3 == 0)
            {
                v[i].push_back(num[i] / 3);
                v[i].push_back(num[i] / 3);
                v[i].push_back(num[i] / 3);
                v[i].push_back(num[i] / 3 - 1);
                v[i].push_back(num[i] / 3);
                v[i].push_back(num[i] / 3 + 1);
            }
            else if(num[i] % 3 == 1)
            {
                    v[i].push_back(num[i] / 3);
                    v[i].push_back(num[i] / 3);
                    v[i].push_back(num[i] / 3 + 1);
                    v[i].push_back(num[i] / 3 - 1);
                    v[i].push_back(num[i] / 3 + 1);
                    v[i].push_back(num[i] / 3 + 1);
            }
            else
            {
                v[i].push_back(num[i] / 3);
                v[i].push_back(num[i] / 3 + 1);
                v[i].push_back(num[i] / 3 + 1);
                v[i].push_back(num[i] / 3);
                v[i].push_back(num[i] / 3);
                v[i].push_back(num[i] / 3 + 2);
            }
        }    
        for( i = 0; i < n; ++i)
        {
            m[i] = i;
        }
        do
        {
            cou = 0;
            for( i = 0; i < s; ++i)
            {
                if(num[m[i]] <= 1)  break;
                if(v[m[i]][5] >= p) cou++;
            }
            for( ; i < n; ++i)
            {
                if(v[m[i]][2] >= p) cou++;
            }
            ans = max(ans,cou);
        }while(next_permutation(m,m + n));
        printf("Case #%d: %d\n",ca++,ans);
    }
    return 0;
}












