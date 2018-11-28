#include <cstdlib>
#include <iostream>
#include <string>
#include <list>

using namespace std;

int findnextnumber(int n, int c);

int main(int argc, char *argv[])
{
    // Input Number of Cases
    int cases;
    cin >> cases;
    
    for(int i = 0;i<cases;i++)  // For Each Case
            {
                cout << "Case #" << i + 1 << ": ";
                
                // Input Number
                int n;
                cin >> n;
                
                int c;
                c = n;
                
                
                list<int> ndigits;      
                list<int> cdigits;                
                
                int t;

                t = n;
                while(t>0)
                          {
                                  ndigits.push_back(t%10);
                                  t = (t - t%10) / 10;
                          }
                ndigits.remove(0);
                ndigits.sort();

                while(ndigits!=cdigits)
                {
                cdigits.clear();
                c++;
                t = c;   
                while(t>0)
                          {
                                  cdigits.push_back(t%10);
                                  t = (t - t%10) / 10;
                          }
                cdigits.remove(0);
                cdigits.sort();  
                
                
                }
                cout << c << endl;
            }
    
    return 0;
}
