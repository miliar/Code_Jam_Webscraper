#include <stdio.h>
#include <iostream>
#include <fstream>

#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#define forn(i, n) for (int i = 0; i<(int) n; i++)
using namespace std;
int main(){
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int test;
  cin>>test;
  forn(tests, test)
  {
    int n;
    cin>>n;
    int rw[100]; int s[100];
    forn(i, n)
    {
      int ls = 0;
      string ts;
      cin>>ts;
      forn(j, n)
        if (ts[j] == '1')
          ls = j;
      
      rw[i] = ls;
  //    cout<<rw[i]<<endl;
    }
    int ans = 0;
    forn(i, n)
    {
      if (rw[i]>i)
      {
//        cout<<i<<"Ssdfsdf"<<endl;
        for(int j = i+1; j<n; j++)      
          if (rw[j]<=i)
          {
            int tmp = rw[j];

            for(int k = j-1; k>=i; k--)
            {
              rw[k+1] = rw[k];
              ans++;
            }
            rw[i] = tmp;
           /* cout<<endl;
            forn(ii, n)
              cout<<rw[ii]<<endl;         
            cout<<ans<<endl;*/
            break;
          }
      }
    }
    cout<<"Case #"<<tests+1<<": "<<ans<<endl;
  }
  return 0;
}
