/*
Number Game
*/

#include <iostream>
#include <fstream>

   using namespace std;

/*
Discovery:
given the value of A, you lose if start[A] <= B < start[A] + A, where start[A] follows a cool pattern;
i have no idea why this is true (or if this is actually correct)
*/


   int start[1000001];
   int bit[1000001]; // binary indexed tree

    void update(int idx, int val)
   {
      while(idx <= 1000000)
      {
         bit[idx] += val;
         idx += (idx & -idx);
      }
   }
   
    int read(int idx)
   {
      int sum = 0;
      while(idx > 0)
      {
         sum += bit[idx];
         idx -= (idx & -idx);
      }
      return sum;
   }

    // int readSingle(int idx)
   // {
      // int sum = bit[idx];
      // if(idx > 0)
      // {
         // int z = idx - (idx & -idx);
         // idx--;
         // while(idx != z)
         // {
            // sum -= bit[idx];
            // idx -= (idx & -idx);
         // }
      // }
   // }

    long long max(long long a, long long b)
   {
      if(a > b)
         return a;
      else
         return b;
   }

    int main()
   {
      ifstream in ("ngame.in");
      ofstream out ("ngame.out");
   
      // calculate start
      start[1] = 1;
      update(1, 1);
      update(2, -1);
      for(int i = 2; i <= 1000000; i++)
      {
         if(i % 1000 == 0)
            cout << i << endl;
      	// check last start
         if(read(start[i - 1]) == start[i - 1])
            start[i] = start[i - 1] + 1;
         else
            start[i] = start[i - 1];
         update(start[i], 1);
         update(start[i] + i, -1);
      }
   
      int T;
      in >> T;
      for(int i = 0; i < T; i++)
      {
         cout << i << endl;
         long long A1, A2, B1, B2;
         in >> A1 >> A2 >> B1 >> B2;
         out << "Case #" << (i + 1) << ": ";
         long long countfail = 0;
         for(int row = A1; row <= A2; row++)
         {
            long long s = start[row]; // INCLUSIVE
            long long e = start[row] + row - 1; // ALSO INCLUSIVE
            int ss = max(s, B1);
            int ee = min(e, B2);
            //cout << ss << ", " << ee << endl;
            if(ee >= ss)
               countfail += (ee - ss + 1);
         }
         long long total = (A2 - A1 + 1) * (B2 - B1 + 1);
         out << total - countfail << endl;
      }
   
      return 0;
   }
   

/*
   bool w[1001][1001];
    int main()
   {
      ifstream in ("ngame.in");
      ofstream out ("ngame.out");
   
      for(int i = 0; i <= 1000; i++)
         w[i][0] = w[0][i] = true;
   
      for(int i = 1; i <= 1000; i++)
         for(int j = 1; j <= i; j++)
         {
            for(int k = j - i; k >= 0; k -= i)
               if(!w[i][k])
                  w[i][j] = true;
            for(int k = i - j; k >= 0; k -= j)
               if(!w[k][j])
                  w[i][j] = true;
            w[j][i] = w[i][j];
         }
         
      for(int i = 1; i <= 1000; i++)
      {
         for(int j = 1; j <= 1000; j++)
            if(i == j)
            	out << "W";
            else if(w[i][j])
               out << ".";
            else
               out << w[i][j];
         out << endl;
      }
   
      int T;
      in >> T;
      // for(int i = 0; i < T; i++)
      // {
      // 	
      // }
   
      return 0;
   }
   */


