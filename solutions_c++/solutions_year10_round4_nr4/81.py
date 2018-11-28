#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include<numeric>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define INFTY 100000000
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define SIZE(x) ((int)(x).size())

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

ll nwd(ll a,ll b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b ? a/b+1 : a/b; }
template <class T> inline T sqr(const T&a) { return a*a; }

VS parse(string s)
{
  string a;
  VS wyn;
  REP(i,(int)s.size())
    if (s[i]!=' ') a+=s[i];
    else if (!a.empty()) { wyn.PB(a); a=""; }
  if (!a.empty()) wyn.PB(a);
  return wyn;
}

int toi(char ch) { return int(ch)-int('0'); }

int chg(char ch) { return int(ch)-int('a'); }

int los(int m)
{
  return (int)((double)m*(rand()/(RAND_MAX+1.0)));
}

/* Podstawowe funkcje geometryczne */

#define X first
#define Y second

/* W przejsciu na double zamieniamy funkcje:
 * sinl, cosl, atanl, fabsl, sqrtl. */
typedef long double D;

const D PI=4.0*atanl(1.0);

typedef pair<D,D> PDD;
typedef struct { ll A,B,C; } prosta;
typedef struct { D A,B,C; } prostad;

/* Iloczyn wektorowy */
inline ll wekt(PII p0,PII p1,PII p2)
{ return (ll)(p1.X-p0.X)*(p2.Y-p0.Y)-(ll)(p2.X-p0.X)*(p1.Y-p0.Y); }

/* Iloczyn skalarny */
inline ll skal(PII p0,PII p1,PII p2)
{ return (ll)(p1.X-p0.X)*(p2.X-p0.X)+(ll)(p2.Y-p0.Y)*(p1.Y-p0.Y); }

/* Czy przechodzac przez wspolny koniec odcinkow p0p1 i p1p2 skrecamy 
 * w lewo (skret<0), prawo (skret>0) czy idziemy prosto (skret=0). */
inline ll skret(PII p0,PII p1,PII p2)
{ return wekt(p0,p2,p1); }

inline int sgn(ll x) { return x>0 ? 1 : x<0 ? -1 : 0; }

/* Czy odcinki p1p2 i p3p4 sie przecinaja? */
inline bool intersect(PII p1,PII p2,PII p3,PII p4)
{
	int x1=min(p1.X,p2.X),y1=min(p1.Y,p2.Y);
	int x2=max(p1.X,p2.X),y2=max(p1.Y,p2.Y);
	int x3=min(p3.X,p4.X),y3=min(p3.Y,p4.Y);
	int x4=max(p3.X,p4.X),y4=max(p3.Y,p4.Y);
	if (x2<x3 || x1>x4 || y2<y3 || y1>y4) return false;
	return sgn(wekt(p1,p3,p2))*sgn(wekt(p1,p4,p2))<=0 &&
	       sgn(wekt(p3,p1,p4))*sgn(wekt(p3,p2,p4))<=0;
}

void pisz(PII p) {	printf("%d %d\n",p.X,p.Y); }

/* Odleglosc dwoch punktow */
inline D d(PII p1,PII p2)
{	return sqrt(sqr(D(p1.X-p2.X))+sqr(D(p1.Y-p2.Y))); }
inline D d(PDD p1,PDD p2)
{	return sqrt(sqr(p1.X-p2.X)+sqr(p1.Y-p2.Y)); }

/* Kat skierowany miedzy odcinkiem p0-p1 a p0-p2 W STOPNIACH */
inline D kat(PII p0,PII p1,PII p2)
{
  D sinus=(D)wekt(p0,p1,p2)/((D)d(p0,p1)*d(p0,p2));
  D cosinus=(D)skal(p0,p1,p2)/((D)d(p0,p1)*d(p0,p2));
  D alfa=asinl(sinus);
  if (cosinus<0.0) alfa=PI-alfa; else if (alfa<0.0) alfa+=2.0*PI;
  return alfa*180.0/PI; /* tu zamiana na stopnie */
}

/* Zamiana para pktow->prosta */
inline prosta prostuj(PII p1,PII p2)
{
  prosta w;
  w.A=(ll)p1.Y-p2.Y;
  w.B=(ll)p2.X-p1.X;
  w.C=(ll)p1.X*(p2.Y-p1.Y)-(ll)p1.Y*(p2.X-p1.X);
  return w;
}

/* Zamiana para pktow->prosta */
inline prostad prostuj(PDD p1,PDD p2)
{
  prostad w;
  w.A=p1.Y-p2.Y;
  w.B=p2.X-p1.X;
  w.C=p1.X*(p2.Y-p1.Y)-p1.Y*(p2.X-p1.X);
  return w;
}

/* Przeciecie dwoch prostych; 0- 1 pkt, 1- || rozlaczne,
 *                            2- te same (zwraca przykladowy punkt) */
