#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    ifstream fin("D:\C-small-attempt0.in");
    ofstream fout("D:\C-small-attempt0.out");
        
    int T, R;
    fin >> T;
    
    bool bacteria[128][128];
    bool newb[128][128];
        
    for (int i = 1 ; i <= T ; i++)
    {
        fin>> R;   
        memset(bacteria, 0, sizeof(bacteria));        
        
        int X1, X2, Y1, Y2;
        for (int j = 0 ; j < R ; j++)
        {
            fin >> X1 >> Y1 >> X2 >> Y2;
            for (int x = X1 ; x <= X2 ; x++)
                for (int y = Y1 ; y <= Y2 ; y++)
                    bacteria[x][y] = true;            
        }
        
        int answer = 0;
        bool exist = true;
        while (exist)
        {
              memset(newb, 0, sizeof(newb));
              answer++;
              for (int x = 1 ; x < 128 ; x++)
                  for (int y = 1 ; y < 128 ; y++)
                  {
                      if (bacteria[x][y])
                      {
                           if (bacteria[x-1][y] || bacteria[x][y-1]) 
                              newb[x][y] = true;
                      }
                      else
                      {
                          if (bacteria[x-1][y] && bacteria[x][y-1])
                             newb[x][y] = true;
                      }                
                  }
                                
              memcpy(bacteria, newb, sizeof(newb));
              
              exist = false;
              for (int x = 1 ; x < 128 ; x++)
                  for (int y = 1 ; y < 128 ; y++)
                      if (bacteria[x][y]) {exist = true; break;}
        }
                
        
        fout << "Case #" << i << ": " << answer << endl;
        
    }
}
