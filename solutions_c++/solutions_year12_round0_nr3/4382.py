#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <set>
#include <utility>

using namespace std;

int rotate(int num, int n)
{
  int digits = log10(num)+1;
  int mult   = pow(10, digits-1);
  for(int j=0; j<n; ++j)
  {
    int d = num%10;
    num /= 10;
    num = num + d*mult;
  }
  return num;
}

int main()
{
  string sn;
  getline(cin, sn);
  const int n = stoi(sn);
  for(int i=0; i<n; ++i)
  {
    int A, B;
    cin >> A >> B;
    cin.ignore();
    
    cout << "Case #" << i+1 << ": ";
    
    int nCount = 0;
    int digits = log10(B)+1;
    std::set<pair<int,int>> rots;
    for(int n=A; n<B-1; ++n)
    {
      for(int m=n+1; m<=B; ++m)
      {
        for(int r=1; r<digits; ++r)
        {
          int C = rotate(n,r);
          //cout << "n: " << n << "\tm: " << m << "\tC: " << C << endl;
          if(C == m)
          {
            rots.insert(make_pair(n, C));
//          cout << "n: " << n << "\tm: " << m << "\tC: " << C << endl;
          }
        }
      }
    }
    cout << rots.size() << endl;
  }

  return 0;
}

