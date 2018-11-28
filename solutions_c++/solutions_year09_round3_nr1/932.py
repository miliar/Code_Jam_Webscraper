#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;
int main()
{
    int t, num[200],k;    
    char a[65];
    long long ans;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(int tt = 0; tt<t; tt++)
    {
        scanf("%s",a);
        //cout << a << endl;
        k = 1;
        for(int i = 0; i < 200; i++) num[i] = -1;
        int n = strlen(a);
        //cout << n << endl;
        for(int i = 0; i < n; i++)
        {
                if (num[a[i]]==-1)
                {
                   num[a[i]] = k;
                   if (k==1) k=0;
                   else if (k==0) k=2;
                   else k++;
                   //cout << k << endl;
                   //cout << i << " " << a[i] << " " << num[a[i]] << endl;
                }
        }
        ans = 0;
        if ((k==0)||(k==1)) k=2;
        for(int i = 0; i < n; i++)
        {
                ans+=num[a[i]];
                if (i!=n-1) ans*=k;
                
        }               
        cout << "Case #" << (tt+1) << ": " << ans << endl;
    }
    
    return(0);
}
