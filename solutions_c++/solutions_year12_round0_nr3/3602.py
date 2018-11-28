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


int POWR[10] = {10, 100, 1000, 10000, 100000, 1000000, 10000000};

int numDigits(int num)
{
 int digits;
 if (num == 0)
  return 0;
 for(int i=0;i<7;i++)
  {
      if(num / POWR[i] == 0)
      {
        digits = i+1;
        break;
      }
    }
    return digits;
 }

void run(int casenr) {
    int A, B;

    fin >> A;
    fin >> B;

    int digits = 0;

    int cnt=0, num, num_by, mod, i, digCnt;

    digits = numDigits(A);

    for(i = A; i < B; i++)
    {
      for(int j=1;j<digits;j++)
      {
         num_by  = i / POWR[j-1];
         mod = i % POWR[j-1];

         digCnt =  numDigits(mod);
         if(digCnt == 0 || (digCnt != j))
           continue;


        num = (mod * POWR[digits-j-1]) + num_by;

       // printf("i=%d,num=%d,num_by=%d,mod=%d,powrJ=%d,j=%d\n",i,num,num_by,mod,POWR[j-1],j);

        if(num > i && num <=B)
        {
        // fout << "i ="<<i<<" num =" <<num<<endl;
         cnt++;
         }
        }
    }

	fout << "Case #" << casenr <<": " << cnt <<endl;
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

