#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <cmath>

const double EPS = 1e-10;
const double PI = acos(-1.0);

double f, R, t, r, g, sqd;

inline double sectorS(double ax, double ay, double bx, double by){
  return (R-t)*(R-t)/2.0 * acos((ax*bx + ay*by)/(R-t)/(R-t));
}

inline double triaS(double ax, double ay, double bx, double by){
  return fabs(ax*by - ay*bx) / 2.0;
}

inline double tS(double ax, double ay, double bx, double by, double cx, double cy){
  return triaS(bx-ax, by-ay, cx-ax, cy-ay);
}

double calcS(){
  double res = 0, cx = r + g/2.0, cy;
  double px, py, qx, qy, rx, ry, sx, sy, tres;
  int pt, qt, rt, st;
  int i;
  for (i=0;i<=1000;i++,cx+=2*r+g){
    cy = r + g/2.0;
    while (((cx-sqd)*(cx-sqd) + (cy-sqd)*(cy-sqd)) <= (R-t)*(R-t) + EPS){
      qt = st = 0;
      pt = rt = 0;
      if (R-t >= cx-sqd - EPS){
        double zy = sqrt((R-t)*(R-t) - (cx-sqd)*(cx-sqd));
        if ((zy >= cy-sqd-EPS) && (zy <= cy+sqd+EPS)){
          px = qx = cx-sqd;
          py = qy = zy;
          pt = 1;
          qt = 1;
        }
      }
      if (R-t >= cy+sqd - EPS){
        double zx = sqrt((R-t)*(R-t) - (cy+sqd)*(cy+sqd));
        if ((zx >= cx-sqd-EPS) && (zx <= cx+sqd+EPS)){
          px = zx;
          py = cy+sqd;
          pt = 2;
          double tty;
          if (px > EPS) tty =py * (cx-sqd) / px;
          else tty = py;
          if (tty >= cy-sqd-EPS){
            qx = cx-sqd;
            qy = tty;
            qt = 1;
          }
          else{
            qx = px * (cy-sqd) / (cy+sqd);
            qy = cy-sqd;
            qt = 2;
          }
        }
      }
      if (R-t >= cy-sqd - EPS){
        double zx = sqrt((R-t)*(R-t) - (cy-sqd)*(cy-sqd));
        if ((zx >= cx-sqd-EPS) && (zx <= cx+sqd+EPS)){
          ry = sy = cy-sqd;
          rx = sx = zx;
          st = 1;
          rt = 1;
        }
      }
      if (R-t >= cx+sqd - EPS){
        double zy = sqrt((R-t)*(R-t) - (cx+sqd)*(cx+sqd));
        if ((zy >= cy-sqd-EPS) && (zy <= cy+sqd+EPS)){
          ry = zy;
          rx = cx+sqd;
          rt = 2;
          double ttx;
          if (ry > EPS) ttx = rx * (cy-sqd) / ry;
          else ttx = rx;
          if (ttx >= cx-sqd-EPS){
            sy = cy-sqd;
            sx = ttx;
            st = 1;
          }
          else{
            sy = ry * (cx-sqd) / (cx+sqd);
            sx = cx-sqd;
            st = 2;
          }
        }
      }
      tres = 0;
      if ((pt == 1) && (rt == 1)){
        tres = sectorS(px, py, rx, ry);
        tres -= triaS(qx, qy, cx-sqd, cy-sqd);
        tres -= triaS(sx, sy, cx-sqd, cy-sqd);
      }
      else if ((pt == 1) && (rt == 2) && (st == 1)){
        tres = sectorS(px, py, rx, ry);
        tres -= triaS(qx, qy, cx-sqd, cy-sqd);
        tres -= triaS(sx, sy, cx-sqd, cy-sqd);
        tres += tS(sx, sy, rx, ry, cx+sqd, cy-sqd);
      }
      else if ((pt == 1) && (rt == 2) && (st == 2)){
        tres = sectorS(px, py, rx, ry);
        tres -= triaS(qx, qy, sx, sy);
        tres += sqd * (sy-cy+sqd + ry-cy+sqd);
      }
      else if ((pt == 2) && (qt == 1)){
        if (rt == 1){
          tres = sectorS(px, py, rx, ry);
          tres -= triaS(qx, qy, cx-sqd, cy-sqd);
          tres -= triaS(sx, sy, cx-sqd, cy-sqd);
          tres += tS(px, py, qx, qy, cx-sqd, cy+sqd);
        }
        if ((rt == 2) && (st == 1)){
          tres = sectorS(px, py, rx, ry);
          tres -= triaS(qx, qy, cx-sqd, cy-sqd);
          tres -= triaS(sx, sy, cx-sqd, cy-sqd);
          tres += tS(px, py, qx, qy, cx-sqd, cy+sqd);
          tres += tS(sx, sy, rx, ry, cx+sqd, cy-sqd);
        }
        if ((rt == 2) && (st == 2)){
          tres = sectorS(px, py, rx, ry);
          tres -= triaS(qx, qy, sx, sy);
          tres += tS(px, py, qx, qy, cx-sqd, cy+sqd);
          tres += sqd * (sy-cy+sqd + ry-cy+sqd);
        }
      }
      else if ((pt == 2) && (qt == 2)){
        if (rt == 1){
          tres = sectorS(px, py, rx, ry);
          tres -= triaS(qx, qy, sx, sy);
          tres += sqd * (px-cx+sqd + qx-cx+sqd);
        }
        if ((rt == 2) && (st == 1)){
          tres = sectorS(px, py, rx, ry);
          tres -= triaS(qx, qy, sx, sy);
          tres += sqd * (px-cx+sqd + qx-cx+sqd);
          tres += tS(rx, ry, sx, sy, cx+sqd, cy-sqd);
        }
      }
      else{
        tres = 4*sqd*sqd;
      }
      res += tres;
      cy += 2*r + g;
    }
  }
  return res;
}

int main(){
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  int tn, tst;
  scanf("%d", &tn);
  for (tst=1; tst<=tn; tst++){
    printf("Case #%d: ", tst);
    scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
    if (2*f >= g-EPS){
      printf("1.000000\n");
      continue;
    }
    sqd = (g/2.0 - f);
    t += f;
    double z = calcS();
    printf("%.6lf\n", 1 - 4*z/PI/R/R);    
  }
  return 0;
}