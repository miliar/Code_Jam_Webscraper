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

int P[] = { 2,3,5,7 };

string S;

LL rek(int k, LL wyn, char znak, LL akt)
{
  if( k == S.size() )
  {
   // cout << s << endl;
 /*   string ss = s;
    vector <char> C;
    for(int i=0;i<ss.size();i++)
    {
      if(ss[i] == '+' || ss[i] == '-') 
      {
        C.push_back(ss[i]);
        ss[i] = ' ';
      }
    }
    istringstream is(ss);
    int wyn = 0;
    is >> wyn;

    int tmp;
    int a = 0;
    while(is >> tmp)
    {
       if( C[a] == '+')
       {
         wyn+= tmp;
       }
       else wyn-= tmp;
       a++;
    }
    
    */
    if( znak == '+')
    {
       wyn+=akt;
    }
    else wyn-=akt;

    if( wyn %2 == 0 || wyn %3 == 0 || wyn %5 == 0 || wyn %7 == 0 ) return 1;
    else return 0;

  }

  LL cnt = rek(k+1, wyn, znak, akt * 10LL + (LL) (S[k]-'0') );
  if(znak == '+')
  {
    cnt += rek(k+1, wyn+akt, '+', S[k]-'0');
    cnt += rek(k+1, wyn+akt, '-', S[k]-'0');

  }
  else
  {
    cnt += rek(k+1, wyn-akt, '+', S[k]-'0');
    cnt += rek(k+1, wyn-akt, '-', S[k]-'0');
  }


  return cnt;
}

int main()
{
  int tst;
  cin >> tst;
  int num = 0;
  while(++num <= tst)
  {

    cin >> S;                  // p - liter, k - klawiszy
    string s;
    s+=S[0];
    int cnt = rek(1, 0LL, '+', s[0]-'0');                 // wynik, poprzedni znak, biezace obliczenia
    cout << "Case #" << num <<": " << cnt <<   endl;

  }

  return 0;
}
