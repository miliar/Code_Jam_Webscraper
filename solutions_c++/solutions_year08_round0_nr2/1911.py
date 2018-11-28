#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

class voznja
{
      public:
      int polazak, dolazak;
      char otkud;
      
      voznja ()
      {
             polazak = 0;
             dolazak = 0;
             otkud = '?';
      } 
      
      voznja (int v1, int v2, char p)
      {
             polazak = v1;
             dolazak = v2;
             otkud = p;
      }    
      
      friend bool operator < (const voznja &a, const voznja &b)
      {
           if (a.polazak < b.polazak)
              return true;
           else
              return false;
      }           
};                  

int main()
{
    int N; 
    scanf ("%d", &N);
    
    for (int k = 0; k < N; k++)
    {
        int A = 0, B = 0;
        vector <voznja> put;
        vector <int> Ardy, Brdy;  //vlakovi u A i B koji su spremni za krenut u neko vrijeme
        int t;
        int Na, Nb;
        
        scanf ("%d", &t);
        scanf ("%d %d", &Na, &Nb);
        
        for (int i = 0; i < Na; i++)
        {
            int v1 = 0, v2 = 0;
            string s1, s2;
            cin >> s1 >> s2;
            
            v1 = ((s1[0]-'0')*10+(s1[1]-'0'))*60 + (s1[3]-'0')*10+(s1[4]-'0');
            v2 = ((s2[0]-'0')*10+(s2[1]-'0'))*60 + (s2[3]-'0')*10+(s2[4]-'0');
            
            voznja tmp (v1,v2,'A');
            put.push_back(tmp);     
        }    
        
        for (int i = 0; i < Nb; i++)
        {
            int v1 = 0, v2 = 0;
            string s1, s2;
            cin >> s1 >> s2;
            
            v1 = ((s1[0]-'0')*10+(s1[1]-'0'))*60 + (s1[3]-'0')*10+(s1[4]-'0');
            v2 = ((s2[0]-'0')*10+(s2[1]-'0'))*60 + (s2[3]-'0')*10+(s2[4]-'0');
            
            voznja tmp (v1,v2,'B');
            put.push_back(tmp);     
        }    
            
        sort(put.begin(), put.end());        
        //sad u vectoru put imam voznje kako idu po redu
        //sad ih treba po redu pogledat i za svaku odabrat najraniji vlak, ako ga nema
        //onda reci jos jednom da od tamo krece    
        
        for (int i = 0; i < put.size(); i++)
        {
            if (put[i].otkud == 'A')
            {
               if ((Ardy.size() > 0) && (Ardy[0] <= put[i].polazak))
               {
                  Brdy.push_back(put[i].dolazak+t);
                  sort(Brdy.begin(),Brdy.end());
                  Ardy.erase(Ardy.begin());
               }
               else
               {
                  Brdy.push_back(put[i].dolazak+t);
                  A++;
               }
            }        
            if (put[i].otkud == 'B')
            {
               if ((Brdy.size() > 0) && (Brdy[0] <= put[i].polazak))
               {
                  Ardy.push_back(put[i].dolazak+t);
                  sort(Ardy.begin(),Ardy.end());
                  Brdy.erase(Brdy.begin());
               }
               else
               {
                  Ardy.push_back(put[i].dolazak+t);
                  B++;
               }
            }
        }
        
        cout << "Case #" << k+1 << ": " << A << " " << B << endl;
    }
    
    return 0;
}                     
        
        
        
        
        
        
        
        
        
        
        
          
             
             
