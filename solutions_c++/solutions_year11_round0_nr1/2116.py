#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

pair<char,int> v[100];

int iabs(int a)
{
  return a<0 ? -a : a;
}

int main()
{
  int T,N;
  cin >> T;
  for (int t=0; t<T; t++)
    {
      cin >> N;
      for (int i=0; i<N; i++)
        {
          cin >> v[i].first >> v[i].second;
        }

      int oi, bi, ot, bt;
      ot = bt = 1000000;
      oi = bi = N;
      for (int i=0; i<N; i++)
        if (v[i].first == 'O')
          {
            oi = i;
            ot = v[i].second-1;
            break;
          }
      for (int i=0; i<N; i++)
        if (v[i].first == 'B')
          {
            bi = i;
            bt = v[i].second-1;
            break;
          }

      int time=0;
      while (oi<N || bi<N)
        {
          if (ot == 0 && bt == 0)
            {
              time++;
              if (oi<bi)
                {
                  int pos = v[oi].second;
                  for (oi++; oi<N; oi++)
                    if (v[oi].first == 'O')
                      break;
                  if (oi<N)
                    ot = iabs(v[oi].second-pos);
                  else
                    ot = 1000000;
                }
              else
                {
                  int pos = v[bi].second;
                  for (bi++; bi<N; bi++)
                    if (v[bi].first == 'B')
                      break;
                  if (bi<N)
                    bt = iabs(v[bi].second-pos);
                  else
                    bt = 1000000;
                }
            }
          else if (ot == 0)
            {
              if (oi<bi)
                {
                  time++;
                  bt--;
                  int pos = v[oi].second;
                  for (oi++; oi<N; oi++)
                    if (v[oi].first == 'O')
                      break;
                  if (oi<N)
                    ot = iabs(v[oi].second-pos);
                  else
                    ot = 1000000;
                }
              else
                {
                  time += bt;
                  bt = 0;
                }
            }
          else if (bt == 0)
            {
              if (bi<oi)
                {
                  time++;
                  ot--;
                  int pos = v[bi].second;
                  for (bi++; bi<N; bi++)
                    if (v[bi].first == 'B')
                      break;
                  if (bi<N)
                    bt = iabs(v[bi].second-pos);
                  else
                    bt = 1000000;
                }
              else
                {
                  time+=ot;
                  ot=0;
                }
            }
          else
            {
              if (ot<bt)
                {
                  time += ot;
                  bt -= ot;
                  ot = 0;
                }
              else
                {
                  time += bt;
                  ot -= bt;
                  bt = 0;
                }
            }
        }
      cout << "Case #" << t+1 << ": " << time << endl;
    }

  return 0;
}
