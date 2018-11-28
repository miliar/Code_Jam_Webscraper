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

using namespace std;

#define FOR(a,b,c) for(int a=(int)(b);a<(int)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define SHIFT(a) (1LL<<(a))
#define PAIR pair<int,int>
#define BEGEND(a) (a).begin(), (a).end()
#define eps 1E-9
#define PI acos(-1.0)
#define INF 1000000000

//BEGIN CUT - Print Array
template<class T> 
void printArray(vector<T> & v) { FOR(i,0,v.size()) cout << v[i] << " "; cout << endl; }
template <class T>
void printArray(vector<vector<T> > &v){ FOR(i,0,v.size()) printArray(v[i]); cout << endl; }
//END CUT - Print Array

// BEGIN CUT - Concatenate
string concatenate(vector<string> &str){ string s; FOR(i,0,str.size()) s += str[i]; return s;}
// END CUT - Concatenate

// BEGIN CUT - Binary Search
long long  binarySearch(long long  low, long long high, bool (* _target) (long long t1)){
  while(low < high){ long long mid = low + (high - low) / 2; if(_target(mid)) high = mid; else low = mid+1;}
  return low;
}
long double binarySearch(long double low, long double high, bool (* _target) (long double t1)){
   while(low < high-eps){ long double mid = low + (high - low) / 2.0; if(_target(mid)) high = mid; else low = mid; }
   return low;
}
// END CUT - Binary Search

// BEGIN CUT - Ternary Search
long long ternarySearch(long long low, long long high, bool (* _better) (long long t1, long long t2)){
   while(low < high - 3){
      long long p1 = low + (high - low) / 3, p2 = low + 2 * (high - low) / 3;
      if(_better(p1, p2)) high = p2; else low = p1;
   }
   if(_better(low,low+1)) return low; else if(_better(low+1,low+2)) return low+1; else if(_better(low+2,low+3)) 
return low+2;
   return low+3;
}
long double ternarySearch(long double low, long double high, bool (* _better) (long double t1, long double t2)){
   while(low < high-eps){
      long double p1 = low + (high - low) / 3.0, p2 = low + 2 * (high - low) / 3.0;
      if(_better(p1, p2)) high = p2; else low = p1;
   }
   return low;
}
// END CUT - Ternary Search


// BEGIN CUT - Matrix Multiplication/Exponentiation
vector<vector<long long> > matrixMultiply(const vector<vector<long long> > & A, const vector<vector<long long> > &B){
  int nR = A.size(), nC = B[0].size(), com = B.size();  vector<vector<long long> > retMatrix;
  if(A[0].size() != com) cerr << "Fatal Matrix Error" << endl, exit(0);
  FOR(i,0,nR){ vector<long long> row;
     FOR(j,0,nC){ long long sum = 0; FOR(k,0,com) sum += A[i][k] * B[k][j]; row.push_back(sum);}
     retMatrix.push_back(row);
  }
  return retMatrix;
}

vector<vector<long long> > matrixExponentiate(vector<vector<long long> > matrix, int power){
   if(power == 1) return matrix; int size = matrix.size();
   vector<vector<long long> > current(size,vector<long long>(size,0));
   FOR(i,0,size) current[i][i] = 1;
   while(power > 0){ if(power & 1) current = matrixMultiply(current,matrix); matrix = matrixMultiply(matrix,matrix); power >>=1;   }
   return current;
}
//END CUT - Matrix Multiplication/Exponentiation


// BEGIN CUT - Maxflow
#define MF_NETWORK_SIZE 1
vector<int> _MFadjlist[MF_NETWORK_SIZE];
int _MFflow[MF_NETWORK_SIZE][MF_NETWORK_SIZE];
int _MFcapacity[MF_NETWORK_SIZE][MF_NETWORK_SIZE];
bool _MFvisited[MF_NETWORK_SIZE];

