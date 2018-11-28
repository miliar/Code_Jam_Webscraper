#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int main()
{
  freopen("A-large.in.txt","r",stdin);
  freopen("A-large.out","w",stdout);
  int l,t,n,k,x,i,d,c;
    // char c;
  char dump;

  cin >> t;
  for (l=0;l<t;l++)
  {
    cin >> n;
    vector<vector<char> > mat;
    mat.resize(n, vector<char>(n, '.'));
    vector<int> tot(n,0);
    vector<int> win(n,0);
    vector<int> loss(n,0);
    
    for (int i = 0; i < n; ++i)
    {
      string row;
      cin >> row;
      for (int j = 0; j < n; ++j)
      {
        mat[i][j] = row[j];
        if (row[j] != '.')
        {
          tot[i]++;
          if (row[j] == '0')
          {
            loss[i]++;
          }
          else
          {
            win[i]++;
          }
        }
      }
    }
    vector<double> wp(n,0.0);
    vector<double> owp(n,0.0);
    vector<double> oowp(n,0.0);
    vector<double> rpi(n,0.0);
    
    for (int i = 0; i < n; i++)
    {
      wp[i] = (double)(win[i])/tot[i];
    }

    // owp
    for (int i = 0; i < n; i++)
    {
      double sum = 0.0;
      for (int j = 0; j < n; j++)
      {
        if (mat[i][j] != '.')
        {
          if (mat[i][j] == '0')
            sum += (double)(win[j]-1)/(tot[j]-1);
          else
          {
            sum += (double)(win[j])/(tot[j] -1);
          }
        }
      }
      owp[i] = sum/tot[i];
    }

    // oowp
    for (int i = 0; i < n ; i++)
    {
      double sum = 0.0;
      for (int j = 0; j < n; j++)
      {
        if (mat[i][j] != '.')
        {
          sum += owp[j];
        }
      }
      
      oowp[i] = sum/tot[i];
    }
    
    cout << "Case #" << l+1 << ": " << endl;
    
    for (int i = 0; i < n; i++)
    {
      rpi[i] = 0.25*wp[i]+0.5*owp[i] +0.25*oowp[i];
      cout << rpi[i] << endl;
    }

  }
	return 0;
}

