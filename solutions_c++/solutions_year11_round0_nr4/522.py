#include<cstdio>
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
    int kase =0 ;
    while(t--)
    {
              kase++;
              
              int n;
              cin>>n;
              int count  =0;
              for(int i = 0; i < n ;i++)
              {
                      int a;
                      cin >> a;
                      if(i != a-1) count++;
              }
              
              cout << "Case #" << kase <<": " ;
              printf("%.7f\n",(float)count);
    }
    
    return 0;
}
