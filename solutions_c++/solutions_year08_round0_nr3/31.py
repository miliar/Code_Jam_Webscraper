#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

const double EPS = 1e-10;
const double PI = 3.14159265358979323846264338328;

#define PB push_back
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define INF INT_MAX
#define MSG(a) cout << #a << " = " << a << endl;
#define SORT(a) sort(a.begin(),a.end())


int main()
{
   ofstream fout;
   fout.open("output.txt");
   ifstream fin("C-large.in");
    
   int N;
   fin >> N;
   
   FOR(k,1,N+1)
   {
      long double f,R,t,r,g;
      fin >> f >> R >> t >> r >> g;
 //     fout << f << " " << R << " " << t << " " << r << " " << g << endl;
      
      if(2.0*f >= g)
      {
         fout << "Case #" << k << ": 1.000000\n";
         continue;
      }
      
      long double ans = 0;
      
      long double xleft = r;
      while(xleft < R-t)
      {
         long double ytop = r+g;
         while(1)
         {
            if((xleft+g)*(xleft+g) + ytop*ytop >= (R-t)*(R-t))
            {
               //calculate one unfinished square

               long double ybot = ytop - g;
               long double upperleftx = xleft + f;
               long double upperlefty = ytop - f;
               long double lowerleftx = xleft + f;
               long double lowerlefty = ybot + f;
               long double lowerrightx = xleft + g - f;
               long double lowerrighty = ybot + f;
               if(lowerleftx >= lowerrightx)
                  break;
               if(lowerlefty >= upperlefty)
                  break;
               
               long double RAD = R - t - f;
               if(lowerleftx*lowerleftx + lowerlefty*lowerlefty >= RAD*RAD)
                  break;
               
               int upperLeftInside = 1;
               int lowerRightInside = 1;
               if(upperleftx*upperleftx + upperlefty*upperlefty >= RAD*RAD)
                  upperLeftInside = 0;
               if(lowerrightx*lowerrightx + lowerrighty*lowerrighty >= RAD*RAD)
                  lowerRightInside = 0;
               
               if(upperLeftInside == 1 && lowerRightInside == 1)
               {
                  //both are inside
                  long double upperIntx = sqrt(RAD*RAD - upperlefty*upperlefty);
                  long double rightInty = sqrt(RAD*RAD - lowerrightx*lowerrightx);
                  
                  long double area = atan2(upperlefty,upperIntx) - atan2(rightInty, lowerrightx);
                  area *= (RAD*RAD);
                  
                  long double leftInty = (upperleftx*upperlefty/upperIntx);
                  long double bottomIntx = (lowerlefty/rightInty)*lowerrightx;
                  
                  area -= (leftInty-lowerlefty)*lowerleftx;
                  area -= (bottomIntx-lowerleftx)*lowerlefty;
                  area += (lowerrightx - bottomIntx)*(rightInty-lowerlefty);
                  area += (upperIntx-upperleftx)*(upperlefty-leftInty);                  
                  area *= 0.5;
                  ans += area;
               }
               else if(upperLeftInside == 0 && lowerRightInside == 0)
               {
                  //both are outside
                  
                  long double bottomIntx = sqrt(RAD*RAD - lowerlefty*lowerlefty);
                  long double leftInty = sqrt(RAD*RAD - lowerleftx*lowerleftx);

                  long double area = atan2(leftInty,lowerleftx) - atan2(lowerlefty,bottomIntx);
                  area *= (RAD*RAD);
                  
                  area -= (leftInty-lowerlefty)*lowerleftx;
                  area -= (bottomIntx-lowerleftx)*lowerlefty;
                  area *= 0.5;
                  ans += area;
               }
               else if(upperLeftInside == 0 && lowerRightInside == 1)
               {
                  long double leftInty = sqrt(RAD*RAD - lowerleftx*lowerleftx);
                  long double rightInty = sqrt(RAD*RAD - lowerrightx*lowerrightx);
                  
                  long double area = atan2(leftInty,upperleftx) - atan2(rightInty, lowerrightx);
                  area *= (RAD*RAD);
                  
                  long double bottomIntx = (lowerlefty/rightInty)*lowerrightx;
                  
                  area -= (leftInty-lowerlefty)*lowerleftx;
                  area -= (bottomIntx-lowerleftx)*lowerlefty;
                  area += (lowerrightx - bottomIntx)*(rightInty-lowerlefty);
                  area *= 0.5;
                  ans += area;
               }
               else
               {
                  long double upperIntx = sqrt(RAD*RAD - upperlefty*upperlefty);
                  long double bottomIntx = sqrt(RAD*RAD - lowerlefty*lowerlefty);
                  
                  long double area = atan2(upperlefty,upperIntx) - atan2(lowerlefty, bottomIntx);
                  area *= (RAD*RAD);

                  long double leftInty = (upperleftx*upperlefty/upperIntx);
                  
                  area -= (leftInty-lowerlefty)*lowerleftx;
                  area -= (bottomIntx-lowerleftx)*lowerlefty;
                  area += (upperIntx-upperleftx)*(upperlefty-leftInty);                                    
                  area *= 0.5;
                  ans += area;
               }
            
               ytop += (2.0*r + g);
            
//               fout << ans << endl;
               
               if((ytop-g)*(ytop-g) + xleft*xleft >= R*R)
                  break;
            }
            else
            {
               ans += (g-2.0*f)*(g-2.0*f);
    //           fout << ans << endl;
               ytop += (2.0*r + g);
            }      
         }
         xleft = xleft + g + 2.0*r;
      }
      
      ans *= 4;
      
      long double denom = PI*R*R;
   
  //    fout << denom << endl;


      fout << "Case #" << k << ": ";
      ans /= denom;
      ans = 1.0 - ans;
      
      long long LL = (ans+0.0000005)*1000000;
      
      if(LL >= 1000000)
         fout << "1.000000\n";
      else 
      {
         fout << "0.";
         fout << (LL/100000)%10;
         fout << (LL/10000)%10;
         fout << (LL/1000)%10;
         fout << (LL/100)%10;
         fout << (LL/10)%10;
         fout << LL%10;
         fout << endl;
      }
      
      
      
   }
   
   return 0; 
    
    
    
    
    
    
}

