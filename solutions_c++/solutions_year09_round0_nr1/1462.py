#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool Jednaki (string rijec, string poruka)
{
     int p = 0;
     for (int i = 0; i < rijec.length(); i++)
     {
         if (poruka[p] != '(')
         {
            if (poruka[p] != rijec[i])
               return false;
            p++;
         }
         else
         {
            p++;
            bool odgovara = false; 
            for(; poruka[p] != ')'; p++)
                  if (poruka[p] == rijec[i])
                     odgovara = true;
            p++;
            if (odgovara == false)
               return false;
         }
     }
     return true;      
}

int main()
{
    int N, L, D; 
    scanf ("%d %d %d", &L, &D, &N);
    vector <string> rijec(D);
    
    for (int i = 0; i < D; i++)
        cin >> rijec[i];
    
    for (int t = 0; t < N; t++)
    {
        int rj = 0;
        string poruka;
        cin >> poruka;
        
        for (int i = 0; i < D; i++)
            if ( Jednaki(rijec[i],poruka) )
               rj++;
        
        cout << "Case #" << t+1 << ": " << rj << endl;
    }
    
    //system ("pause");
    return 0;
}
            
    
