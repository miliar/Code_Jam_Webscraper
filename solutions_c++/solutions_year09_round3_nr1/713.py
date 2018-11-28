#include <iostream>
#include <vector>
#include <string>

using namespace std;

long long pot (int a, int x)
{
     long long rj = 1;
     for (int i = 0; i < x; i++)
         rj *= a;
     return rj;
}

int main()
{
    int T;
    cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        string rijec;
        cin >> rijec;
        vector <int> prijevod (rijec.length(),-1);
        
        int znam = 1;
        bool Isk0 = false;
        
        for (int i = 0; i < rijec.length(); i++)
            if (rijec[i] != '#')
               if ((i > 0) && (Isk0 == false))
               {
                  Isk0 = true;
                  char slovo = rijec[i];
                  for (int j = i; j < rijec.length(); j++)
                      if (rijec[j] == slovo)
                      {
                         prijevod[j] = 0;
                         rijec[j] = '#'; 
                      }
               }
               else
               {
                   char slovo = rijec[i];
                   for (int j = i; j < rijec.length(); j++)
                       if (rijec[j] == slovo)
                       {
                          prijevod[j] = znam;
                          rijec[j] = '#'; 
                       }
                   znam++;
               }
        
        long long rj = 0;
        for (int i = 0; i < prijevod.size(); i++)
            rj += pot(znam,prijevod.size()-i-1)*prijevod[i];
        
        cout << "Case #" << t << ": " << rj << endl;
    }
    //system ("pause");
    return 0;
}
                         
                      
               
        
