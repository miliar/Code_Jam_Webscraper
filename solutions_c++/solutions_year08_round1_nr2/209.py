#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <cstdio>
using namespace std;

enum Flavor_State
{
   FLAVOR_UNMALT = 0,
   FLAVOR_MALT,
   FLAVOR_UNKNOWN
};

void extractans(int);

int main(void)
{
   int c;
   cin >> c;
   for(int i = 1; i <= c; ++i)
   {
      cout << "Case #" << i << ":";
      int n; // |flavors|
      cin >> n;

//      vector<Flavor_State> flavors(n, FLAVOR_UNKNOWN);

      int m; // |customer|
      cin >> m;
      vector<vector<Flavor_State> > prefs;
      vector<Flavor_State> single_pref;
      for(int j = 0; j < m; ++j)
      {
         single_pref.clear();
         single_pref.resize(n, FLAVOR_UNKNOWN);
         int t; // |preference|
         cin >> t;
         for(int k = 0; k < t; ++k)
         {
            int id;
            int ismalted;
            cin >> id >> ismalted;
            single_pref[id - 1] = (ismalted?FLAVOR_MALT:FLAVOR_UNMALT);
         }
         prefs.push_back(single_pref);
      }

      ofstream pbprob("tbs.opb");
      //objective
      pbprob << "min:";
      for(int j = 0; j < n; ++j)
      {
         pbprob << " +1 x" << j;
      }
      pbprob << " ;\n";

      // constraints
      for(int j = 0; j < m; ++j)
      {
         int rhs = 1;
         for(int k = 0; k < n; ++k)
         {
            if(prefs[j][k] == FLAVOR_MALT)
            {
               pbprob << "+1 x" << k << " ";
            }
            else if(prefs[j][k] == FLAVOR_UNMALT)
            {
               pbprob << "-1 x" << k << " ";
               --rhs;
            }
         }
         pbprob << ">= " << rhs << " ;\n";
      }

      pbprob.close();
      system("./Pueblo tbs.opb > pb.result");
      extractans(n);
   }
   return 0;
}

void extractans(int n)
{
   ifstream pb_result("pb.result");
   if(!pb_result)
   {
      cout << " IMPOSSIBLE\n";
      return;
   }

   string buf;
   while(getline(pb_result, buf))
   {
      if(buf[0] == 'c' || buf[0] == 'o')
         continue;

      if(buf[0] == 's')
      {
         istringstream strm(buf);
         string tmp;
         strm >> tmp; // "s"
         strm >> tmp;
         if(tmp == "UNSATISFIABLE" || tmp == "UNKNOWN")
         {
            cout << " IMPOSSIBLE\n";
            return;
         }
      }

      if(buf[0] == 'v') // parse solution
      {
         vector<int> ans(n, 0);
         istringstream strm(buf);
         string tmp;
         strm >> tmp; // "v"
         while(strm >> tmp)
         {
            if(tmp[0] != '-')
            {
               int id;
               sscanf(tmp.c_str(), "x%d", &id);
               ans[id] = 1;
            }
         }
         for(int i = 0; i < n; ++i)
            cout << " " << ans[i];
         cout << endl;
         return;
      }
   }
}
