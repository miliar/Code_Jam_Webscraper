#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
using namespace std;

int main()
{
    
    ifstream in("happy.txt");
    ofstream out("sad.txt");
    
      int cases;
      in >> cases;
      
      for (int c = 0; c < cases; c++)
      {
          int thea = -1, theb = -1, theda = -1, thedb = -1;
          
          int m, n, area;
          in >> m >> n >> area;
          //cout << area << endl;
          
          for (int a = 1; a <= m; a++)
          for (int b = 1; b <= n; b++)
          {   
              int dif = a*b - area;
              if (dif < 0) continue;
              if (dif == 0)
              {
                 thea = a;
                 theb = b;
                 theda = 0;
                 thedb = 0;
                 goto theend;
              }
              if (dif >= a*b) continue;
              for (int da = max(1,(dif / b)); da < a; da++)
              {
                  if (da == 0) break;
                  if (dif % da != 0) continue;
                  if (dif < da) break;
                  int db = dif / da;
                  if (db >= b) continue;
                  thea = a;
                 theb = b;
                 theda = da;
                 thedb = db;
                 goto theend;
              }
          }
                  
                      
          
          theend:
                 if (thea < 0)
                 {
                       out << "Case #" << (c+1) << ": IMPOSSIBLE" << endl;
                 }
                 else
                 {
                     int x1 = thea;
                     int y1 = theb;
                     int x2 = 0;
                     int y2 = theb - thedb;
                     int x3 = thea - theda;
                     int y3 = 0;
                     
                     int tri1 = (thea - theda) * (theb - thedb);
                     int tri2 = thea * thedb;
                     int tri3 = theb * theda;
                     int ar = 2*thea * theb - tri1 - tri2 - tri3;
                     //cout << thea << " " << theb << " " << theda << " " << thedb << endl;
                     if (area != ar) cout << "Bad area " << ar << " " << area << endl;
                     
                     out << "Case #" << (c+1) << ": " << x1 << " " << y1 << " " << x2 << " " 
                     << y2 <<  " " << x3 << " " << y3 << endl;
                 
                 }
          }
          system("PAUSE");
          return 0;
          
}