void initMF(){ memset(_MFflow,0,sizeof(_MFflow)); memset(_MFcapacity,0,sizeof(_MFcapacity)); FOR(i,0,MF_NETWORK_SIZE) 
_MFadjlist[i].clear(); }
void reset(){ memset(_MFflow,0,sizeof(_MFflow));}

bool aug_path_dfs(int cur, int snk){
   if(_MFvisited[cur]) return false; if(snk == cur) return true; _MFvisited[cur] = true;
   FOR(i,0,_MFadjlist[cur].size()){
      int tmp = _MFadjlist[cur][i];
      if(_MFflow[cur][tmp] >= _MFcapacity[cur][tmp]) continue;
      _MFflow[cur][tmp]++; _MFflow[tmp][cur]--;
      if(aug_path_dfs(tmp,snk)) return true;
      _MFflow[cur][tmp]--; _MFflow[tmp][cur]++;
   }
   return false;
}
void cullPath(const vector<int> &lst){ FOR(i,1,lst.size()) _MFcapacity[lst[i-1]][lst[i]] = 0; }
void restorePath(const vector<int> &lst){ FOR(i,1,lst.size()) _MFcapacity[lst[i-1]][lst[i]] = 1; }

int maxFlow(int src, int snk){
   assert(MF_NETWORK_SIZE!=1); int ret = 0;
   while(true){ memset(_MFvisited,false,sizeof(_MFvisited)); if(!aug_path_dfs(src,snk)) break;  ret++; } return ret;
}
void addMFConnection(int left, int right, int cap){
   _MFflow[left][right] = _MFflow[right][left] = 0;
   _MFcapacity[left][right] = cap; _MFcapacity[right][left] = 0;
   _MFadjlist[left].push_back(right); _MFadjlist[right].push_back(left);
}
// END CUT - Maxflow

// BEGIN CUT - Geometry Library
template <class T>
T distanceSquared(const vector<T> &p1, const vector<T> &p2){
    T ret = 0; FOR(i,0,p1.size()) ret += (p2[i] - p1[i]) * (p2[i] - p1[i]); return ret;
}

template <class T>
T distanceSquared(const pair<T,T> &p1, const pair<T,T> *p2){
   T ret = 0; ret += (p2.first - p1.first) * (p2.first - p1.first); ret += (p2.second - p1.second) * (p2.second - p1.second); return ret;
}

bool line_intersection2D(const vector<double> &p1, const vector<double> &p2, const vector<double> &q1, const 
vector<double> &q2,
	vector<double> &r, bool &colinear){
    colinear = false; r = vector<double>(2,0); double N1, N2, D, u1, u2;
    N1 = (q2[0] - q1[0]) * (p1[1] - q1[1]) - (q2[1] - q1[1]) * (p1[0] - q1[0]);
    N2 = (p2[0] - p1[0]) * (p1[1] - q1[1]) - (p2[1] - p1[1]) * (p1[0] - q1[0]);
    D  = (q2[1] - q1[1]) * (p2[0] - p1[0]) - (q2[0] - q1[0]) * (p2[1] - p1[1]);

    if(fabs(D) > eps) {
       u1 = N1 / D; u2 = N2/D; if(u1 < -eps || u1 > 1+eps || u2 < -eps || u2 > 1+eps) return false;
       r[0] = p1[0] + (p2[0] - p1[0]) * u1;  r[1] = p1[1] + (p2[1] - p1[0]) * u1; return true;
    } 
    if(fabs(N1) > eps && fabs(N2) > eps) return false; else colinear = true;
    if(p1[0] >= min(q1[0],q2[0]) && p1[0] <= max(q1[0],q2[0]) && p1[1] >= min(q1[1],q2[1]) && p1[1] <= max(q1[1],q2[1]))  { r = p1; return true;}
    if(p2[0] >= min(q1[0],q2[0]) && p2[0] <= max(q1[0],q2[0]) && p2[1] >= min(q1[1],q2[1]) && p2[1] <= max(q1[1],q2[1]))  { r = p2; return true;}
    return false;
}

