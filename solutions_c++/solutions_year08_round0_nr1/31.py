#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>

using namespace std;

#define PB push_back
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define MSG(a) cout << #a << " = " << a << endl;


int main()
{
   ofstream fout;
   fout.open("output.txt");
   ifstream fin("A-large.in");
    
   int N;
   fin >> N;
   
   FOR(k,1,N+1)
   {
      int s;
      fin >> s;
      vector<string> engines;
      FOR(t,0,s)
      {
         string tmp;
         if(t == 0) getline(fin,tmp);
         getline(fin,tmp);
         engines.PB(tmp);
      }
      
      int ans = 0;
      
      int l;
      fin >> l;
      
      set<string> E;
      set<string> TMP;
      
      FOR(t,0,l)
      {
         string tmp;
         if(t == 0) getline(fin,tmp);
         getline(fin,tmp);
         TMP.insert(tmp);
         if(TMP.size() == engines.size())
         {
            ans++;
            E.clear();
            E.insert(tmp);
            TMP.clear();
            TMP.insert(tmp);
         }
         else
         {
            E.insert(tmp);
         }
      }
      
      fout << "Case #" << k << ": " << ans << endl;
      
      
      
      
   }
   
   return 0; 
    
    
    
    
    
    
}

