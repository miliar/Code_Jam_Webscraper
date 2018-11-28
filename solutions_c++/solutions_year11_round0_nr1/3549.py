#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

int main()
{
    ifstream in;
    in.open("A-large.in");
    
    ofstream out;
    out.open("output.txt");
    
    int noc=0;
    in >> noc;
    
    for (int i=1; i<=noc; i++)
    {
        out << "Case #" << i << ": " ;
        int n=0;
        in >> n;
        
        char arr[n];
        int pos[n];
        
        for (int j=0; j<n; j++)
        {
            in >> arr[j] >> pos[j] ;
        }
/*      for (int j=0; j<n; j++)
        {
            cout << arr[j] << " " << pos[j] << "\n" ;
        }
*/        
        int opos=1, bpos=1;
        int otime=0, btime=0;
        int ans=0;
        
        for (int j=0; j<n; j++)
        {
            if (arr[j] == 'O')
            {
                int curro = abs(pos[j]-opos)+1;
                opos = pos[j];
                
                otime += curro;
                if (btime >= otime)
                {
                   ans = btime+1;
                   otime = ans;
                }
                else
                {
                    ans = otime;
                }
            }
            
            if (arr[j] == 'B')
            {
               int currb = abs(pos[j]-bpos)+1;
               bpos = pos[j];
               
               btime += currb;
               if (otime >= btime)
               {
                  ans = otime+1;
                  btime = ans;          
               }
               else
               {
                   ans = btime;    
               }
            } 
        }
        out << ans << "\n" ;
    }


    return 0;
}
