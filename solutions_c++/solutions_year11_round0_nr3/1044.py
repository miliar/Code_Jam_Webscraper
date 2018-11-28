#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int a[1000];
int main()
{
    int t,T,n,i,j,sum;

    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);   
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        j=sum=0;
        
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            j^=a[i];
            sum+=a[i];
        }
        if(j) printf("Case #%d: NO\n",t);
        else printf("Case #%d: %d\n",t,sum- *min_element(a,a+n));
    
    }
//system("pause");

    return 0;
}
