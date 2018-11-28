#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <cstring>
#include <stack>
using namespace std;

int ma[1001];

int main()
{
    int T;
    scanf("%d",&T);
    for(int I=0;I<T;I++)
    {
        int n;
        scanf("%d",&n);
        int ok=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&ma[i]);
            ok^=ma[i];
        }
        if(ok)
        {
            printf("Case #%d: NO\n",I+1);
            continue;
        }
        sort(ma,ma+n);
        long long res=0;
        for(int i=1;i<n;i++)
            res+=ma[i];

        cout<<"Case #"<<I+1<<": "<<res<<endl;
    }
}