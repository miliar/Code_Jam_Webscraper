#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <cassert>
using namespace std;

#define FOR(a,b,c) for(int a=(int)(b);a<(int)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define PAIR pair<int,int>
#define BEGEND(a) (a).begin(), (a).end()
#define SHIFT(v) (1LL<<(v))
#define SQ(a) ((a) * (a))
#define LSB(a,b) (b<=sizeof(a)?(b & (SHIFT(a)-1)):-1)

#define eps 1E-9
#define PI acos(-1.0)
#define INF 1000000000
#define LINF 90000000000000000000LL
#define LLMAX ((unsigned long long)(-1))

// BEGIN CUT - Geometry Library = O(dimensions)
template <class T>
T distanceSquared(const vector<T> &p1, const vector<T> &p2){ T ret = 0; FOR(i,0,p1.size()) ret += SQ(p2[i] - p1[i]); return ret;}
template <class T>
inline T distanceSquared(const pair<T,T> p1, const pair<T,T> p2){ return SQ(p2.first - p1.first) + SQ(p2.second - p1.second);}
bool line_intersection2D(const vector<double> &p1, const vector<double> &p2, const vector<double> &q1, const vector<double> &q2, vector<double> &r, bool &colinear){
    colinear = false; r = vector<double>(2,0); double N1, N2, D, u1, u2; N1 = (q2[0] - q1[0]) * (p1[1] - q1[1]) - (q2[1] - q1[1]) * (p1[0] - q1[0]); N2 = (p2[0] - p1[0]) * (p1[1] - q1[1]) - (p2[1] - p1[1]) * (p1[0] - q1[0]);  D  = (q2[1] - q1[1]) * (p2[0] - p1[0]) - (q2[0] - q1[0]) * (p2[1] - p1[1]);
    if(fabs(D) > eps) { u1 = N1 / D; u2 = N2/D; if(u1 < -eps || u1 > 1+eps || u2 < -eps || u2 > 1+eps) return false; r[0] = p1[0] + (p2[0] - p1[0]) * u1;  r[1] = p1[1] + (p2[1] - p1[0]) * u1; return true;} 
    if(fabs(N1) > eps && fabs(N2) > eps) return false; else colinear = true; if(p1[0] >= min(q1[0],q2[0]) && p1[0] <= max(q1[0],q2[0]) && p1[1] >= min(q1[1],q2[1]) && p1[1] <= max(q1[1],q2[1]))  { r = p1; return true;}  if(p2[0] >= min(q1[0],q2[0]) && p2[0] <= max(q1[0],q2[0]) && p2[1] >= min(q1[1],q2[1]) && p2[1] <= max(q1[1],q2[1]))  { r = p2; return true;} return false;
}
bool line_intersection2D(const pair<double, double> &p1, const pair<double,double> &p2, const pair<double,double> &q1, pair<double,double> &q2, pair<double, double> &r, bool &colinear){ vector<double> pv1(2), pv2(2), qv1(2), qv2(2), rv; pv1[0] = p1.first; pv1[1] = p1.second; pv2[0] = p2.first; pv2[1] = p2.second; qv1[0] = q1.first; qv1[1] = q1.second; qv2[0] = q2.first; qv2[1] = q2.second; bool ret = line_intersection2D(pv1,pv2,qv1,qv2,rv,colinear); r.first = rv[0]; r.second = rv[1]; return ret;}
template <class T>
T dot_product(vector<T> &p1, vector<T> &p2){ T ret = 0; FOR(i,0,p1.size()) ret += p1[i] * p2[i];  return ret; }
template <class T>
vector<T> cross_product(vector<T> &p1, vector<T> &p2){ vector<T> ret(3);    ret[0] = p1[1] * p2[2] - p1[2] * p2[1]; ret[1] = p1[2] * p2[0] - p1[0] * p2[2]; ret[2] = p1[0] * p2[1] - p1[1] * p2[0]; return ret; }
template <class T>
vector<T> cross_product(pair<T,T> &p1, pair<T,T> &p2){ vector<T> v1(3), v2(3); v1[0] = p1.first; v1[1] = p1.second; v2[0] = p2.first; v2[1] = p2.second; return cross_product(v1,v2); }
// END CUT - Geometry Library

long long N, M,A;
int main(){
  int C;
  cin >> C;

  FOR(i,0,C){
    cin >> N >> M >> A;
    bool possible = false;
    int data[4];

    FOR(x1,0,N+1) FOR(y1,0,M+1) FOR(x2,0,N+1) FOR(y2,0,M+1){
	   if(possible) break;
	   if(x1==0&&y1==0 || x2==0&&y2==0 || x1==x2 && y1==y2) continue;
           if(abs(x1*y2-x2*y1) == A) data[0]=x1, data[1]=y1, data[2]=x2, data[3]=y2, possible = true;
	   
	}

    cout << "Case #" << (i+1) << ": ";    
    if(!possible) cout << "IMPOSSIBLE" << endl;
    else cout << "0 0 " << data[0] << " " << data[1] << " " << data[2] << " " << data[3] << endl;
  }
  return 0;
}
