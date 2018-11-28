#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

#define PB push_back
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define MSG(a) cout << #a << " = " << a << endl;
#define SORT(a) sort(a.begin(),a.end())


int main()
{
   ofstream fout;
   fout.open("output.txt");
   ifstream fin("B-large.in");
    
   int N;
   fin >> N;
   
   FOR(MM,1,N+1)
   {
      int T,NA,NB;
      fin >> T >> NA >> NB;
      
      vector<int> start;
      vector<int> finish;
      vector<int> locStart;
      
      FOR(p,0,NA)
      {
         string first,second;
         fin >> first >> second;
         start.PB(((first[0]-'0')*10 + (first[1]-'0'))*60 + (first[3]-'0')*10 + (first[4]-'0'));
         finish.PB(((second[0]-'0')*10 + (second[1]-'0'))*60 + (second[3]-'0')*10 + (second[4]-'0'));
         locStart.PB(0);
      }
      FOR(q,0,NB)
      {
         string first,second;
         fin >> first >> second;
         start.PB(((first[0]-'0')*10 + (first[1]-'0'))*60 + (first[3]-'0')*10 + (first[4]-'0'));
         finish.PB(((second[0]-'0')*10 + (second[1]-'0'))*60 + (second[3]-'0')*10 + (second[4]-'0'));
         locStart.PB(1);
      }      
      
      FOR(k,0,start.size())
      FOR(l,0,k)
      if(start[l] > start[k])
      {
         swap(start[l],start[k]);
         swap(finish[l],finish[k]);
         swap(locStart[l],locStart[k]);
      }
      
      vector<int> Abuffer;
      vector<int> Bbuffer;
      
      int Atrains = 0;
      int Btrains = 0;
      
      FOR(k,0,start.size())
      {
         if(locStart[k] == 0)
         {
            if(Abuffer.size() > 0 && Abuffer[0] <= start[k])
            {
               Bbuffer.PB(finish[k] + T);
               Abuffer.erase(Abuffer.begin());
            }
            else
            {
               Bbuffer.PB(finish[k] + T);
               Atrains++;
            }  
         }
         else
         {
            if(Bbuffer.size() > 0 && Bbuffer[0] <= start[k])
            {
               Abuffer.PB(finish[k] + T);
               Bbuffer.erase(Bbuffer.begin());
            }
            else
            {
               Abuffer.PB(finish[k] + T);
               Btrains++;
            }  
         }
         SORT(Abuffer);
         SORT(Bbuffer);
      }
      
      fout << "Case #" << MM << ": " << Atrains << " " << Btrains << endl;
      
   }
   
   return 0; 
    
    
    
    
    
    
}

