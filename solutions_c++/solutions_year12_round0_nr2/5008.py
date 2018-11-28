#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<cmath>
#include<map>
using namespace std;

int main()
{
    int t,a,count = 0;
    ifstream fin("B-large.in");
    ofstream fout("out.in");
    fin>>t;
    int ans = 0;
    while(t--)
    {
              int n1,n2,n3;
              fin>>n1>>n2>>n3;
              ans = 0;
              for (int i =0; i < n1; i++)
              {
                  fin>>a;
                  int b = a/3;
                  int c = a%3;
                  if (b >= n3)
                  {
                        ans++;
                        continue;
                  }
                  if (n3 - b == 1 && c >= 1)
                  {
                        ans++;
                        continue;
                  }
                  if (n3 - b == 2 && c > 1 && n2 > 0)
                  {
                        ans++;
                        n2--;
                        continue;
                  }
                  if (n3 - b == 1 && n2 > 0 && b > 0)
                  {
                         ans++;
                         n2--;
                  }
              }
              count++;
              fout<<"Case #"<<count<<": "<<ans<<endl;
    }
    // system("pause");
    return 0;
}

// 1 QFT 1 QF 7 FAQFDFQ
