#include <iostream>
#include <vector>

using namespace std;

int main()
{
   int cases;
   int c = 1;
   cin >> cases;
   while(cases-- > 0)
   {
      int n, k;
      cin >> n >> k;
      vector<vector<char> > mat;
      for(int j = 0; j < n; j++)
      {
         vector<char> row;
         for(int i = 0; i < n; i++)
         {
            char ch;
	    cin >> ch;
            row.push_back(ch);
         }
         mat.push_back(row);
      }
 
      for(int kk = 0; kk < n; kk++)
      {
      for(int i = n-1; i > 0; i--)
      {
         for(int j = 0; j < n; j++)
         {
            if (mat[j][i] == '.' && mat[j][i-1] != '.')
            {
               mat[j][i] = mat[j][i-1];
               mat[j][i-1] = '.';
            }
         }
      }
      }

      

      bool r = false;
      bool b = false;

      for(int i = 0; i < n; i++)
      {
         for(int j = 0; j < n; j++)
         {
            bool found;
            found = true;
            for(int kk = 0; kk < k; kk++)
            {
               if (j+kk >= n || mat[i][j+kk] != 'R') { found = false; break; }
            }
            if (found) { r = true; }

            found = true;
            for(int kk = 0; kk < k; kk++)
            {
               if (i+kk >= n || mat[i+kk][j] != 'R') { found = false; break; }
            }
            if (found) { r = true; }

            found = true;
            for(int kk = 0; kk < k; kk++)
            {
               if (i+kk >= n || j+kk >= n || mat[i+kk][j+kk] != 'R') { found = false; break; }
            }
            if (found) { r = true; }

            found = true;
            for(int kk = 0; kk < k; kk++)
            {
               if (i+kk >= n || j-kk < 0 || mat[i+kk][j-kk] != 'R') { found = false; break; }
            }
            if (found) { r = true; }

         }
      }

      for(int i = 0; i < n; i++)
      {
         for(int j = 0; j < n; j++)
         {
            bool found;
            found = true;
            for(int kk = 0; kk < k; kk++)
            {
               if (j+kk >= n || mat[i][j+kk] != 'B') { found = false; break; }
            }
            if (found) { b = true; }

            found = true;
            for(int kk = 0; kk < k; kk++)
            {
               if (i+kk >= n || mat[i+kk][j] != 'B') { found = false; break; }
            }
            if (found) { b = true; }

            found = true;
            for(int kk = 0; kk < k; kk++)
            {
               if (i+kk >= n || j+kk >= n || mat[i+kk][j+kk] != 'B') { found = false; break; }
            }
            if (found) { b = true; }

            found = true;
            for(int kk = 0; kk < k; kk++)
            {
               if (i+kk >= n || j-kk < 0 || mat[i+kk][j-kk] != 'B') { found = false; break; }
            }
            if (found) { b = true; }

         }
      }

      if (r && b) cout << "Case #" << c++ << ": Both" << endl ;
      if (r && !b) cout << "Case #" << c++ << ": Red" << endl ;
      if (!r && b) cout << "Case #" << c++ << ": Blue" << endl ;
      if (!r && !b) cout << "Case #" << c++ << ": Neither" << endl ;
       
   }
}
