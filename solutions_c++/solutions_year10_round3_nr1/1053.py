#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

int i,j,k,n,l[2000],r[2000],cnt,test,kase;
bool flag[2000];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>test;
    while(test--)
    {
        memset(flag,0,sizeof(flag));
        cin>>n;cnt = 0;
        for(i=0;i<n;i++)
            scanf("%d %d",&l[i],&r[i]);
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {

                if(i!=j && !flag[j] && ((l[i]>l[j] && r[i]<r[j]) || (l[i]<l[j] && r[i]>r[j])))
                {
                    cnt++;
                    flag[i] = 1;
                }
            }
        }
        printf("Case #%d: %d\n",++kase,cnt);
    }
    return 0;
}
