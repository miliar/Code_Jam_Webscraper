#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

void f (vector<int>& e,int t,int S,bool flag,bool flag2)
{
  if (flag2)
  {
    for (int i = 0; i < e.size(); i++) e[i] = 0;
  }
  if (flag)  t -= 2;
  int d = 1;
  if (t%3 == 0)
  {
    e[0] = t/3;
    e[1] = t/3;
    e[2] = t/3;
  }
  else
  {
    e[0] = t;
    for (int i = 0; i < e.size()-1; i++)
    {
      for (int j = i+1; j < e.size(); j++)
      {
        while (abs(e[i]-e[j]) > d)
        {
          if (e[i] > e[j]) 
          {
            --e[i];
            ++e[j];
          }
          else
          {
            ++e[i];
            --e[j];
          }
        }
      }
    }
  }
  sort (e.begin(),e.end());
  while ( (e[e.size()-1] - e[0]) > d)
  {
    --e[e.size()-1];
    ++e[0];
  }
  
  if (flag)
  {
    sort(e.begin(),e.end());
    if (e[e.size()-1] - e[0] == 1)
    {
      ++e[e.size()-1];
      ++e[1];
    }
    else if (e[e.size()-1] - e[0] == 0)
    {
      e[e.size()-1] += 2;
    }
  }
}

bool comp (vector<int> a,vector<int> b) { return a[a.size()-1] > b[b.size()-1]; }

int main ()
{
  /*int j = 0; cin >> j;
  int S2 = 1;
  vector<int> y(3);
  f(y,j,S2,false);
   
  for (int i = 0; i < y.size(); i++)
  {
    cout << y[i] << " ";
  }
  cout << endl;
 
  return 0;*/
  int QWERTY = 0;
  cin >> QWERTY;
  for (int qwer = 0; qwer < QWERTY; qwer++)
  {
  int g = 3;
  int N = 0,
      S = 0,
      p = 0;

  cin >> N >> S >> p;

  //cout << N << " " << S << " " << p << endl;

  vector<int> t(N);
  for (int i = 0; i < t.size(); i++)
  {
    cin >> t[i];
  }
  /*for (int i = 0; i < t.size(); i++)
  {
    cout << t[i] << " ";
  }
  cout << endl;*/
  vector<vector<int> > all;
  vector<vector<int> > all2;
  for (int i = 0; i < t.size(); i++)
  {
    bool flag = false;
    vector<int> e(g);
    vector<int> e2(g);
    if (t[i]%g == 0)
    {
      for (int j = 0; j < e.size(); j++)
      {
        e2[j] = t[i]/g;
      }
      if (t[i] > 2)
      f (e,t[i],S,true,false);
      else
      f (e,t[i],S,false,false);
      flag = true;
    }
    else
    {
      if (S == 0)
      {
        f (e,t[i],S,false,false);
        f (e2,t[i],S,false,false);
        flag = true;
      }
      else {
        if (t[i] > 2)
        { 
        f (e,t[i],S,true,false);
        f (e2,t[i],S,false,false);
        flag = true;
        }
        else
        {
        f (e,t[i],S,false,false);
        f (e2,t[i],S,false,false);
        flag = true;
        }
      } 
    }
    all.push_back(e);
    if (flag) all2.push_back(e2);
  }

  for (int i = 0; i < all.size(); i++)
  {
    sort(all[i].begin(),all[i].end());
    sort(all2[i].begin(),all2[i].end());
  }

  /*sort (all.begin(),all.end(),comp);
  sort (all2.begin(),all2.end());*/
 
  /*for (int i = 0; i < all.size(); i++)
  {
    for (int j = 0; j < all[i].size(); j++)
    {
      cout << all[i][j] << " ";
    }
    cout << endl;
  }

  cout << endl;
  

  for (int i = 0; i < all.size(); i++)
  {
    for (int j = 0; j < all[i].size(); j++)
    {
      cout << all2[i][j] << " ";
    }
    cout << endl;
  }
 
  cout << endl;*/ 

  int count = 0;
  vector<int> bla;
  for (int i  = 0; i < all2.size(); i++)
  {
    if (all2[i][all2[i].size()-1] >= p)
    {
      bla.push_back(i);
      count++;
    }
    else
    {
      bla.push_back(-1);
    }
  }
  
  for (int i = 0; i < all.size(); i++)
  {
    bool flag = false;
    for (int j = 0; j < bla.size(); j++)
    {
      if (i != bla[j])
      {
        flag = true;
      }
      else
      {
        flag = false;
        break;
      } 
    }
    if (flag == true)
    if (all[i][all[i].size()-1] >= p)
    {
        if (S)
        {
          count++;
          --S;
        }
    }
  }
  

  cout << "Case #" << qwer+1 << ": " << count << endl;
  }
  return 0;
}
