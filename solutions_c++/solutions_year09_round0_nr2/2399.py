#include <iostream>
#include <vector>
using namespace std;

struct cell {
   int alt;
   char basin;
   int x, y;
};

bool isSink(vector<vector<cell> > &m, const int x, const int y, const int h, const int w) {
   return !((x-1 >= 0 && m[x-1][y].alt < m[x][y].alt) || (x+1 < h && m[x+1][y].alt < m[x][y].alt) ||
          (y-1 >= 0 && m[x][y-1].alt < m[x][y].alt) || (y+1 < w && m[x][y+1].alt < m[x][y].alt));
}

cell next(vector<vector<cell> > &m, const int x, const int y, const int h, const int w) {
   int min = 0;
   vector<cell> pos;
   
   if (x-1 >= 0      && m[x][y].alt > m[x-1][y].alt && m[x][y].alt - m[x-1][y].alt > min) 
      {min = m[x][y].alt - m[x-1][y].alt; pos.clear(); pos.push_back(m[x-1][y]);}
   
   else if (x-1 >= 0 && m[x][y].alt > m[x-1][y].alt && m[x][y].alt - m[x-1][y].alt == min) 
      pos.push_back(m[x-1][y]);
   
   if (y-1 >= 0      &&  m[x][y].alt > m[x][y-1].alt && m[x][y].alt - m[x][y-1].alt > min) 
      {min = m[x][y].alt - m[x][y-1].alt; pos.clear(); pos.push_back(m[x][y-1]);}
   
   else if (y-1 >= 0 && m[x][y].alt > m[x][y-1].alt && m[x][y].alt - m[x][y-1].alt == min) 
      pos.push_back(m[x][y-1]);
   
   if (y+1 < w       && m[x][y].alt > m[x][y+1].alt && m[x][y].alt - m[x][y+1].alt > min) 
      {min = m[x][y].alt - m[x][y+1].alt; pos.clear(); pos.push_back(m[x][y+1]);}
   
   else if (y+1 < w  && m[x][y].alt > m[x][y+1].alt && m[x][y].alt - m[x][y+1].alt == min) 
      pos.push_back(m[x][y+1]);
   
   if (x+1 < h       && m[x][y].alt > m[x+1][y].alt && m[x][y].alt - m[x+1][y].alt > min) 
      {min = m[x][y].alt - m[x+1][y].alt; pos.clear(); pos.push_back(m[x+1][y]);}
   
   else if (x+1 < h  && m[x][y].alt > m[x+1][y].alt && m[x][y].alt - m[x+1][y].alt == min) 
      pos.push_back(m[x+1][y]);
   
   return pos[0];
}

void analyze(vector<vector<cell> > &m, const int h, const int w) {
   char bas = 'a', asig;
   cell temp;
   vector<cell> cam;
   
   for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++) {
         temp = m[i][j];
         cam.clear();
         
         if (temp.basin != ' ') continue;
         
         while (temp.basin == ' ' && !isSink(m, temp.x, temp.y, h, w)) {
            cam.push_back(temp);
            temp = next(m, temp.x, temp.y, h, w);
         }
         
         if (temp.basin == ' ') {
            temp.basin = bas; 
            m[temp.x][temp.y].basin = bas;
            bas++;
         }
         asig = temp.basin;
         for (int k = 0; k < cam.size(); k++)
         m[cam[k].x][cam[k].y].basin = asig;
      }
   
   
}



int main(int argc, char *argv[]) {
	int c, h, w, alt;
   vector<vector<cell> > m;
   cell temp;
   
   cin >> c;
   
   for (int i = 1; i <= c; i++) {
      cin >> h >> w;
      m.clear();
      m.resize(h);
      
      for (int j = 0; j < h; j++)
         for (int k = 0; k < w; k++) {
            cin >> alt;
            temp.x = j; temp.y = k; temp.basin = ' '; temp.alt = alt;
            m[j].push_back(temp);
         }
      
      analyze(m, h, w);
      cout << "Case #" << i << ":" << endl;
      
      for (int j = 0; j < h; j++) {
         for (int k = 0; k < w; k++) {
            cout << m[j][k].basin << " ";
         }
         cout << endl;
      }
      
      
      
   }
   
   
   
   
   
	return 0;
}

