#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <string>
#include <algorithm>


using namespace std;

struct revent
{
  int i,j,k;
  double time;

  bool operator<(const revent &a) const
  {
    return time < a.time;
  };

};



int main()
{
  int n1,i1;
  cin >> n1;
  for (i1=1;i1<=n1;++i1)
  {
    int ceil[101][101], floor[101][101];
    int i,j,k,l,m,n;
    double h;

    
    cin >> h >> n >> m;
    for (i=0;i<n;++i)
      for (j=0;j<m;++j)
        cin >> ceil[i][j];

    for (i=0;i<n;++i)
      for (j=0;j<m;++j)
        cin >> floor[i][j];
  

    bool reach[101][101][4];
    int d[4][2]={{-1,0},{0,-1},{1,0},{0,1}};

    vector<revent> event;


    for (i=0;i<n;++i)
      for (j=0;j<m;++j)
        for (k=0;k<4;++k)
        {
          reach[i][j][k] = false;
          if (i+d[k][0]>=0 && i+d[k][0]<n && j+d[k][1]>=0 && j+d[k][1]<m)
          {
            int ti=i+d[k][0];
            int tj=j+d[k][1];

            if (floor[i][j]+50 <= ceil[ti][tj] &&
                floor[ti][tj]+50 <= ceil[ti][tj] &&
                floor[ti][tj]+50 <= ceil[i][j])
            {
              if (h+50<=ceil[ti][tj])
                reach[i][j][k] = true;
              else
              {
                revent e;
                e.i = i;
                e.j = j;
                e.k = k;
                e.time = (h+50.0-ceil[ti][tj])/10; 
                event.push_back(e);
              };
            };               
          };
        };

    sort(event.begin(),event.end());

    double flag[101][101];
    int mark[101][101];
    for (i=0;i<n;++i)
      for (j=0;j<m;++j)
      {
        flag[i][j] = 1000000000;
        mark[i][j] = 1;
      };
    
    int queue[30000][2];
    int closed,open;

    closed = 0;
    open = 1;
    queue[0][0] = 0;
    queue[0][1] = 0;

    flag[0][0] = 0;
    mark[0][0] = 0;

    while (closed != open)
    {
      i = queue[closed][0];
      j = queue[closed][1];
      closed ++;
      for (k=0;k<4;++k)
        if (reach[i][j][k])
        {
          int ti=i+d[k][0];
          int tj=j+d[k][1];
          if (flag[ti][tj] > 0)
          {
            flag[ti][tj] = 0;
            queue[open][0] = ti;
            queue[open][1] = tj;
            mark[ti][tj] = 0;
            open ++;
          };
        };
    };


    double min = flag[n-1][m-1];
    for (l=0;l<event.size();++l)
    {
      revent e = event[l];
      reach[e.i][e.j][e.k] = true;

      double next=0;
      if (l==event.size()-1)
        next=100000000;
      else
        next = event[l+1].time;


      if (true)
      {
        if (flag[e.i][e.j]<=e.time)
        {
          mark[e.i][e.j] = 1;
          flag[e.i][e.j] = e.time;
        };


/*        
        if (flag[e.i][e.j]<=e.time)
        {
          queue[open][0] = e.i;
          queue[open][1] = e.j;
          flag[e.i][e.j] = e.time;
          mark[e.i][e.j] = open;
          open += 1;
        };
*/
  
        while (true)
        {

          int l1,m1;
          double dmin = 1e10;

          for (l1 =0; l1<n; ++l1)
            for (m1 = 0; m1<m; ++m1)
              if (flag[l1][m1] < dmin && mark[l1][m1] != 0)
              {
                dmin = flag[l1][m1];
                i = l1;
                j = m1;
              };


          if (dmin == 1e10)
            break;

//          printf("check %d %d %lf %lf\n", i,j, flag[i][j], next);

//          i = queue[closed][0];
//          j = queue[closed][1];
          double delta;
          if (h-flag[i][j]*10-floor[i][j]>=20)
            delta=1;
          else 
            delta=10;
  
          if (flag[i][j]>=next)
            break;

          mark[i][j] = 0;
          

          //closed ++;
          for (k=0;k<4;++k)
            if (reach[i][j][k])
            {
              int ti=i+d[k][0];
              int tj=j+d[k][1];
              if (flag[ti][tj] > flag[i][j]+delta)
              {
                flag[ti][tj] = flag[i][j]+delta;
//                queue[open][0] = ti;
//                queue[open][1] = tj;
                open ++;
              };
            };
        };
      };

      if (flag[n-1][m-1]<min)
        min = flag[n-1][m-1];
    };

    printf("Case #%d: %.6f\n", i1, min);
  };

};
