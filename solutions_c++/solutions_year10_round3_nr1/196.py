#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<deque>
#include<algorithm>
using namespace std ;

typedef long long LL ;
typedef vector<int> VI ;
typedef pair<int,int> para ;

const int INF = 1000000000 ;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(i,c) for(__typeof((c).begin())i = (c).begin();i!=(c).end(); ++i)
#define ALL(x) x.begin(),x.end()

const double EPS = 1e-9;
inline bool IsZero(double x){ return x>=-EPS && x<=EPS; }
#define POINTT int // Dla wspolrzednych punktu (int lub double)
#define POINTR LL // Dla wynikow operacji - pole, iloczyn wektorowy (LL lub double)
struct POINT {
    POINTT x,y;
    POINT(POINTT wx, POINTT wy) : x(wx), y(wy) {}
    POINT() {}
    bool operator ==(POINT& a) {return a.x==x && a.y==y;}
};
#define Det(p1,p2,w) (POINTR(p2.x-p1.x)*POINTR(w.y-p1.y)-POINTR(p2.y-p1.y)*POINTR(w.x-p1.x))
int sgn(double x){ return IsZero(x)?0:(x < 0 ? -1 : 1); }
#define PointInRect(p1,p2,p3) (min(p1.x,p2.x) <= p3.x && min(p1.y,p2.y) <= p3.y && max(p1.x,p2.x) >= p3.x && max(p1.y,p2.y) >= p3.y)
#define PointInSegment(p1,p2,l) (Det(p1,p2,l)==0 && PointInRect(p1,p2,l))
inline bool SegmentCross(POINT& p1, POINT& p2, POINT& l1, POINT& l2) {
    return sgn(Det(p1,p2,l1))*sgn(Det(p1,p2,l2)) == -1 && sgn(Det(l1,l2,p1))*sgn(Det(l1,l2,p2)) == -1;
}

int D;

int main()
{
  scanf("%d",&D);
  FOR(I,1,D){
    printf("Case #%d: ",I);
    int n;
    POINT t[2][1007];
    scanf("%d",&n);
    REP(j,n)
    REP(i,2){
      int y;
      scanf("%d",&y);
      t[i][j]=POINT(i,y);
    }
    int wyn=0;
    REP(i,n)
    FOR(j,i+1,n-1)
    if(SegmentCross(t[0][i],t[1][i],t[0][j],t[1][j]))
    wyn++;
    printf("%d\n",wyn);
  }
	return 0 ;
}


