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
#define X first
#define Y second
#define INFTY 100000000
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define SIZE(x) ((int)(x).size())

typedef vector<int> VI;
typedef vector<double> VD;
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

typedef double D;
typedef pair<D,D> PDD;

inline D d(PII p1,PII p2)
{	return sqrt(sqr(D(p1.X-p2.X))+sqr(D(p1.Y-p2.Y))); }
inline D d(PDD p1,PDD p2)
{	return sqrt(sqr(p1.X-p2.X)+sqr(p1.Y-p2.Y)); }

/* Rozwiazywanie ukladow rownan w R metoda Gaussa;
 * uklad ma macierzowa postac: Ax=b.
 * Zlozonosc: O(n^3). */

/* Zwraca rzad przestrzeni rozwiazan (-1 dla 0 rozwiazan)
 * i przykladowe rozwiazanie w x;
 * Indeksowanie: A[wiersz][kolumna], rozmiar b=liczba wierszy
 */
int gauss(vector<vector<double> > A,vector<double> b,vector<double> &x)
{
  int n=A.size(),m=A[0].size();
  int akt=0; /* aktywny wiersz */
  REP(i,m)
  {
    /* szukamy niezerowej pozycji w i-tej kolumnie */
    if (!A[akt][i])
      FOR(j,akt+1,n-1) if (fabs(A[j][i])>fabs(A[akt][i]))
      {
        swap(A[akt],A[j]); swap(b[akt],b[j]);
        break;
      }
    if (fabs(A[akt][i])<1e-8) continue;
    
    /* uzyskujemy 1 na przedzie i-tej kolumny */
    double z=A[akt][i];
    FOR(j,i,m-1) A[akt][j]/=z;
    b[akt]/=z;
    
    /* zerujemy i-te pola pozostalych kolumn */
    double pom;
    REP(j,n) if (j!=akt && fabs(A[j][i])>1e-8)
    {
      pom=A[j][i];
      FOR(k,i,m-1)
        A[j][k]-=A[akt][k]*pom;
      b[j]-=b[akt]*pom;
    }
    akt++;
    if (akt>=n) break;
  }
  /* Liczymy przykladowe rozwiazanie */
  x.clear(); x.resize(m,0);
  REP(i,akt) REP(j,m) if (fabs(A[i][j])>1e-8) { x[j]=b[i]; break; }
  /* Liczymy liczbe rozwiazan */
  FOR(i,akt,n-1) if (b[i]) return -1;
  return m-akt;
}

inline double wekt(PDD p0,PDD p1,PDD p2)
{ return (double)(p1.X-p0.X)*(p2.Y-p0.Y)-(double)(p2.X-p0.X)*(p1.Y-p0.Y); }

int ILE;
PII p[3],q[3];

int main()
{
  scanf("%d",&ILE);
  FOR(LICZ,1,ILE)
  {
    printf("Case #%d: ",LICZ);
    REP(i,3) scanf("%d%d",&(p[i].X),&(p[i].Y));
    REP(i,3) scanf("%d%d",&(q[i].X),&(q[i].Y));
    double f=double(d(p[0],p[1])/double(d(q[0],q[1])));
//    printf("f=%lf\n",f);
    double f1=f; f=sqr(f);
    double A,B,C;
    A=-2.0*p[0].X+f*2.0*q[0].X-(-2.0*p[1].X+f*2.0*q[1].X);
    B=-2.0*p[0].Y+f*2.0*q[0].Y-(-2.0*p[1].Y+f*2.0*q[1].Y);
    C=sqr(p[0].X)+sqr(p[0].Y)-f*sqr(q[0].X)-f*sqr(q[0].Y)-(sqr(p[1].X)+sqr(p[1].Y)-f*sqr(q[1].X)-f*sqr(q[1].Y));
    double A1,B1,C1;
    A1=-2.0*p[0].X+f*2.0*q[0].X-(-2.0*p[2].X+f*2.0*q[2].X);
    B1=-2.0*p[0].Y+f*2.0*q[0].Y-(-2.0*p[2].Y+f*2.0*q[2].Y);
    C1=sqr(p[0].X)+sqr(p[0].Y)-f*sqr(q[0].X)-f*sqr(q[0].Y)-(sqr(p[2].X)+sqr(p[2].Y)-f*sqr(q[2].X)-f*sqr(q[2].Y));
    vector<vector<double> > a;
    vector<double> b,x;
    VD pom;
    pom.PB(A); pom.PB(B); a.PB(pom); pom.clear();
    pom.PB(A1); pom.PB(B1); a.PB(pom); pom.clear();
    b.PB(-C); b.PB(-C1);
    int w=gauss(a,b,x);
    fprintf(stderr,"w=%d\n",w);
//    fprintf(stderr,"%lf %lf %lf\n",A,B,C);
//    fprintf(stderr,"%lf %lf %lf\n",A1,B1,C1);

    PDD p1[3],q1[3]; REP(i,3) p1[i]=p[i]; REP(i,3) q1[i]=q[i];
    PDD pp=MP(x[0],x[1]);
//    double aa=d(pp,p1[0])-f1*d(pp,q1[0]);
//    double bb=d(pp,p1[1])-f1*d(pp,q1[1]);
//    double cc=d(pp,p1[2])-f1*d(pp,q1[2]);
//    if (fabs(aa)>1e-6 || fabs(bb)>1e-6 || fabs(cc)>1e-6) { puts("No Solution1"); continue; }
//    aa=fabs(wekt(p1[0],p1[1],pp))+fabs(wekt(p1[1],p1[2],pp))+fabs(wekt(p1[2],p1[0],pp))-fabs(wekt(p1[0],p1[1],p1[2]));
//    bb=fabs(wekt(q1[0],q1[1],pp))+fabs(wekt(q1[1],q1[2],pp))+fabs(wekt(q1[2],q1[0],pp))-fabs(wekt(q1[0],q1[1],q1[2]));
//    printf("TU %lf %lf\n",aa,bb);
//    if (fabs(aa)>1e-6 || fabs(bb)>1e-6 || fabs(cc)>1e-6) { puts("No Solution1"); continue; }
    printf("%.10lf %.10lf\n",x[0],x[1]);
  }
  return 0;
}
