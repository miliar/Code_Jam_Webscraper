#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int abs(int x)
{
   if (x < 0) return x * -1;
   else return x;

}

int main()
{
  int cases, c=1;
  cin >> cases;

  while (cases-- > 0)
  {
    int d, in, m, n;
    cin >> d >> in >> m >> n;
    vector<int> as;
    for(int i = 0; i < n; i++)
    {
       int t;
       cin>> t;
       as.push_back(t);
    }

    int dp[n+1][256];
    for(int i = 0; i < n+1; i++)
    {
       for(int j = 0; j < 256; j++)
       {
           dp[i][j] = 1000000000;
       }
    }
    for(int i = 0; i < 256; i++)
    {
       dp[0][i] = 0;
    }

    for(int i = 1; i < n+1; i++)
    {
       for(int j = 0; j < 256; j++)
       {          
           for(int k = 0; k < 256; k++)
           {
              // insert cost = ceil(double(j-k)/m)*in
              if (abs(k-j) <= m)            
              {
                 dp[i][j] = min(dp[i][j], dp[i-1][k]+abs(j-as[i-1]));
                 dp[i][j] = min(dp[i][j], dp[i-1][k]+d);
              }
              else if (m != 0)
              {
                 dp[i][j] = min(dp[i][j], dp[i-1][k]+(int(ceil(double(abs(j-k))/m))-1)*in + abs(j-as[i-1]));
                 dp[i][j] = min(dp[i][j], 255+dp[i-1][k]+(int(ceil(double(abs(j-k))/m))-1)*in);
 
              }
              
           }
       }
    }

    for(int i = 0; i <= n; i++)
    {
     for( int j = 0; j < 256; j++)
     {
//        cout << dp[i][j] << " ";
     }
  //   cout << endl;
    }


    int mm = 1000000000;
    for(int i = 0; i < 256; i++)
    {
        mm = min(mm,dp[n][i]);
    }
    cout << "Case #" << c++ <<": " << mm << endl; 

    

  }

}
