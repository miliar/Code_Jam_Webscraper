#include <iostream>
//#include <string>
#include <vector>
#include <list>
//#include <algorithm>
#include <cmath>
using namespace std;
//#define M_PI       3.14159265358979323846
//typedef unsigned long long tull;
//const int MAX = 100000;

int main() 
{
  freopen("C-small-attempt1.in", "rt", stdin);
  freopen("C-small-attempt1.out", "wt", stdout);
  //freopen("C-small.in", "rt", stdin);
  //freopen("C-small.out", "wt", stdout);
  int T;

  cin >> T;
  int ind[5000];
  int l[5000];
  bool fl[5000];
  int n, K, d, siz;
  int diff, curin;

  for (int inn=0; inn<T; ++inn)
  {
    cin >> K;

    for (int i=0; i<K; ++i)
    {
      l[i] = i; fl[i] = true;
    }

    siz = K; 

    //list<int>::iterator it2, it = l.begin();
    ind[0] = 0; curin = 0;
    
    for (int i=0; i<K; ++i)
    {
      diff = i;
      diff = diff % siz;

      for (int j=0; j<diff; ++j)
      {

 
        do
        {
          ++curin;
          if (curin == K) curin = 0;
        }while (!fl[curin]);
        //if (it == l.end())
        //  it = l.begin();
      }

      ind[l[curin]] = i;
      fl[l[curin]] = false; 
      ++curin;
      if (curin == K) curin = 0;
      --siz;
      if (siz)
      while (!fl[curin])
      {
        ++curin;
        if (curin == K) curin = 0;
      }

    }

    cout << "Case #" << inn+1 << ": ";
    cin >> n;

    for (int i=0; i<n; ++i)
    {
      cin >> d;
      cout << ind[d-1]+1 << " ";
    }
    cout << endl;

  }
  return 0;
}
