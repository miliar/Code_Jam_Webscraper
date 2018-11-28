/*
Theme Park
*/

#include <fstream>
#include <iostream>

   using namespace std;

   long long group[3000];
   int howfar[1000]; // howfar[i] = maximum index j such that sum{i ... j} <= k && sum{i ... (j + 1)} > k
   long long howmany[1000]; // howmany[i] = inclusive sum from group[i] ... howfar[i] (may have to go backwards...)
   int N, R, k;

   ofstream out ("coaster.out");

    void solve(int x)
   {
      //cout << endl << k << endl;
      out << "Case #" << (x + 1) << ": ";
   // compute howfar and howmany
      long long sofar = group[0];
      for(int i = 0; i < N; i++)
      {
         if(i > 0)
         {
            sofar -= group[i - 1];
            howfar[i] = howfar[i - 1];
         }
         //cout << sofar << endl;
         while(howfar[i] + 1 < N + i && sofar + group[howfar[i] + 1] <= k)
         {
            howfar[i]++;
            sofar += group[howfar[i]];
            //cout << sofar << endl;
         }
         howmany[i] = sofar;
         //cout << group[i] << ", " << howfar[i] % N << ", " << howmany[i] << endl;
      }
      for(int i = 0; i < N; i++)
         howfar[i] %= N;
      
   // brute force time!
      long long total = 0;
      int pos = 0;
      for(int i = 0; i < R; i++)
      {
         total += howmany[pos];
         pos = (howfar[pos] + 1) % N;
      }
      out << total << endl;
   }

    int main()
   {
      ifstream in ("coaster.in");
   
      int T;
      in >> T;
      for(int i = 0; i < T; i++)
      {
         cout << i << endl;
         in >> R >> k >> N;
         for(int j = 0; j < N; j++)
         {
            in >> group[j];
            group[j + N] = group[j];
         }
         howfar[0] = 0;
         solve(i);
      }
   
      return 0;
   }