inline pair<int,PDD> przec(prosta w1,prosta w2) 
{
  PDD w;
  /* w - jakis punkt na prostej w1 */
  if (w1.A) w=MP(-D(w1.C)/w1.A, 0.0);
  else w=MP(0.0, -D(w1.C)/w1.B);
  if (w1.A*w2.B==w1.B*w2.A) /* DOKLADNOSC TYPU!!! */
  {
    if (w1.B*w2.C==w1.C*w2.B) return MP(2,w);
    else return MP(1,w);
  }
  D m=D(w1.A*w2.B-w2.A*w1.B);
  w.X=D(w1.B*w2.C-w2.B*w1.C)/m;
  w.Y=D(w1.C*w2.A-w2.C*w1.A)/m;
  return MP(0,w);
}

/* Przeciecie dwoch prostych; 0- 1 pkt, 1- || rozlaczne,
 *                            2- te same (zwraca przykladowy punkt) */
inline pair<int,PDD> przec(prostad w1,prostad w2) 
{
  PDD w;
  /* w - jakis punkt na prostej w1 */
  if (fabsl(w1.A)>1e-9) w=MP(-w1.C/w1.A, 0.0);
  else w=MP(0.0, -w1.C/w1.B);
  if (fabsl(w1.A*w2.B-w1.B*w2.A)<1e-9)
  {
    if (fabsl(w1.B*w2.C-w1.C*w2.B)<1e-9) return MP(2,w);
    else return MP(1,w);
  }
  D m=w1.A*w2.B-w2.A*w1.B;
  w.X=(w1.B*w2.C-w2.B*w1.C)/m;
  w.Y=(w1.C*w2.A-w2.C*w1.A)/m;
  return MP(0,w);
}

/* Przeciecie 2 odcinkow; 0- 1 pkt, 1- rozlaczne,
 *                        2- duzo pktow (zwraca przykladowy punkt) */
inline pair<int,PDD> przec(PII p1,PII p2,PII p3,PII p4)
{
  if (!intersect(p1,p2,p3,p4)) return MP(1,MP(0.0,0.0));
  if (p1==p2) return MP(0, MP((D)p1.X,(D)p1.Y));
  if (p3==p4) return MP(0, MP((D)p3.X,(D)p3.Y));
  pair<int,PDD> wyn=przec(prostuj(p1,p2),prostuj(p3,p4));
  if (wyn.FI==2) // czy moze nie 1-pktowe przeciecie?
  {
    if (p1==p3 || p1==p4) swap(p1,p2);
    if (p2==p4) swap(p3,p4);
    if (p2==p3 && skal(p2,p1,p4)<0) return MP(0, MP((D)p2.X,(D)p2.Y));
    if (intersect(p1,p1,p3,p4)) return MP(2, MP((D)p1.X,(D)p1.Y));
    if (intersect(p2,p2,p3,p4)) return MP(2, MP((D)p2.X,(D)p2.Y));
    if (intersect(p3,p3,p1,p2)) return MP(2, MP((D)p3.X,(D)p3.Y));
    if (intersect(p4,p4,p1,p2)) return MP(2, MP((D)p4.X,(D)p4.Y));
  } else return wyn;
}

/* Dwusieczna kata zawartego miedzy p2-p1 a p2-p3 */
prostad dwus(PII p1,PII p2,PII p3)
{
  D alfa=kat(p2,p1,p3)/2.0*PI/180.0;
  PDD p=p1;
  p.X-=p2.X; p.Y-=p2.Y;
  D x,y; x=p.X*cosl(alfa)-p.Y*sinl(alfa); y=p.X*sinl(alfa)+p.Y*cosl(alfa);
  return prostuj(MP((D)p2.X,(D)p2.Y),MP(x+p2.X, y+p2.Y));
}

/* Pole wielokata PODWOJONE
 * Jezeli wierzcholki podane anticlockwise, to pole >=0, wpp. pole<=0. */
ll pole(vector<PII> t)
{
  ll wyn=0;
  REP(i,(int)t.size())
  {
    int j=i+1; if (j>=(int)t.size()) j=0;
    wyn+=(ll)(t[i].X-t[j].X)*(t[i].Y+t[j].Y);
  }
  return wyn;
}

int ILE;

PII a,b,p;
int n,m;

D doit()
{
  D r1=d(a,p), r2=d(b,p);
  D odl=d(a,b);
  if (odl>r1+r2) return 0.0;
  if (odl+r1<=r2) return M_PI*sqr(r1);
  if (odl+r2<=r1) return M_PI*sqr(r1);

  return sqr(r1) * acosl( (sqr(odl)+sqr(r1)-sqr(r2))/(2.0*odl*r1) ) +
    sqr(r2) * acosl( (sqr(odl)+sqr(r2)-sqr(r1))/(2.0*odl*r2) ) -
    0.5 * sqrtl( (-odl+r1+r2) * (odl+r1-r2) * (odl-r1+r2) * (odl+r1+r2) );
}

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d:",iii);
    scanf("%d%d",&n,&m);
    scanf("%d%d",&(a.X),&(a.Y));
    scanf("%d%d",&(b.X),&(b.Y));
    while (m--)
    {
      scanf("%d%d",&(p.X),&(p.Y));
      printf(" %.10lf",double(doit()));
    }
    puts("");
  }
  return 0;
}
