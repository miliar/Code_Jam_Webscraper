#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct diagram
{
  int dep, arr; // depart and arrived time
  int a2b;      // 0 ... A->B,  1 ... B->A
};

bool cmpDia(const diagram& a, const diagram& b) {
  if( a.dep < b.dep ) return true;
  if( a.dep > b.dep ) return false;
  if( a.arr < b.arr ) return true;
  if( a.arr > b.arr ) return false;
  return a.a2b < b.a2b;
}

int main(void)
{
  int N;
  cin >> N;
  vector<diagram> dia;
  
  for( int cas = 0 ; cas < N ; ) {
    cout << "Case #" << (++cas) << ": ";
    int turn, na, nb;
    cin >> turn >> na >> nb;

    dia.clear();
    for( int i = 0 ; i < na ; ++i ) {
      int a, b;
      diagram d;
      string str;
      cin >> str;
      d.dep = strtol(str.c_str(),NULL, 10) * 60 + strtol(str.c_str() + 3, NULL, 10);
      cin >> str;
      d.arr = strtol(str.c_str(), NULL, 10) * 60 + strtol(str.c_str() + 3, NULL, 10);
      d.a2b = 0;
      dia.push_back(d);
    }
    for( int i = 0 ; i < nb ; ++i ) {
      int a, b;
      diagram d;
      string str;
      cin >> str;
      d.dep = strtol(str.c_str(), NULL, 10) * 60 + strtol(str.c_str() + 3, NULL, 10);
      cin >> str;
      d.arr = strtol(str.c_str(), NULL, 10) * 60 + strtol(str.c_str() + 3, NULL, 10);
      d.a2b = 1;
      dia.push_back(d);
    }

    sort(dia.begin(), dia.end(), cmpDia);

    // Here, NA and NB mean neccessary trains in A(B) station
    na = nb = 0;
    vector<diagram>::iterator p;
    while( dia.size() > 0 ) {
      if( dia[0].a2b ) { ++nb; } else { ++na; };
      int station = 2, tim = -100;
      for( p = dia.begin() ; p != dia.end() ; ) {
        if( p->a2b == station || p->dep < tim ) {
          ++p;
          continue;
        }

        station = p->a2b;
        tim = p->arr + turn;
        p = dia.erase(p);
      }
    }
    cout << na << " " << nb << "\n";
  }
  return 0;
}
