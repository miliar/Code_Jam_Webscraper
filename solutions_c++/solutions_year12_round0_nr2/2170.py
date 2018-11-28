#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<string>
#include<algorithm>
#include<stack>
#include<vector>
using namespace std;

int main()
{
    int tc;
    cin>>tc;
    for(int i = 1; i<= tc; i++)
    {
            int n,p,s,cnt1 = 0, cnt2 =0;
            scanf("%d %d %d",&n,&s,&p);
            int arr[n];
            for(int j = 0;j<n ;j++)
            {
                    scanf("%d", &arr[j]);
                    if(p>1)
                    {
                    if(arr[j] >= (3*p-2))
                              cnt1++;
                    else if(arr[j] >= (3*p-4))
                              cnt2++;
                    }
                    else if(p== 1 && arr[j] > 0)
                         cnt1++;     
                    else if(p == 0)
                         cnt1++;
            }
            int tot = cnt1 + min(cnt2,s);
            printf("Case #%d: %d\n",i,tot);
    }
    return 0;
}
