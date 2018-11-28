#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <time.h>
#include <stdlib.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define vi vector <int>
#define rep(i,n) for(int i = 0; i < n; i++)
#define read(a) rep(i, a.size()) fin >> a[i];
#define write(a) rep(i, a.size()) fout << a[i] << ' '; fout << endl;
#define fi first
#define se second
#define ll long long
const int inf = 2000000000, mod = 1000000007;
const double eps = 0.000001;

int main()
{
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    int t = 1;
    fin >> t;
    for (int count = 1; count <= t; count++)
    {
        int n;
        fin >> n;
        deque <int> b, o;
        vector <char> a;
        for (int i = 0; i < n; i++)
        {
            char c;
            int x;
            fin >> c >> x;
            if (c == 'O')
               o.pb(x);
            else
                b.pb(x);
            a.pb(c);
        }
        int cur = 0, res = 0, curo = 1, curb = 1, tmp;
        while (cur != n)
        {
              if (a[cur] == 'O')
              { 
                 if (o.front() - curo == 0)
                 {
                    cur++;
                    o.pop_front();
                 }
                 else
                 {
                     if (o.front() - curo < 0)
                        curo--;
                     else 
                         curo++;
                 }
                 
                 if (b.front() - curb < 0)
                    curb--;
                 else if (b.front() - curb > 0)
                     curb++;
              }
              else if (a[cur] == 'B')
              {
                  if (b.front() - curb == 0)
                  {
                     b.pop_front();
                     cur++;
                  }
                  else
                  {
                      if (b.front() - curb < 0)
                         curb--;
                      else if (b.front() - curb > 0)
                          curb++;
                  }
                  
                  if (o.front() - curo < 0)
                     curo--;
                  else  if (o.front() - curo > 0)
                      curo++;   
              }
              res++;
        }
        fout << "Case #" << count << ": " << res << endl;
    }
    return 0;
}








