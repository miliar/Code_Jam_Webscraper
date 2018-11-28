#include <fstream>
#include <iostream>
   using namespace std;
   bool cell[500][500];
    int main()
   {
      ifstream in ("bacteria.in");
      ofstream out ("bacteria.out");
   
      int T;
      in >> T;
      for(int i = 0; i < T; i++)
      {
         for(int r = 1; r <= 100; r++)
            for(int c = 1; c <= 100; c++)
               cell[r][c] = false;
         int R;
         in >> R;
         for(int j = 0; j < R; j++)
         {
            int x1, y1, x2, y2;
            in >> x1 >> y1 >> x2 >> y2;
            for(int r = x1; r <= x2; r++)
               for(int c = y1; c <= y2; c++)
                  cell[r][c] = true;
         }
         bool flag = true;
         if(R == 0) flag = false;
         int time = 0;
         while(flag)
         {// 
            // for(int r = 1; r <= 10; r++)
            // {	
               // for(int c = 1; c <= 10; c++)
               // {
                  // cout << cell[r][c];
               // }
               // cout << endl;
            // }	
            // cout << endl;
            time++;
            flag = false;
            for(int r = 100; r >= 1; r--)
               for(int c = 100; c >= 1; c--)
               {
                  if(!cell[r][c] && cell[r - 1][c] && cell[r][c - 1])
                     cell[r][c] = true;
                  else if(cell[r][c] && !cell[r - 1][c] && !cell[r][c - 1])
                     cell[r][c] = false;
                  if(cell[r][c]) flag = true;
               }
         }
         out << "Case #" << (i + 1) << ": " << time << endl;
      }
      
   
      return 0;
   }
   
