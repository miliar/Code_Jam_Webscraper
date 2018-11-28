#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <utility>
#include <queue>
using namespace std;
 
#define all(c)         (c).begin(),(c).end()
#define fori(c,i)     for(typeof(c).begin() i = (c).begin(); i != (c).end(); i++)
 
typedef long long     LL;
typedef vector<int>   vi; 
typedef vector< vi >   vvi; 

struct poc
{
  bool kon;
  int czas;
  bool st;  // false - A, true - B
  poc(int _czas, bool _kon, bool _st):czas(_czas),kon(_kon),st(_st) {;}
};

bool operator<(const poc & A, const poc & B)
{
   if( A.czas == B.czas )
   {
      return A.kon > B.kon;
   }
   return A.czas < B.czas;
}


int main()
{
  char arr[30], dept[50];
  int tst;
  cin >> tst;
  int num = 0;
  while(++num <= tst)
  {
    int A= 0, B = 0;
    int t;
    scanf("%d", &t);
    int na,nb;
    scanf("%d%d", &na,&nb);
    vector <poc> T;
    for(int i=0;i<na;i++)
    {
        scanf("%s %s", arr, dept);
        int ar, de;
        int h,s;
        sscanf(arr ,"%d:%d", &h,&s);
        ar = h*60 + s;
        sscanf(dept ,"%d:%d", &h,&s);
        de = h*60 + s + t;
    //    cout << ar << " " << de << endl;
       T.push_back( poc(ar, false,false));
       T.push_back( poc(de, true,true));
    }
    
    
    for(int i=0;i<nb;i++)
    {
        scanf("%s %s", arr, dept);
        int ar, de;
        int h,s;
        sscanf(arr ,"%d:%d", &h,&s);
        ar = h*60 + s;
        sscanf(dept ,"%d:%d", &h,&s);
        de = h*60 + s + t;
        
        T.push_back( poc(ar, false,true));
       T.push_back( poc(de, true,false));

    }
    int aA = 0,aB = 0; // aktualnych a i b
    sort( T.begin(), T.end()  );
    for(int i=0;i<T.size();i++)
    {
       if( T[i].kon )
       {
         if( T[i].st )
         {
           ++aB;
         }
         else ++aA;
         continue;  // koncowy
       }
       // poczatkowe stacje
       if( !T[i].st ) // stacja A
       {
         if(aA) aA--;
         else A++;

       }
       else // stacja B
       {
         if(aB) aB--;
         else B++;
       }
    }

    cout << "Case #" << num <<": " << A << " " << B << endl;
  }

  return 0;
}
