#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const int MAXS = 2000;

struct state {
 int flag, wh, minu;
 state() { }
 state(int flag, int wh, int minu) : flag(flag), wh(wh), minu(minu) { }
 bool operator < (const state &t) const
 {
  if (minu != t.minu) return minu < t.minu;
  if (flag != t.flag) return flag < t.flag;
  return wh < t.wh;
 }
};

int T, NA, NB;

int get_time(string s)
{
 int a = s[0] - '0', b = s[1] - '0', c = s[3] - '0', d = s[4] - '0';
 return (a * 10 + b) * 60 + (c * 10 + d);
}

state inp[MAXS];

int main()
{
 ifstream fin("trains.in");
 ofstream fout("trains.out");
 
 int N; fin >> N;
 
 for (int u = 0; u < N; u++)
 {
  fin >> T;
  fin >> NA >> NB;
  int tot = 0;
  for (int i = 0; i < NA; i++)
  {
   string st, en; fin >> st >> en;
   int t1 = get_time(st), t2 = get_time(en); 
   inp[tot++] = state(1, 0, t1);
   inp[tot++] = state(0, 1, t2 + T);
  }
  for (int i = 0; i < NB; i++)
  {
   string st, en; fin >> st >> en;
   int t1 = get_time(st), t2 = get_time(en); 
   inp[tot++] = state(1, 1, t1);
   inp[tot++] = state(0, 0, t2 + T);
  }
  
  sort(inp, inp + tot);
  
  int ans = 1000000, minl = -1, minr = -1;
  
  for (int fa = 0; fa <= 100; fa++) //!!!!!!!!!!!!!!!!!!!!!!!!!
   for (int fb = 0; fb <= 100; fb++) //!!!!!!!!!!!!!!!!!!!!!!!!
   {
    int left = fa, right = fb; bool ok = true;
    for (int i = 0; i < tot; i++)
    {
     if (inp[i].flag == 0)
     {
      if (inp[i].wh == 0) left++; else right++;
     }
     else
     if (inp[i].flag == 1)
     {
      if (inp[i].wh == 0)
      {
       if (left < 1) { ok = false; break; } else left--;
      }
      else
      if (inp[i].wh == 1)
      {
       if (right < 1) { ok = false; break; } else right--;
      }
     }
    }
    
    if (ok)
    {
     if (fa + fb < ans) { ans = fa + fb; minl = fa; minr = fb; }
     break;
    }
    
   }
   
  fout << "Case #" << u + 1 << ": " << minl << " " << minr << endl;
 }
 
 fin.close();
 fout.close();

 return 0;
}
