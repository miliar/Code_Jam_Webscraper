#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <complex>
#include <stack>
#include <cctype>
#include <cstdlib>
#include <iostream>

#define X real()
#define Y imag()
#define PB push_back
#define MP make_pair
#define FR(i,n) for( int i = 0; i < n; i ++ )
#define FOR(i,a,n) for(int i = a; i < n; i ++)
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )



using namespace std;


typedef double type;
typedef double ld;
#define EPS 5e-8
#define eps 5e-8

const ld PI = acos(-1);
// USE COUT (INT) CEIL, ALWAYS WITH INT

typedef double tipo;
using namespace std;

typedef double tipo;

struct punto {
    tipo x, y;
    punto(tipo a = 0, tipo b = 0) : x(a), y(b) {}
    bool operator<(const punto &b) const {
        if (x < b.x - eps) return true;
        if (x > b.x + eps) return false;
        return y < b.y - eps;
    }
    punto operator +(punto b) const { return punto(x + b.x, y + b.y); }
    punto operator -(punto b) const { return punto(x - b.x, y - b.y); }
    punto operator *(tipo r) const { return punto(x * r, y * r); }
    punto operator /(tipo r) const { return punto(x / r, y / r); }
    
    // Producto escalar
    tipo operator *(punto b) const { return x * b.x + y * b.y; }
    // Coordenada Z del producto vectorial
    tipo operator ^(punto b) const  { return x * b.y - y * b.x; }
    
    punto perp() { return punto(-y, x); }
    tipo mod2() const { return x * x + y * y; }
    double mod() const { return sqrt(x * x + y * y); }
    tipo distcuad(punto b) const {
        tipo dx = b.x - x, dy = b.y - y;
        return dx * dx + dy * dy;
    }
    
    /* Distancia a otro punto */
    double dist(punto b) const { return sqrt(distcuad(b)); }
    
    void normaliza() { // si usas esto con enteros te hostio
        tipo d = (tipo)mod();
        x /= d; y /= d;
    }
};

inline int signo(tipo x) { return x > eps ? 1 : x < -eps ? -1 : 0; }

/* Devuelve 1 si el punto c est· a la izquierda del segmento ab, -1 si est· a la derecha,
 * y 0 si est·n alineados.  0.2 us */
int sentido(punto a, punto b, punto c) {
    return signo((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x));
}

/* Devuelve -2 si dos cÌrculos son iguales, -1 si son concÈntricos y distintos,
 * 1 si no son concÈntricos y se cortan en al menos un punto, y 0 si no son 
 * concÈntricos y no se cortan */
int intercirculo(punto a, tipo ra, punto b, tipo rb, punto &s, punto &t) {
    tipo d = a.distcuad(b), x, y;
    if (d < eps) {
        if (fabs(ra - rb) < eps) return -2;
        return -1;
    }
    x = ra * ra - rb * rb + d;
    y = ra * ra - x * x / (4 * d);
    x /= (2 * sqrt(d));
    if (fabs(y) < eps) y = 0;
    if (y < 0) return 0;
    y = sqrt(y);
    punto v(b - a); v.normaliza();
    s = a + punto(x * v.x - y * v.y, y * v.x + x * v.y);
    t = a + punto(x * v.x + y * v.y, -y * v.x + x * v.y);
    return 1;
}


int ncands;
punto cands[3300];
punto cen[40];
double radd[40];
int main()
{
    int t,n;
    scanf("%d",&t);
    FR(i,t)
    {
        printf("Case #%d: ",i+1);        
        scanf("%d",&n);
      //  houses.clear();
        ld minx=10000.0,miny=10000.0,maxx=0.0,maxy=0.0;
        ld maxr=0.0;
        FR(i,n)
        {
            int x,y;
            scanf("%d %d",&x,&y);
            int cc;
            scanf("%d",&cc);
            radd[i]=cc;
            maxr=max(radd[i],maxr);
            minx=min((ld)x,minx);
            miny=min((ld)y,miny);
            maxy=max((ld)y,maxy);
            maxx=max((ld)x,maxx);
            cen[i]=punto(x,y);
        }
        int cccc=i;
        ld lw=maxr,hg=20000.0;
        ld rad;
        while(fabs(hg-lw)>EPS)
        {
            ncands=0;
            rad=(lw+hg)/2.0;
            FR(i,n) FOR(j,i,n)
            {
                if(i==j) cands[ncands++]=(cen[j]);
                if(i==j) continue;
                punto c1,c2;
                int res=intercirculo(cen[i],rad-radd[i],cen[j],rad-radd[j],c1,c2);                
                if(res==1)  cands[ncands++]=c1;
                if(res==1 &&c1.distcuad(c2)>eps) cands[ncands++]=c2;
            }

            FR(i,ncands)
                FOR(j,i,ncands)
            {
                // stupid pruning
        //        if(cands[i].x+rad<maxx-EPS&&cands[j].x+rad<maxx-EPS) continue;
        //        if(cands[i].y+rad<maxy-EPS&&cands[j].y+rad<maxy-EPS) continue;
        //        if(cands[i].y-rad>miny+EPS&&cands[j].y-rad>miny+EPS) continue;
        //        if(cands[i].x-rad>minx+EPS&&cands[j].x-rad>minx+EPS) continue;

                bool ok = true;
                FR(k,n)
                {      
              //     if(cccc==0) cout << cen[k].dist(cands[i]) << " " << radd[k] << " " << rad  << endl;
                    if(cen[k].dist(cands[i])+radd[k]>rad+EPS&&cen[k].dist(cands[j])+radd[k]>rad+EPS){
                      ok=false;
                        break;
                    }                     
                }
               // if(ok)
               // {
                //    cout << "ok with " << rad << endl;
               //     cout << cands[i].x << " " << cands[i].y << endl;
  //                  cout << cands[j].x << " " << cands[j].y << endl;
//
    //            }
                if(ok) goto SOL;
            }
            
            lw=rad;
            continue;
        SOL:
            
            hg=rad;
        }
        printf("%.8lf\n",rad);
        
        
    }
}
