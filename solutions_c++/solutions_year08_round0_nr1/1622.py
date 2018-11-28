#include <iostream>
#include <vector>
#include <string>

using namespace std;

int diff(string a, string b)
{
   if (a == b) return 1;
   else return 0;
}

int solve(vector<string> &engines, vector<string> &queries)
{
   vector<vector<int> > mat(engines.size());
   if (queries.size() == 0) return 0;

   for(int i = 0; i < engines.size(); i++)
      mat[i].resize(queries.size(),0x7000001);

   for(int i = 0; i < engines.size(); i++)
   {
      mat[i][0] = diff(engines[i], queries[0]);
   }


   for(int i = 1; i < queries.size(); i++)
   {
      for(int j = 0; j < engines.size(); j++)
      {
         if (engines[j] == queries[i]) { mat[j][i] = 0x7000000; continue; }
         else
         {
            mat[j][i] = mat[j][i-1];

            for(int k = 0; k < engines.size(); k++)
               mat[j][i] = min(mat[j][i],mat[k][i-1]+1);
         }
      }
   }

/*   cout << endl;
   for(int i = 0; i < engines.size(); i++)
   {
      for(int j = 0; j < queries.size(); j++)
      {
         cout << mat[i][j] << " ";
      }
      cout << endl;
   }
*/


   int mv = 0x7000000;
   for(int i = 0; i < engines.size(); i++)
   {
      mv = min(mv,mat[i][queries.size()-1]);
   }
   return mv;
}

int main()
{
   cin >> cases;
   int c = 1;
   while (cases-- > 0)
   {
      vector<string> se;
      int ii;
      cin >> ii;
         string s;
         getline(cin,s);
      while (ii-- > 0)
      {
         getline(cin,s);
         se.push_back(s);
      }
      int iii;
      cin >> iii;
      vector<string> queries;
      getline(cin,s);
      while(iii-- > 0)
      {
         getline(cin,s);
         queries.push_back(s);
      }


      cout << "Case #" << c++ << ": ";
      int tmp = solve(se,queries);
      if (tmp != 0x7000000)      cout  << tmp << endl;
      else
        cout << queries.size()-1 << endl;
   }

   return 0;

}


