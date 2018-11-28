#include <iostream>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;

int S, Q, prom, kol;
vector <string> servis (1000);
vector <bool> isk (1000,false);

void iskoristi (string s)
{
     for (int i = 0; i < S; i++)
         if (servis[i] == s)
         {
            if (isk[i] == false)
               kol++;
            isk[i] = true;
            break;
         }
}

void resetiraj (int x)
{
     for (int i = 0; i < x; i++)
         isk[i] = false;
     kol = 0;
     prom++;    
}

                  

int main()
{
    int N;
    scanf ("%d\n", &N);
    vector <int> rj;
    
    for (int k = 0; k < N; k++)
    {      
        resetiraj (1000);
        prom = 0; kol = 0;
           
             
        scanf ("%d\n", &S);
        for (int i = 0; i < S; i++)
            getline(cin,servis[i]);
            
        scanf ("%d\n", &Q);        
        for (int i = 0; i < Q; i++)
        {
            string tmp;
            getline(cin,tmp);
            
            iskoristi(tmp);
            if (kol == S)
            {
               resetiraj(S);
               iskoristi(tmp);
            }
        }
        
        rj.push_back(prom);
    }
    
    for (int i = 0; i < N; i++)
        cout << "Case #" << i+1 << ": " << rj[i] << endl;
    
    return 0;
}                  
               
            
            
            
            
            
            
            
            
            
                        
    
    
