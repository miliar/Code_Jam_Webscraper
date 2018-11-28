// A lovely code!
#include <iostream>
#include <vector>
#include <ctime>
#include <string>
#include <cmath>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("minn.in");
    ofstream fout("output.txt");
    
    int t,q;
    fin>>t;
    q=0;
    while(t--)
    {
              int n,k;
              fin>>n>>k;
              int j;
              q++;
              fout<<"Case #"<<q<<": ";        
              int p= k & (int(pow(2,float(n)))-1);
              for(j=0; j<n; j++)
              {
                        if(p%2==0)break;
                        p=p>>1;
              }
              if(!p && j==n)
              {
                    fout<<"ON\n";
//                      printf("ON\n");
              }
              else
                  fout<<"OFF\n";
    }                    
    cin.get();
    cin.ignore();
    return 0;
}
