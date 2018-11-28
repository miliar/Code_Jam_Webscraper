#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long

using namespace std;

int main()
{
   ifstream entrada("A-large.in");
   ofstream saida("A-large.out");
   vector<ll> freq;
   //vector<long> touches;

   int ncases;

   entrada >> ncases;

   for (int ccase = 1; ccase <= ncases; ccase++){
       ll p, k, l;
       
       entrada >> p >> k >> l;
       
       for (ll i = 0; i < l; i++){
           ll f;
           entrada >> f;
           freq.push_back(f);
           //touches.push_back(0);
       }
       
       sort(freq.begin(), freq.end());
       reverse(freq.begin(), freq.end());
       
       // Calculates the no of touches
       ll tt = 0;
       for (ll i = 0; i < l; i++){
           //touches[i] = (i / k) + 1;
           //tt += touches[i] * freq[i];
           tt += ((i / k) + 1) * freq[i];
       }
       
       saida << "Case #" << ccase << ": " << tt;
       if (ccase < ncases)
           saida << endl;
       freq.clear();
   }

   saida.close();
   entrada.close();
   return 0;
}
