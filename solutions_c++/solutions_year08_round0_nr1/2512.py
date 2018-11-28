#include<iostream>
#include<string>
#include<vector>
#include<map>

using namespace std;

int main()
{
   int cases;
   cin >> cases;
   int i,j,k;
   for(int i = 1; i <= cases; i++)
   {
      int S,Q,switcch=0;
      vector<string> engines;
      vector<string> queries;
      map<string, int> selected;
      string engine;

      cin >> S;
      cin.ignore();
      j = S;
      for(j = 0; j < S; j++)
      {
         getline(cin,engine);
         engines.push_back(string(engine));
         selected[engine] = 0;
      }

      cin >> Q;
      cin.ignore();
      j = Q;
      //Input taken.
      //Greedy algo. Take the engine which comes in last in the query.
      //
      for(j = 0; j < Q; j++)
      {
         getline(cin,engine);
         queries.push_back(engine);
      }
      for(j = 0; j < Q; j++)
      {
         selected[queries[j]]++;
         for (k = 0; k < S; k++)
            if (!selected[engines[k]])
               break;
         //Found the first instance
         if (k == S)
         {
            switcch++;
            for (k = 0; k < S; k++)
               selected[engines[k]] = 0;
            j--;
         }
      }
      cout << "Case #" << i << ": " << switcch << endl;
   }
}
