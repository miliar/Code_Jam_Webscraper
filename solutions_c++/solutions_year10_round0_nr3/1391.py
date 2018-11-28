#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

vector<long long> sizes;
vector<long long> next;
vector<long long> stane;

int main()
    {
    int tc;
    cin >> tc;
    for( int t = 0; t < tc; ++t )
         {
         long long rj = 0;
         long long R, k, N;
         cin >> R >> k >> N;
         sizes.clear();
         sizes.resize(N);
         next.clear();
         next.resize(N,-1);
         stane.clear();
         stane.resize(N,0);
         for( int i = 0; i < N; ++i ) 
              cin >> sizes[i];
         
         for( int i = 0; i < N; ++i ) 
              {
              long long sum = sizes[i];
              long long p = ( i + 1 ) % N;
              while ( sum + sizes[p] <= k && p != i )
                    {
                    sum += sizes[p];
                    p = ( p + 1 ) % N;      
                    }
              stane[i] = sum;
              next[i] = p;
              }
         
         //cout << "debug" << endl;
         //for( int i = 0; i < N; ++i ) 
         //     {
         //     cout << i << " " << stane[i] << " " << next[i] << endl;    
         //     }
         //cout << endl;
         long long zarada_ciklus=0;
         long long duzina_ciklus=0;
         int bio[1010] = { -1 };
         for( int i = 0; i < 1010; ++i ) bio[i] = -1;
         long long s_c[1010];
         long long d_c[1010];
         int p = 0; long long suma = 0; int cnt = 0;
         while ( bio[p] == -1 ) 
               {
               s_c[p] = suma;
               d_c[p] = cnt;
               bio[p]= cnt;
               ++cnt;
               suma += stane[p];
               p = next[p];
               }
         duzina_ciklus = cnt - d_c[p];
         zarada_ciklus = suma - s_c[p];
         long long pocetni_dio = d_c[p];
         long long pocetna_zarada = s_c[p];
         
         //cout << duzina_ciklus << " " << zarada_ciklus << endl;
         //cout << pocetni_dio << " " << pocetna_zarada << endl;
         
         if ( R <= pocetni_dio ) 
            {
            int pos = 0;
            for( int i = 0; i < R; ++i )
                 { rj += stane[pos]; pos = next[pos]; } 
            }
         else
             {
             rj = pocetna_zarada + zarada_ciklus*( (R - pocetni_dio)/duzina_ciklus);
             int pos = p;
             for( int i = 0; i < ((R-pocetni_dio)%duzina_ciklus); ++i ) 
                  { rj += stane[pos]; pos = next[pos]; } 
             }
         cout << "Case #" << t + 1 << ": " << rj << endl; 
         }     
    return 0;
    }
