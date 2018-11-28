#include <iostream>
#include <vector>
using namespace std;

struct celda {
   int x,y,alt;
   char basin;
};

bool magia_loca(vector<vector<celda> > &m,int x,int y,int h,int w)
{
   return !((x-1>=0 && m[x-1][y].alt < m[x][y].alt) || (x+1 < h && m[x+1][y].alt < m[x][y].alt) ||
          (y-1 >= 0 && m[x][y-1].alt < m[x][y].alt) || (y+1 < w && m[x][y+1].alt < m[x][y].alt));
}

celda next(vector<vector<celda> > &m,int x,int y,int h,int w) {
   int min=0; vector<celda> posi;
   if (x-1 >= 0 && m[x][y].alt > m[x-1][y].alt && m[x][y].alt - m[x-1][y].alt > min)
   {
      min = m[x][y].alt - m[x-1][y].alt;
      posi.clear();
      posi.push_back(m[x-1][y]);
      }

   else if (x-1 >= 0 && m[x][y].alt > m[x-1][y].alt && m[x][y].alt - m[x-1][y].alt == min)
      posi.push_back(m[x-1][y]);

   if (y-1>=0&& m[x][y].alt > m[x][y-1].alt && m[x][y].alt - m[x][y-1].alt > min)
      {
          min = m[x][y].alt - m[x][y-1].alt;
          posi.clear();
          posi.push_back(m[x][y-1]);}

   else if (y-1 >= 0 && m[x][y].alt > m[x][y-1].alt && m[x][y].alt - m[x][y-1].alt == min)
      posi.push_back(m[x][y-1]);

   if (y+1 < w       && m[x][y].alt > m[x][y+1].alt && m[x][y].alt - m[x][y+1].alt > min)
      {min = m[x][y].alt - m[x][y+1].alt; posi.clear(); posi.push_back(m[x][y+1]);}

   else if (y+1 < w  && m[x][y].alt > m[x][y+1].alt && m[x][y].alt - m[x][y+1].alt == min)
      posi.push_back(m[x][y+1]);

   if (x+1 < h       && m[x][y].alt > m[x+1][y].alt && m[x][y].alt - m[x+1][y].alt > min)
      {min = m[x][y].alt-m[x+1][y].alt;
      posi.clear();
      posi.push_back(m[x+1][y]);}

   else if (x+1 < h  && m[x][y].alt > m[x+1][y].alt && m[x][y].alt - m[x+1][y].alt == min)
      posi.push_back(m[x+1][y]);
   return posi[0];
}

void analyce(vector<vector<celda> > &m,  int h,  int w) {
   char bas = 'a', asig;
   celda tempo;
   vector<celda> cam;

   for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++) {
         tempo = m[i][j];
         cam.clear();
         if (tempo.basin != ' ') continue;
         while (tempo.basin == ' ' && !magia_loca(m, tempo.x, tempo.y, h, w)) {
            cam.push_back(tempo);
            tempo = next(m, tempo.x, tempo.y, h, w);
         }
         if (tempo.basin == ' ') {
            tempo.basin = bas;
            m[tempo.x][tempo.y].basin = bas;
            bas++;
         }
         asig = tempo.basin;
         for (int k = 0; k < cam.size(); k++)
         m[cam[k].x][cam[k].y].basin = asig;
      }
}

int main()
{
   int c,h,w,alt;
   vector<vector<celda> > m;
   celda tempo;
   std::cin>>c;
   for(int i=1;i<=c;i++) {
      std::cin>>h>>w;
      m.clear();
      m.resize(h);
      for(int z=0;z<h;z++)
         for (int k = 0; k < w; k++) {
            std::cin >> alt;
            tempo.x = z; tempo.y = k; tempo.basin = ' '; tempo.alt = alt;
            m[z].push_back(tempo);
         }

      analyce(m,h,w);
      std::cout << "Case #" << i << ":" << std::endl;

      for(int z=0;z<h;z++) {
         for (int k=0;k<w;k++) {
            std::cout<<m[z][k].basin <<" ";
         }
         std::cout<<std::endl;
      }
   }
	return 0;
}

