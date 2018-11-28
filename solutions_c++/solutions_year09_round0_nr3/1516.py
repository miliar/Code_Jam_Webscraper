#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int N;
    scanf("%d\n", &N);
    for (int n = 0; n < N; n++)
    {
        string text;
        getline(cin,text);
        
        vector <int> komb (19,0);
        vector <bool> moze (19,false);
        
        for (int i = 0; i < text.size(); i++)
        {
            if (text[i] == 'w')
            {
               komb[0] = (komb[0]+1)%10000;
               moze[0] = true;
            }
            
            if (text[i] == 'e')
            {
               if (moze[13])
               {
                  komb[14] = (komb[14] + komb[13])%10000;
                  moze[14] = true;
               }
               if (moze[5])
               {
                  komb[6] = (komb[6] + komb[5])%10000;
                  moze[6] = true;
               }
               if (moze[0])
               {
                  komb[1] = (komb[1] + komb[0])%10000;
                  moze[1] = true;
               }
            }
            
            if (text[i] == 'l')
               if (moze[1])
               {
                  komb[2] = (komb[2] + komb[1])%10000;
                  moze[2] = true;
               }
               
            if (text[i] == 'c')
            {
               if (moze[10])
               {
                  komb[11] = (komb[11] + komb[10])%10000;
                  moze[11] = true;
               }
               if (moze[2])
               {
                  komb[3] = (komb[3] + komb[2])%10000;
                  moze[3] = true;
               }
            }
            
            if (text[i] == 'o')
            {
               if (moze[11])
               {
                  komb[12] = (komb[12] + komb[11])%10000;
                  moze[12] = true;
               }
               if (moze[8])
               {
                  komb[9] = (komb[9] + komb[8])%10000;
                  moze[9] = true;
               }
               if (moze[3])
               {
                  komb[4] = (komb[4] + komb[3])%10000;
                  moze[4] = true;
               }
            }
            
            if (text[i] == 'm')
            {
               if (moze[17])
               {
                  komb[18] = (komb[18] + komb[17])%10000;
                  moze[18] = true;
               }
               if (moze[4])
               {
                  komb[5] = (komb[5] + komb[4])%10000;
                  moze[5] = true;
               }
            }
            
            if (text[i] == ' ')
            {
               if (moze[14])
               {
                  komb[15] = (komb[15] + komb[14])%10000;
                  moze[15] = true;
               }
               if (moze[9])
               {
                  komb[10] = (komb[10] + komb[9])%10000;
                  moze[10] = true;
               }
               if (moze[6])
               {
                  komb[7] = (komb[7] + komb[6])%10000;
                  moze[7] = true;
               }
            }
            
            if (text[i] == 't')
            {
               if (moze[7])
               {
                  komb[8] = (komb[8] + komb[7])%10000;
                  moze[8] = true;
               }
            }
            
            if (text[i] == 'd')
            {
               if (moze[12])
               {
                  komb[13] = (komb[13] + komb[12])%10000;
                  moze[13] = true;
               }
            }
            
            if (text[i] == 'j')
            {
               if (moze[15])
               {
                  komb[16] = (komb[16] + komb[15])%10000;
                  moze[16] = true;
               }
            }
            
            if (text[i] == 'a')
            {
               if (moze[16])
               {
                  komb[17] = (komb[17] + komb[16])%10000;
                  moze[17] = true;
               }
            }
        }
        
        cout << "Case #" << n+1 << ": ";
        if (komb[18] < 10) cout << "0";
        if (komb[18] < 100) cout << "0";
        if (komb[18] < 1000) cout << "0";
        cout << komb[18] << endl;
    }
    
    //system ("Pause");
    return 0;
}
        
            
            
            
            
               
        
        
