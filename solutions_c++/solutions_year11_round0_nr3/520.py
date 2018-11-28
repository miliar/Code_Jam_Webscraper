
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>

using namespace std;
#define sz(a) a.size()
#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair

int main()
{
    int t;
    cin >> t;
    int kase = 0;
    while(t--)
    {
              int n;
              kase++;
              cin >> n;
              int arr[n];
              int sum = 0, ans=0, m = 10000000;
              for(int i=0;i < n ;i++)
              {
                      cin >> arr[i];
                      sum^=arr[i];
                      ans +=arr[i];
                      m = min(m , arr[i]);
              }
              if(sum) cout <<"Case #" << kase << ": NO\n" ;
              else  cout <<"Case #" << kase << ": " << ans - m <<endl;
    }
    return 0;
}
