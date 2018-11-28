#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>

#include<sstream>
#include<stack>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-9



int a[10000];


int main()
{
    freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
    int i,n,cs=1,T;

    //printf("%d",T);
    scanf("%d",&T);

    for(cs=1;cs<=T;cs++)
    {
        scanf("%d",&n);
        {
            printf("Case #%d: ",cs);
            int ans=0;
            for(i=0;i<n;i++)
            {
                scanf("%d",&a[i]);
                ans^=a[i];
            }
            if(ans!=0)
            {
                printf("NO\n");
                continue;
            }
            sort(a,a+n);

            for(i=1;i<n;i++)
            {
                ans+=a[i];
            }
            printf("%d\n",ans);
        }
    }



    return 0;
}
