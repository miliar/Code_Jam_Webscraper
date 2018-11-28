#include <iostream>
#include <cmath>
using namespace std;
int fO,fB;
int tn,n;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i;
  
    cin >> tn;
    for (int t=1;t<=tn;t++)
    {
        char ch;
        int po=1,pb=1,pos;
        fO=fB=0;
        
          cin >> n;
          cin.get();
          for (i=0;i<n;i++)
          {
              cin >> ch;
              cin >> pos;
              cin.get();
              
              if (ch=='O')
              {
                  fO = max(fO+abs(pos-po)+1,fB+1);
                  po = pos;
              }
              else
              {
                  fB = max(fB+abs(pos-pb)+1,fO+1);
                  pb = pos;
              }
          }
          cout << "Case #" << t << ": " << max(fO,fB) << endl;
    }
}