bool line_intersection2D(const pair<double, double> &p1, const pair<double,double> &p2, const pair<double,double> 
&q1, pair<double,double> &q2, 
	pair<double, double> &r, bool &colinear){
    vector<double> pv1(2), pv2(2), qv1(2), qv2(2), rv;
    pv1[0] = p1.first; pv1[1] = p1.second; pv2[0] = p2.first; pv2[1] = p2.second;
    qv1[0] = q1.first; qv1[1] = q1.second; qv2[0] = q2.first; qv2[1] = q2.second;
    bool ret = line_intersection2D(pv1,pv2,qv1,qv2,rv,colinear);
    r.first = rv[0]; r.second = rv[1]; return ret;
}

template <class T>
T dot_product(vector<T> &p1, vector<T> &p2){
   T ret = 0; FOR(i,0,p1.size()) ret += p1[i] * p2[i];  return ret;
}
template <class T>
vector<T> cross_product(vector<T> &p1, vector<T> &p2){
    vector<T> ret(3);    ret[0] = p1[1] * p2[2] - p1[2] * p2[1]; ret[1] = p1[2] * p2[0] - p1[0] * p2[2]; ret[2] = p1[0] * p2[1] - p1[1] * p2[0]; return ret;
}
template <class T>
vector<T> cross_product(pair<T,T> &p1, pair<T,T> &p2){
    vector<T> v1(3), v2(3); v1[0] = p1.first; v1[1] = p1.second; v2[0] = p2.first; v2[1] = p2.second; return cross_product(v1,v2);
}
// END CUT - Geometry Library

// BEGIN CUT - Bellman-Ford
#define BF_NETWORK_SIZE 1
struct BFedge{ int src, dest, cost; };
vector<BFedge> _BFedgeList;
int _BFdistance[BF_NETWORK_SIZE]; 

void initBF(){_BFedgeList.clear();}
void addBFEdge(int from, int to, int cost) {  BFedge bfe; bfe.src = from; bfe.dest = to; bfe.cost = cost; _BFedgeList.push_back(bfe);}

bool bellman_ford(int src, int NV, int *_array = _BFdistance){
   assert(BF_NETWORK_SIZE!=1); FOR(i,0,NV){ _array[i] = INF;} _array[src] = 0;
   FOR(i,0,NV) FOR(j,0,_BFedgeList.size())
        if(_array[_BFedgeList[j].src] < INF){
           int nD = _array[_BFedgeList[j].src] + _BFedgeList[j].cost; _array[_BFedgeList[j].dest] = min(nD,_array[_BFedgeList[j].dest]);
        }
   FOR(i,0,_BFedgeList.size()) if(_array[_BFedgeList[i].dest] > _array[_BFedgeList[i].src] + _BFedgeList[i].cost) return false;
   return true;
}
// END CUT - Bellman-Ford

// BEGIN CUT - Graph Manipulation
vector<string> rotateR(const vector<string> &orig){ vector<string> ret(orig[0].length()); FOR(i,0,orig[0].length()) 
FOR(j,0,orig.size()) ret[i].push_back(orig[orig.size()-j-1][i]); return ret;}
vector<string> flipH(const vector<string> &orig){ vector<string> ret = orig; FOR(i,0,orig.size()) 
FOR(j,0,orig[0].length()) ret[i][j] = orig[i][orig.size()-j-1]; return ret;}
// END CUT - Graph Manipulation

//BEGIN CUT - Math Functions
long long gcd(long long A, long long B){  if(!A && !B) return 0;  return (A%B)?gcd(B,A%B):B; }
long long lcm(long long A, long long B){ if(!A && !B) return 0; return A / gcd(A,B) * B; }
//END CUT - Math Functions

