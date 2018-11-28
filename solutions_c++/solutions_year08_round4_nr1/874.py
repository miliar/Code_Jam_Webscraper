#include <iostream>
//#include <string>
//#include <vector>
//#include <list>
//#include <algorithm>
#include <cmath>
using namespace std;
//#define M_PI       3.14159265358979323846
//typedef unsigned long long tull;
//const int MAX = 100000;

typedef long tull;

const long LOTS = 99999;


int main() 
{
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);

  int N;
  cin >> N;

  tull M, V;
  tull ins, i, val, w,n1, n2;
  tull G[10001], C[10001];
  //tull val[10001];
  tull v0[10001],v1[10001];

  for (int inn=0; inn<N; ++inn)
  {
    cin >> M >> V;
    ins = (M-1)/2;

    for(i=1; i<=ins; ++i)
      cin >> G[i] >> C[i];

    for(i=ins+1; i<=M; ++i)
    {
      cin >> val;
      if (val)
      {
        v1[i] = 0;
        v0[i] = LOTS;
      }
      else
      {
        v1[i] = LOTS;
        v0[i] = 0;
      }
    }
    
    for (i = ins; i>0; --i)
    {
      n1 = 2*i; n2 = n1+1;
      if (G[i] == 1)
      { //and

        // 1
        if (v1[n1]+v1[n2]>=LOTS)
        { v1[i]=LOTS;}
        else
        { v1[i] = v1[n1]+v1[n2];}

        // 0
        v0[i] = LOTS;
        if (v0[n1]+v0[n2]<v0[i])
        {v0[i] = v0[n1]+v0[n2];}

        if (v1[n1]+v0[n2]<v0[i])
        {v0[i] = v1[n1]+v0[n2];}

        if (v0[n1]+v1[n2]<v0[i])
        {v0[i] = v0[n1]+v1[n2];}
        
        if (C[i] == 1)
        {
          // 1 
  //        v1[i] = LOTS;

          if ((v1[n1]+v1[n2]+1)<v1[i])
            v1[i] = v1[n1]+v1[n2]+1;

          if ((v0[n1]+v1[n2]+1)<v1[i])
            v1[i] = v0[n1]+v1[n2]+1;

          if ((v1[n1]+v0[n2]+1)<v1[i])
            v1[i] = v1[n1]+v0[n2]+1;
        }

      }
      else
      {
        //0
        if ((v0[n1]+v0[n2]+1)>=LOTS)
        {
          v0[i]=LOTS;
        }
        else
        {
          v0[i] = v0[n1]+v0[n2];
        }

        // 1 
        v1[i] = LOTS;

        if (v1[n1]+v1[n2]<v1[i])
          v1[i] = v1[n1]+v1[n2];

        if (v0[n1]+v1[n2]<v1[i])
          v1[i] = v0[n1]+v1[n2];

        if (v1[n1]+v0[n2]<v1[i])
          v1[i] = v1[n1]+v0[n2];

        if (C[i])
        {
          // 0
//          v0[i] = LOTS;
          if ((v0[n1]+v0[n2]+1)<v0[i])
          {v0[i] = v0[n1]+v0[n2]+1;}

          if ((v1[n1]+v0[n2]+1)<v0[i])
          { v0[i] = v1[n1]+v0[n2]+1;}

          if ((v0[n1]+v1[n2]+1)<v0[i])
          {v0[i] = v0[n1]+v1[n2]+1;}
        }
      }
    }

    if (V == 1)
    {
      if (v1[1] >= LOTS)
      {cout << "Case #" << inn+1 << ": IMPOSSIBLE" << endl;}
      else
      {cout << "Case #" << inn+1 << ": " << v1[1] << endl;}
    }
    else
    {
      if (v0[1] >= LOTS)
        cout << "Case #" << inn+1 << ": IMPOSSIBLE" << endl;
      else
        cout << "Case #" << inn+1 << ": " << v0[1] << endl;
    }
  }

  return 0;
}
