#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

int main()
{
  int n;
  std::cin >> n;
  
  for(int oo = 0;oo < n;oo++){
    double f,rr,t,r,g;
    std::cin >> f >> rr >> t >> r >> g;
//    std::cout << f << '\t' << rr << '\t' << t << '\t' << r << '\t' << g << std::endl;
    
    double p;
    if(g <= 2 * f){
      p = 1.0;
    }else{
      int nn = (int)((rr - t) / (g + 2 * r)) + 1;
      double pi = 3.14159265358979;
      double s = pi*rr*rr/4.0;
      double sq = g - 2 * f;
      double unit = g + 2 * r;
      double rrr = rr - t - f;
      double c = 0.0;
//        std::cout << "unit : " << unit << std::endl;
      for(int i = 0;i < nn;i++){
        double yu = unit * (double)i + g + r - f;
        double yl = unit * (double)i + r + f;
        for(int j = 0;j < nn;j++){
          double xu = unit * (double)j + g + r - f;
          double xl = unit * (double)j + r + f;
          if(xu * xu + yu * yu < rrr * rrr){
            c += sq * sq;
            continue;
          }
          
          if(xl * xl + yl * yl >= rrr * rrr){
            break;
          }
          
          bool lu = (xl * xl + yu * yu < rrr * rrr);
          bool rl = (xu * xu + yl * yl < rrr * rrr);
          if(lu){
            if(rl){
              double dx = sqrt(rrr * rrr - yu * yu) - xl;
              double dy = sqrt(rrr * rrr - xu * xu) - yl;
              double theta = pi * 0.5 - acos(yu / rrr) - acos(xu / rrr);
//              std::cout << yu << std::endl;
//              std::cout << xu << std::endl;
//              std::cout << theta << std::endl;
              
//              std::cout << "xxx" << (0.5 * (yu * dx + xu * dy - sq * xl - sq * yl) + theta * 0.5 * rrr * rrr) << std::endl;
              c += 0.5 * (yu * dx + xu * dy - sq * xl - sq * yl) + theta * 0.5 * rrr * rrr;
            }else{
              double dxu = sqrt(rrr * rrr - yu * yu) - xl;
              double dxl = sqrt(rrr * rrr - yl * yl) - xl;
              double theta = pi * 0.5 - acos(yu / rrr) - asin(yl / rrr);
              c += 0.5 * (yu * dxu - sq * xl - dxl * yl) + theta * 0.5 * rrr * rrr;
            }
          }else{
            if(rl){
              double dyu = sqrt(rrr * rrr - xu * xu) - yl;
              double dyl = sqrt(rrr * rrr - xl * xl) - yl;
              double theta = pi * 0.5 - acos(xu / rrr) - asin(xl / rrr);
              c += 0.5 * (xu * dyu - sq * yl - dyl * xl) + theta * 0.5 * rrr * rrr;
            }else{
              double dx = sqrt(rrr * rrr - yl * yl) - xl;
              double dy = sqrt(rrr * rrr - xl * xl) - yl;
              double theta = pi * 0.5 - asin(yl / rrr) - asin(xl / rrr);
//              std::cerr << "ooo" << (0.5 * (- dx * yl - dy * xl) + theta * 0.5 * rrr * rrr) << std::endl;
              c += 0.5 * (- dx * yl - dy * xl) + theta * 0.5 * rrr * rrr;
            }
          }
        } // j
      } // i
      p = 1.0 - c / s;
    }
    
    std::cout << "Case #" << (oo + 1) << ": ";
    fprintf(stdout, "%0.6f", p);
    std::cout << std::endl;
    
  }
  
  return 0;
}
