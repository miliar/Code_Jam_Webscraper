#include <iostream>
#include <cstdio>
using namespace std;

bool has[1001][1001], trans[1001][1001];

int minY, minX, maxX, maxY;

void print()
{
     for (int i = 1; i <= 10; i++)
     {
         for (int j = 1; j <= 10; j++)
             cout << has[i][j];
             
         cout << endl;
     }
             
     cout << endl << endl;
}

int solve()
{
    int sec = 0;
    
    for (;;)
    {
        //print();
        
        bool bac = false;
        for (int i = minY - 2; i <= maxY + 2; i++)
        {
            for (int j = minX - 2; j <= maxX + 2; j++)
                if (has[i][j])
                {
                   bac = true;
                   break;              
                }
                
            if (bac)
               break;
        }
        
        if (!bac)
           break;
        
        for (int i = minY - 2; i <= maxY + 2; i++)
          for (int j = minX - 2; j <= maxX + 2; j++)
          {
              trans[i][j] = has[i][j];
              
              if (has[i][j])
              {
                 bool ok = false;
                 ok |= (i - 1 >= 1 && has[i - 1][j]);
                 ok |= (j - 1 >= 1 && has[i][j - 1]);
                 
                 if (!ok)
                    trans[i][j] = false;
                    
                 continue;
              }
              else
              {
                 bool ok = true;
                 ok &= (i - 1 >= 1 && has[i - 1][j]);
                 ok &= (j - 1 >= 1 && has[i][j - 1]);
                 
                 if (ok)
                    trans[i][j] = true;
              }              
          }
        
        for (int i = 1; i <= 1000; i++)
           for (int j = 1; j <= 1000; j++)
           {
              has[i][j] = trans[i][j];
              if (has[i][j])
              {
                 minY = min(minY, i);
                 minX = min(minX, j);
            
                 maxY = max(maxY, i);
                 maxX = max(maxX, j);
             }
           }
        
        sec++;
    }
    
    return sec;
}

int main()
{
    int T;
    cin >> T;
    
    for (int TT = 1; TT <= T; TT++)
    {
        int R;
        cin >> R;
        
        memset(has, 0, sizeof(has));
        
        minY = 1000000;
        minX = 1000000;
        maxX = 0;
        maxY = 0;
        
        for (int i = 0; i < R; i++)
        {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            
            minY = min(minY, 500 + y1);
            minX = min(minX, 500 + x1);
            
            maxY = max(maxY, 500 + y2);
            maxX = max(maxX, 500 + x2);
            
            for (int x = x1; x <= x2; x++)
                for (int y = y1; y <= y2; y++)
                    has[500 + y][500 + x] = true;
        }
        
        printf("Case #%d: %d\n", TT, solve());
    }
    
    return 0;
}
