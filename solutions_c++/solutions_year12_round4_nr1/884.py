#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

int main()
{
  int i1,n1;
  cin >> n1;
  int **f;
  f = new int*[10002];
  for (int i=0;i<10002;++i)
    f[i] = new int[10002];

  
  for (i1=1;i1<=n1;++i1)
  {
    int i,j,k,l,m,n;
    cin >> n;
    vector<int> dist,length;
    dist.push_back(0);
    length.push_back(0);
    for (i=0;i<n;++i)
    {
      cin >> j >> k;
      dist.push_back(j);
      length.push_back(k);
    };

    cin >> l;
  
    n += 1;
    
    dist.push_back(l);
    length.push_back(0);

    
    for (i=0;i<=n;++i)
      for (j=0;j<=n;++j)
        f[i][j] = 0;
    
    f[0][1] = 1;
    

    struct pair
    {
      int x,y;
    };

    vector<pair> queue;
    pair temp;
    temp.x = 0;
    temp.y = 1;
    queue.push_back(temp);
    
    printf("Case #%d: ", i1);
    int closed = 0, open = 1;
    
    bool found = false;

    while (closed != open)
    {
      temp = queue[closed];
      int remain = dist[temp.y]-dist[temp.x];
      int current;
      if (remain > length[temp.y])
      {
        current = dist[temp.y]-length[temp.y];
        remain = length[temp.y];
      }
      else
        current = dist[temp.x];
      closed += 1;   

      for (i=temp.y+1;i<=n;++i)  
        if (dist[temp.y]+remain >= dist[i])
        {
          if (f[temp.y][i] == 0)
          {
           if (i==n)
            {
              printf("YES\n");
              found = true;
              break;
            };
            f[temp.y][i] = 1;
            open += 1;
            pair temp2;
            temp2.x = temp.y;
            temp2.y = i;
            queue.push_back(temp2);
          };
        };
      if (found)
        break;
    };
    if (not found)
      printf("NO\n");
  };


};

