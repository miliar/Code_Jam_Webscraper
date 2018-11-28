#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <cassert>
using namespace std;

#define REP(a,b) for(int a = 0; (a) < (b); a++)
#define FFF(a,b,c) for(int a = (b); (a) <= (c); a++)
#define FOR(a,b,c) for(int a = (b); (a) <= (c); a++)
#define FOREACH(it, x) for(__typeof(x.begin()) it = (x).begin(); it != (x).end(); it++)
#define ALL(x) (x).begin(), (x).end()
int COND = 0; 
#define DB(x) { if (COND) cerr << __LINE__ << " " << #x << " " << x << endl;}
#define DB2(x) { if (0) cerr << __LINE__ << " " << #x << " " << x << endl;}
#define db DB
#define ll long long
#define ld long double
const ld PI = 2 * acos(0);
#define PB push_back
#define VV vector

#define X x
#define Y y
#define x first
#define y second
#define EPS 1e-9
#define PII po



int N;
#define po pair <ld, ld>
po operator * (po le, ld ri) { return po(le.x * ri, le.y * ri); }
po operator / (po le, ld ri) { return po(le.x / ri, le.y / ri); }

po operator + (po le, po ri) { return po(le.x + ri.x, le.y + ri.y); }
po operator - (po le, po ri) { return po(le.x - ri.x, le.y - ri.y); }

ld po_dist2(po rhs) { return sqrtl(rhs.x * rhs.x + rhs.y * rhs.y); }
po po_rotate(po rhs, ld alpha) { return po(rhs.x * cosl(alpha) - rhs.y * sinl(alpha), rhs.x * sinl(alpha) + rhs.y * cos(alpha)); }
ostream &operator << (ostream &os, po rhs) {
  os << rhs.x << " " << rhs.y;
  return os;
}
ld det(ld x1, ld y1, ld x2, ld y2) {
  return x1 * y2 - x2 * y1;
}
ld det(po le, po ri) {
  return le.x * ri.y - le.y * ri.x;
}

struct line {
  po le, ri;
  ld a, b, c;

  po LD, UR;
  line (po le_, po ri_){
    le = le_; ri = ri_;
    a = (le.y - ri.y);
    b = -(le.x - ri.x);
    c = le.x * a + le.y * b;
    //   db(c<<" "<<ri.x*a + ri.y*b);

    LD = po(min(le.x, ri.x), min(le.y, ri.y));
    UR = po(max(le.x, ri.x), max(le.y, ri.y)); 
  }

  ld dist(po rhs) {
    return abs(rhs.x * a + rhs.y * b - c) / sqrt(a * a + b * b);
  }


  ld dist_to_line(po rhs) {
    return abs(rhs.x * a + rhs.y * b - c) / sqrt(a * a + b * b);
  }

  void attach(po rhs) {
    c = rhs.x * a + rhs.y * b;
  }

  bool inside(po rhs) {
    return LD.x - EPS <= rhs.x && rhs.x <= UR.x + EPS
    &&  LD.y - EPS <= rhs.y && rhs.y <= UR.y + EPS;
  }


  bool SEGSEGCROSS(line rhs) {
    po cross = LINELINECROSS(rhs);
    return inside(cross) && rhs.inside(cross);
  }

  bool PARALLEL(line rhs) {
    return abs(det(a, rhs.a, b, rhs.b)) <= EPS;
  }

  po LINELINECROSS(line rhs) {
    ld mian = det(a, rhs.a, b, rhs.b);
    return po(det(c, rhs.c, b, rhs.b) / mian, det(a, rhs.a, c, rhs.c) / mian);
  }

  bool sameside(po p1, po p2) {
    ld c1 = p1.x * a + p1.y * b - c;
    ld c2 = p2.x * a + p2.y * b - c;
    return  (c1 <= 0 && c2 - EPS <= 0 || c1 >= 0 && c2 + EPS >= 0);
  }
  bool sameside2(po p1, po p2) {
    ld c1 = p1.x * a + p1.y * b - c;
    ld c2 = p2.x * a + p2.y * b - c;
    return  (c1 <= 0 && c2 + EPS < 0 || c1 >= 0 && c2 - EPS > 0);
  }
};

ld tr_field(ld a, ld b, ld c) {
  ld p = (a + b + c) / 2;
  return sqrt(p * (p - a) * (p - b) * (p - c));
}

struct circle {
  ld rad;
  po cen;
  circle() {}
  circle(ld rad_, po cen_) { rad = rad_; cen = cen_;
    
  }
  
