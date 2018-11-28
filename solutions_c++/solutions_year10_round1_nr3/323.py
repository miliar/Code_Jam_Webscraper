#include <iostream>
#include <fstream>

using namespace std;


int main()
{
     ifstream fin("D:\C-small-attempt0.in");
    ofstream fout("D:\C-small-attempt0.out");
    int T, A1, A2, B1, B2;

    fin >> T;
    for (int i = 1 ; i <= T ; i++)
    {    
        int ans = 0;
        fin >> A1 >> A2 >> B1 >> B2;
        for (int aa = A1 ; aa <= A2 ; aa++) 
            for (int bb = B1 ; bb <= B2 ; bb++)
            {
                int a = aa;
                int b = bb;
                int check = 0;
                int temp = 0;
                while (true)
                {                      
                      if (a > b)
                      {
                         temp = a/b;
                         if (temp > 1) break;
                         check++;
                         a = a %b;                   
                      }
                      else if (a <= b)
                      {
                         temp = b/a;
                         if (temp > 1) break;                         
                         check++;
                         b = b %a;
                         if ( b == 0) break;
                      }                    
                }
                if (check % 2 == 0) ans++;
            }
              
        
        fout << "Case #" << i << ": " << ans << endl;  
    }
}
