#include <algorithm> 
#include <iostream>
#include <string>
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;

#include<fstream>
ifstream fin("input.txt");
ofstream fout("output.txt");
 

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;  

void run(int casenr) {
	int N; int S,p;
    fin >> N;
    fin >> S;
    fin >> p;

     int output=0, num, num_by_3, rem;

     FORE(i,1,N)
     {
       fin >> num;
       num_by_3  = num/3;
       rem = num%3;


       if(num_by_3 >= p)
       {
         output++;
         continue;
       }

       if(num == 0)
        continue;


       if(rem == 0)
       {
          if(S >= 1 && ((num_by_3+1 <= 10) && (num_by_3+1)>=p))
          {
            S--;
            output++;
           }
          continue;
        }

        if(((num_by_3+1) <= 10) &&((num_by_3+1)>=p))
         {
             output++;
             continue;
         }

         if(rem == 2)
         {
            if(S >= 1 && (((num_by_3+2) <= 10) &&((num_by_3+2)>=p)))
            {
             S--;
             output++;
             }
           continue;
         }
   }
	fout << "Case #" << casenr <<": " << output <<endl;
}

int main() {
    if(NULL == fin)
    {
      cout<<"NO INPUT FILE"<<endl;
      return 0;
    }
	int n;  fin >> n;

   FORE(i,1,n) run(i);

   system("PAUSE");
	return 0;
}