  int CIRCLECROSS(circle rhs, po &p1, po &p2) {
    if (rad < rhs.rad) return rhs.CIRCLECROSS(*this, p1, p2);

    po ve = rhs.cen - cen;;
    ld d = po_dist2(ve);
    if (rad + rhs.rad + EPS < d) return 0;

    ld h = 2 * tr_field(rad, rhs.rad, d) / d;


    db(ve<<" "<<d);
    ve = ve * rad / d;
    ld angle = asinl(h / rad);
    p1 = cen + po_rotate(ve, angle);
    p2 = cen + po_rotate(ve, -angle);

    if (rad + rhs.rad - EPS <= d) return 1;
    return 2;
  }

  vector <PII> SEGCROSS(line &rhs) {
    vector <PII> result;
    ld h = rhs.dist(cen);
    ld d = sqrtl(max((ld)0, rad * rad - h * h));
    if (h - EPS <= rad) {
        PII v0 = PII(rhs.a, rhs.b) / po_dist2(PII(rhs.a, rhs.b));
        PII v1 = v0 * h;
        PII v2 = PII(v0.y, v0.x) * d;

        FOR (i, -1, 1) if (i) {
            PII ret = cen +  v1 * i;
            if (rhs.dist(ret) <= EPS) {
                FOR (j, -1, 1) if (j) {
                    PII pkt = ret + v2 * j;
                    if (rhs.inside(pkt))
                        result.PB(pkt);                    
                }

            }
        }

    }
    return result;
  }
};


//
void przyleg(circle le, circle ri, VV <line> &OUT) {
  if (le.rad > ri.rad) { przyleg(ri, le, OUT);
    return;
  }
  ///le.rad <= ri.rad
  ld d = po_dist2(le.cen - ri.cen);
  ld r1 = le.rad;
  ld r2 = ri.rad;
  ld h = r2 - r1;
  //  ld w = sqrt(d * d - h * h);
  
  ld alpha = PI / 2 + asin(h / d);

  po vct = ri.cen - le.cen;
  
  FFF (kat, -1, 1) if (kat != 0) {
    po v1 = po_rotate(vct, alpha * kat) / d;
    db(vct/d<<" "<<v1);
    po p1 = le.cen + v1 * r1;
    po p2 = ri.cen + v1 * r2;
    if (po_dist2(p1 - p2) > EPS) {
      // assert(abs(po_dist2(p1 - le.cen) - r1) <= EPS);
      //assert(abs(po_dist2(p2 - ri.cen) - r2) <= EPS);
      db(p1<<" "<<p2<<" "<<le.cen<<" "<<ri.cen);
      db(line(p1, p2).dist_to_line(le.cen)<<" "<<r1);
      db(line(p1, p2).dist_to_line(ri.cen)<<" "<<r2);
      
      //assert(abs(line(p1, p2).dist_to_line(le.cen) - r1) <= EPS);
      //      assert(abs(line(p1, p2).dist_to_line(ri.cen) - r2) <= EPS);

      OUT.PB(line(p1, p2));
     
    }
    else {
      
      /*

       */
    }
  }
}


void symetr(circle le, circle ri, VV<line> &OUT) {
  line tmp(le.cen, ri.cen);
  swap(tmp.a, tmp.b); tmp.a = -tmp.a;
  tmp.attach((le.cen + ri.cen) / 2);
  OUT.PB(tmp);
}


void przyleg2(circle le, circle ri, VV<line> &OUT) {
  if (le.rad > ri.rad) { przyleg2(ri, le, OUT);
    return;
  }
  ///le.rad <= ri.rad
  ld d = po_dist2(le.cen - ri.cen);
  ld r1 = le.rad;
  ld r2 = ri.rad;
  
  ld d1 = d * r1 / (r1 + r2);
  ld d2 = d * r2 / (r1 + r2);
  
  ld h1 = sqrt(d1 * d1 - r1 * r1);
  ld h2 = sqrt(d2 * d2 - r2 * r2);

  ld alpha = acos(r2 / d2); //jedno z nich moze byc zerem

  po vct = ri.cen - le.cen;
  
  db(d<<" "<<le.cen<<" "<<ri.cen);
  db(h1<<" "<<h2<<" "<<d1<<" "<<d2<<" "<<alpha<<" "<<r1<<" "<<r2);  

  FFF (kat, -1, 1) if (kat != 0) {
    po v1 = po_rotate(vct, alpha * kat) / d;
    po p1 = le.cen + v1 * r1;
    po p2 = ri.cen - v1 * r2;
    db(vct<<" "<<v1<<" "<<p1<<" "<<p2);
    db(po_dist2(p1 - p2)<<" "<<h1<<" "<<h2);
    if (po_dist2(p1 - p2) > EPS) {
   //   assert(abs(po_dist2(p1 - le.cen) - r1) <= EPS);
   //   assert(abs(po_dist2(p2 - ri.cen) - r2) <= EPS);

      db(line(p1, p2).dist_to_line(le.cen)<<" "<<r1);
      db(line(p1, p2).dist_to_line(ri.cen)<<" "<<r2);

      //      assert(abs(line(p1, p2).dist_to_line(le.cen) - r1) <= EPS);
      // a//ssert(abs(line(p1, p2).dist_to_line(ri.cen) - r2) <= EPS);
      OUT.PB(line(p1, p2));
    }
    else {
      /*    line tmp(le.cen, ri.cen);
      swap(tmp.a, tmp.b); tmp.a = -tmp.a;
      tmp.attach((le.cen + ri.cen) / 2);
      TMP.PB(tmp);
      */
    }
  }

}


