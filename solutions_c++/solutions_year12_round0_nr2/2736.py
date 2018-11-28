#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen ("Dancing With the Googlers.in" , "r" , stdin);
    freopen ("Dancing With the Googlers.out" , "w" , stdout);
    
    int T,N,S,P,i,j;
    cin >> T;
    for (i=1; i<=T; i++)
    {
        cin >> N >> S >> P;
        vector <int> a(N,0);
        int ans=0;
        for (j=0; j<N; j++)cin >> a[j];
        sort(a.begin(),a.end());
        j=0;
        while (S)
        { 
          if (a[j]<2)
             if (a[j]>=P)ans++;
             else;
          else
          {
              int m=a[j]/3+1;
              if (a[j]%3==2)m+=1;
              if (m>=P)ans++;
              S--;
          }
          j++;
         }
         for (; j<N; j++)
         {
             int m=a[j]/3+(a[j]%3>0);
             if (m>=P)ans++;
         }
         cout << "Case #" << i << ": " << ans << endl;
    }
}