//BEGIN CUT - Choose Function
long long choose(long long T, long long B){
  long long ret = 1;  vector<long long> top, bottom;
  if(T<B || B<0) return -1; B = min(B,T-B);
  FOR(i,0,B){ top.push_back(T-i); bottom.push_back(i+1); }
  FOR(i,0,top.size()) FOR(j,0,bottom.size()){ if(top[i]==1) break;
        long long g = gcd(top[i],bottom[j]); top[i]/=g; bottom[j]/=g;
        if(bottom[j]==1){ swap(bottom[bottom.size()-1],bottom[j--]); bottom.pop_back();}
     }
  FOR(i,0,top.size()) ret*=top[i]; return ret;
}
// END CUT - Choose Function

// BEGIN CUT - Flood Fill
#define _FLD_ROWS 1
#define _FLD_COLS 1
int fdr[] = {0,0,-1,1}, fdc[] = {-1,1,0,0};
bool floodmatrix[_FLD_ROWS][_FLD_COLS];
void initFlood(){ MEMSET(floodmatrix,false);}
int flood(int r, int c, int nR, int nC, bool (*invalid)(int,int)){ 
      if(r<0 || c<0 || r>=nR || c>=nC || floodmatrix[r][c] || invalid(r,c)) return 0;
      floodmatrix[r][c] = true; int ret =1;
      FOR(i,0,4) ret += flood(r+fdr[i],c+fdr[i],nR,nC,invalid); return ret;
}
// END CUT - Flood Fill

// BEGIN CUT - BFS
#define _BFS_ROWS 1
#define _BFS_COLS 1
int bfsdr[] = {0,0,-1,1}, bfsdc[] = {-1,1,0,0};
int bfsmatrix[_BFS_ROWS][_BFS_COLS];
void bfs(int r, int c, int numRows, int numCols){
       memset(bfsmatrix,-1,sizeof(bfsmatrix));
       vector<pair<int,int> > left(1,make_pair(r,c)); vector<int> dist(1,0);
       while(left.size() > 0){
         pair<int,int> p = left[0]; left.erase(left.begin());
         int d = dist[0]; dist.erase(dist.begin());
         if(p.first < 0 || p.second < 0 || p.first >=  numRows || p.second >= numCols || bfsmatrix[p.first][p.second]!=-1) continue;
         bfsmatrix[p.first][p.second] = d;
         // cout << "NEED TO PUT SOME MORE CODE HERE" << endl;
         cout << "NEED TO PUT SOME MORE CODE HERE" << endl;
         FOR(i,0,4) dist.push_back(d+1), left.push_back(make_pair(p.first + bfsdr[i],p.second + bfsdc[i]));
      }
}
// END CUT - BFS

int C, N, M, T;

int main(){
   cin >> C;
   FOR(loop,0,C){
     cin >> N >> M;
     vector<int> res(N,0);
     vector<vector<int> > clauses;
     bool okay = true;

     FOR(i,0,M){
	  cin >> T;
	  int v1, v2;
	  vector<int> have;
	  FOR(j,0,T) {cin >> v1 >> v2; have.push_back(v2?v1:-v1);}
	  clauses.push_back(have);
	}


     bool found;     
     do
     {
       found = false;
       FOR(i,0,clauses.size()) if(clauses[i].size()==1) {
	found = true;
	int v = clauses[i][0];
	if(v>0) res[v-1] = 1;

	clauses[i].clear();
	FOR(j,0,M) FOR(k,0,clauses[j].size())
		if(clauses[j][k] == v) clauses[j].clear();
		else if(clauses[j][k]==-v) {clauses[j].erase(clauses[j].begin()+k); if(clauses[j].size()==0) okay = false;}
	}
      }while(okay && found);
      cout << "Case #" << (loop+1) << ":";
      if(!okay) cout << " IMPOSSIBLE" << endl;
      else { FOR(i,0,res.size()) cout << " " << res[i]; cout << endl; }
   }	
   return 0;  
}