inline ld wekt(PII p0,PII p1,PII p2)
{ return (ld)(p1.X-p0.X)*(p2.Y-p0.Y)-(ld)(p2.X-p0.X)*(p1.Y-p0.Y); }

inline ld skret(PII p0,PII p1,PII p2)
{ return wekt(p0,p2,p1); }

/* Zwraca wypukla otoczke w kolejnosci counterclockwise. */
#define RED() do { while (l>=2 && skret(tab[l-2],tab[l-1],t[i])>=0) { tab.pop_back(); l--; } tab.PB(t[i]); l++; } while (0);
vector<PII> graham(vector<PII> t)
{
  sort(ALL(t)); t.erase(unique(ALL(t)),t.end());
  int n=t.size();
  vector<PII> tab,tab1; int l=0;
  REP(i,n) RED();
  tab1=tab; tab.clear(); l=0;
  reverse(ALL(t));
  REP(i,n) RED();
  FOR(i,1,(int)tab.size()-2) tab1.PB(tab[i]);
  return tab1;
}

int main(int argc, char **argv) {   ios::sync_with_stdio(false); COND = argc >= 2 && argv[1][0] == 'q';
    ios::sync_with_stdio(false); 
 
    DB(PI);
    cin >> N;
    FOR (ii, 1, N) {
      DB(ii);
      cerr << ii << endl;
      ld sum = 0;
      ld f, R, t, r, g;
      cin >> f >> R >> t >> r >> g;
      r = r + min(g / 2, f);
      g = max((ld)0, g - 2 * f);
      t = min(R, t + f);
      ld rad = R - t;
      
      if (rad >= 0) {
	int dim = rad / (g + 2 * r) + 2;
	REP (a, dim)
	  REP (b, dim) {
	  //(a + r, b + r)
	  //(a + r + g, b + r + g)
	  vector<PII> poi;
	  vector<PII> quad;  
	  vector<PII> przec;     
	  REP (dx, 2) REP (dy, 2) { 
	    PII pkt(a * (2 * r + g) + r + g * dx, b * (2 * r + g) + r + g * dy);
	    quad.PB(pkt);
	    DB("");
	    if (po_dist2(pkt) - EPS <= rad) {
	      poi.PB(pkt);
	    }
	  }
	  swap(quad[2], quad[3]);
	  
	  REP (d, 4) {
	    line tmp(quad[d%4], quad[(d+1)%4]);
	    circle cen(max((ld)0, rad), PII(0,0));
            
	    vector <PII> res = cen.SEGCROSS(tmp);
	    FOREACH (it, res) { 
	      poi.PB(*it);
	      przec.PB(*it);
	    }
	  }
	  REP (i, przec.size()) {
	    REP (j, i) {
	      if (po_dist2(przec[i] - przec[j]) <= EPS) {
		przec.erase(przec.begin() + i);
		i--;
		break;
	      }
	    }
	  }


	  assert(przec.size() == 2 || przec.size() == 0);
	  if (przec.size() == 2) {
	    ld d = po_dist2(przec[0] - przec[1]);
	    DB2(przec[0].X<<" "<<przec[0].Y);
	    DB2(przec[1].X<<" "<<przec[1].Y);
	    ld h = sqrtl(rad * rad - (d/2)*(d/2));
	    
	    ld angle = 2 * asin((d/2) / rad);
	    DB2(rad<<" "<<d<<" "<<h<<" "<<angle<<" "<<angle *  pow(rad, 2)<<" "<<d*h);
	    

	    sum += abs(angle / 2 * pow(rad, 2)) - abs(d * h) / 2; 
	  }

	  DB2("");
	  FOREACH (it, poi) DB2(it->X<<" "<<it->Y);
	  
	  vector<PII> otoczka = graham(poi);
	  

	  ld pole = 0;
	  int K = otoczka.size();

	  DB2(K);
	  REP (i, K) {
	    pole += otoczka[i].X * otoczka[(i+1)%K].Y - otoczka[i].Y * otoczka[(i+1)%K].X;
	  }                                
	  sum += abs(pole) / 2;
	  DB(pole);
	}
      }
      
      ld totalfield = (PI * (R) * (R) / 4);
      DB2(sum);
      DB2(PI <<" " <<sum <<" "<<totalfield);
      
      printf("Case #%d: %.9Lf\n", ii, (totalfield - sum) / totalfield);
    }
    

    return 0;
}


