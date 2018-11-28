#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <map>
#include <complex>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <cassert>
#include <string.h>
#include <gmp.h>
using namespace std;

#define FOR(a,b,c) for(long long a=(long long)(b);a<(long long)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define SUBSET(a,b) for(long long a = b; a!=0; a = (b & (a-1)))
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define PAIR pair<long long,long long>
#define BEGEND(a) (a).begin(), (a).end()
#define SHIFT(v) (1LL<<(v))
#define SQ(a) ((a) * (a))
#define LSB(a,b) (b<=sizeof(a)?(b & (SHIFT(a)-1)):LLMAX)

#define eps 1E-9
#define PI acos(-1.0)
#define INF 1000000000
#define LLINF ((1LL<<62)-1)


// ---------------------------------------------------------------------------------
//BEGIN CUT - Print Array - O(N)
void printArray(const vector<string> & v) { FOR(i,0,v.size()) cout << v[i] << endl; cout << endl; }
template<class T> 
void printArray(const vector<T> & v) { FOR(i,0,v.size()) cout << v[i] << " "; cout << endl; }
template <class T>
void printArray(const vector<vector<T> > &v){ FOR(i,0,v.size()) printArray(v[i]);}
//END CUT - Print Array

//BEGIN CUT - Graph deltas
int dr4[] = {0,0,-1,1},           dc4[] = {1,-1,0,0};
int dr8[] = {0,0,1,1,1,-1,-1,-1}, dc8[] = {1,-1,-1,0,1,-1,0,1};
//END CUT - Graph deltas

// BEGIN CUT - Misc. Data
string months[] = {"January","February","March","April","May","June","July","August","September","October","November","December"};
string daysOfWeek[] = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
int daysOfMonth[] = {31,28,31,30,31,30,31,31,30,31,30,31};

string lettersU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string lettersL = "abcdefghijklmnopqrstuvwxyz";
// BEGIN CUT - Misc. Data

//BEGIN CUT - HexStuff [ USED BY Bigint ]
string _hexdigits = "0123456789ABCDEF";
unsigned long long toHexLong(string str){ unsigned long long num = 0; FOR(i,0,str.length()) { num<<=4; if(isalpha(str[i])) num += (str[i]-'A'+10); else num += (str[i]-'0');} return num; }
string toHexString(unsigned long long num) {string ret; FOR(k,0,16) { ret += _hexdigits[((num>>(k<<2))&0xF)]; } reverse(ret.begin(),ret.end()); return ret;}
//END CUT - HexStuff

//BEGIN CUT - Math Functions - O(digits^2) [ USED By Bigint, Choose, Frac]
long long gcd(long long A, long long B){  if(!A && !B) return 0;  return (A%B)?gcd(B,A%B):B; }
long long lcm(long long A, long long B){ if(!A && !B) return 0; return A / gcd(A,B) * B; }
long long gcdext(long long A, long long B, long long &Aout, long long &Bout, long long cmod){ long long r,t; if(A%B==0) { Aout = 0, Bout = 1; r = B; } else{ r = gcdext(B,A%B,Aout,Bout,cmod); t = Bout; Bout = (Aout - A/B * Bout) % cmod; Aout = t;} return r;}
long long ModDiv(long long num, long long denom, long long mod){ long long A, B; gcdext(mod,denom,A,B,mod); return ((num * B) % mod + mod) % mod;}
//END CUT - Math Functions

//BEGIN CUT - Random Functions [ USED BY Bigint]
static bool _seeded = false;
unsigned long long lrand(int seed=-1){ if(!_seeded) _seeded=true,srand((seed==-1)?time(0):seed); return ((((unsigned long long)rand())<<32) | rand());}
//END CUT - Random Functions
// ---------------------------------------------------------------------------------

//BEGIN CUT - AVL Trees structure
#define _AVLSIZE 1
template <class T>
struct AVLTree{
 private:
   int _AVLleftChild[_AVLSIZE], _AVLrightChild[_AVLSIZE], _AVLparent[_AVLSIZE], _AVLdepth[_AVLSIZE], _AVLdescendants[_AVLSIZE]; int _AVLroot, _AVLtotal; bool _AVLbalanced; T _AVLdata[_AVLSIZE]; int _AVLleftCount[_AVLSIZE], _AVLrightCount[_AVLSIZE];
   int _AVLrightMost(int index){ return (_AVLrightChild[index] == -1)?index:_AVLrightMost(_AVLrightChild[index]); }
   int _AVLleftMost(int index){ return (_AVLleftChild[index] == -1)?index:_AVLleftMost(_AVLleftChild[index]); }
   int _AVLgetDepth(int index){ if(index == -1) return -1; else return _AVLdepth[index];}
   int _AVLgetDescendants(int index){ if(index==-1) return 0; else return _AVLdescendants[index];}
   int _AVLgetBalance(int index){ if(index == -1) return -1; else return _AVLgetDepth(_AVLrightChild[index]) - _AVLgetDepth(_AVLleftChild[index]);}
   void _AVLleftRotate(int rt, int pivot){ if(_AVLparent[rt]!=-1){ if(rt == _AVLleftChild[_AVLparent[rt]]) _AVLleftChild[_AVLparent[rt]] = pivot; else _AVLrightChild[_AVLparent[rt]] = pivot;} _AVLparent[pivot] = _AVLparent[rt]; _AVLparent[rt] = pivot; _AVLrightChild[rt] = _AVLleftChild[pivot]; _AVLleftChild[pivot] = rt; if(_AVLrightChild[rt]!=-1) _AVLparent[_AVLrightChild[rt]] = rt; if(_AVLroot == rt) _AVLroot = pivot; _AVLdepth[rt] = 1 + max(_AVLgetDepth(_AVLleftChild[rt]),_AVLgetDepth(_AVLrightChild[rt])); _AVLdepth[pivot] = 1 + max(_AVLgetDepth(_AVLleftChild[pivot]),_AVLgetDepth(_AVLrightChild[pivot])); _AVLdescendants[rt] = 1 + _AVLgetDescendants(_AVLleftChild[rt]) + _AVLgetDescendants(_AVLrightChild[rt]); _AVLdescendants[pivot] = 1 + _AVLgetDescendants(_AVLleftChild[pivot]) + _AVLgetDescendants(_AVLrightChild[pivot]);}
   void _AVLrightRotate(int rt, int pivot){ if(_AVLparent[rt]!=-1){ if(rt == _AVLleftChild[_AVLparent[rt]]) _AVLleftChild[_AVLparent[rt]] = pivot; else _AVLrightChild[_AVLparent[rt]] = pivot;} _AVLparent[pivot] = _AVLparent[rt]; _AVLparent[rt] = pivot; _AVLleftChild[rt] = _AVLrightChild[pivot]; _AVLrightChild[pivot] = rt; if(_AVLleftChild[rt]!=-1) _AVLparent[_AVLleftChild[rt]] = rt; if(_AVLroot == rt) _AVLroot = pivot; _AVLdepth[rt] = 1 + max(_AVLgetDepth(_AVLleftChild[rt]),_AVLgetDepth(_AVLrightChild[rt])); _AVLdepth[pivot] = 1 + max(_AVLgetDepth(_AVLleftChild[pivot]),_AVLgetDepth(_AVLrightChild[pivot])); _AVLdescendants[rt] = 1 + _AVLgetDescendants(_AVLleftChild[rt]) + _AVLgetDescendants(_AVLrightChild[rt]); _AVLdescendants[pivot] = 1 + _AVLgetDescendants(_AVLleftChild[pivot]) + _AVLgetDescendants(_AVLrightChild[pivot]);}
   void _AVLbalance(int cur){ if(cur == -1) return;  int balance = _AVLgetBalance(cur); if(abs(balance) > 1){ if(balance < 0){ if(_AVLgetBalance(_AVLleftChild[cur]) > 0) _AVLleftRotate(_AVLleftChild[cur],_AVLrightChild[_AVLleftChild[cur]]); _AVLrightRotate(cur,_AVLleftChild[cur]);} else{         if(_AVLgetBalance(_AVLrightChild[cur]) < 0) _AVLrightRotate(_AVLrightChild[cur],_AVLleftChild[_AVLrightChild[cur]]); _AVLleftRotate(cur,_AVLrightChild[cur]);}}_AVLdepth[cur] = max(_AVLgetDepth(_AVLrightChild[cur]),_AVLgetDepth(_AVLleftChild[cur])) + 1; _AVLdescendants[cur] = 1 + _AVLgetDescendants(_AVLrightChild[cur]) + _AVLgetDescendants(_AVLleftChild[cur]); _AVLbalance(_AVLparent[cur]);}
   void _AVLinsert(int last, int cur, int index, T data){ if(cur == -1){ _AVLparent[index] = last; _AVLdata[index]= data; _AVLrightChild[index] = _AVLleftChild[index] = -1; _AVLdepth[index] = 0; _AVLdescendants[index] = 1; _AVLtotal++; if(last == -1) _AVLroot = index; else if(_AVLdata[last] < data || _AVLdata[last] == data && last < index) _AVLrightChild[last] = index; else _AVLleftChild[last] = index; if(_AVLbalanced) _AVLbalance(index);} else if(_AVLdata[cur] < data || _AVLdata[cur]==data && cur < index) _AVLinsert(cur,_AVLrightChild[cur],index,data); else _AVLinsert(cur,_AVLleftChild[cur],index,data); _AVLdepth[cur] = max(_AVLgetDepth(_AVLrightChild[cur]),_AVLgetDepth(_AVLleftChild[cur])) + 1; _AVLdescendants[cur] = 1 + _AVLgetDescendants(_AVLrightChild[cur]) + _AVLgetDescendants(_AVLleftChild[cur]);}
   void _AVLremove(int cur, int index, T value){ if(cur==-1) return; else if(cur == index || index==-1 && _AVLdata[cur]==value){ if(_AVLdescendants[cur]>1){ int replace = (_AVLleftChild[cur]!=-1)?_AVLrightMost(_AVLleftChild[cur]):_AVLleftMost(_AVLrightChild[cur]); int par = _AVLparent[replace]; if(replace == _AVLleftChild[par]) _AVLleftChild[par] = _AVLrightChild[replace]; else _AVLrightChild[par] = _AVLleftChild[replace]; _AVLdepth[par] = max(_AVLgetDepth(_AVLrightChild[par]),_AVLgetDepth(_AVLleftChild[par])) + 1; _AVLdescendants[par] = 1 + _AVLgetDescendants(_AVLrightChild[par]) + _AVLgetDescendants(_AVLleftChild[par]);  _AVLparent[replace] = _AVLparent[cur]; if(_AVLparent[replace]!=-1){ if(_AVLleftChild[_AVLparent[replace]] == cur) _AVLleftChild[_AVLparent[replace]] = replace; else _AVLrightChild[_AVLparent[replace]] = replace;} _AVLleftChild[replace] = _AVLleftChild[cur]; _AVLrightChild[replace] = _AVLrightChild[cur]; _AVLparent[cur] = -2;  if(_AVLleftChild[replace]!=-1) _AVLparent[_AVLleftChild[replace]] = replace; if(_AVLrightChild[replace]!=-1) _AVLparent[_AVLrightChild[replace]] = replace;_AVLdepth[replace] = max(_AVLgetDepth(_AVLrightChild[replace]),_AVLgetDepth(_AVLleftChild[replace])) + 1; _AVLdescendants[replace] = 1 + _AVLgetDescendants(_AVLrightChild[replace]) + _AVLgetDescendants(_AVLleftChild[replace]); if(cur == _AVLroot) _AVLroot = replace;if(_AVLbalanced) if(par!=cur) _AVLbalance(par); else _AVLbalance(replace);  return;} else if(_AVLroot == cur) _AVLroot = -1, _AVLparent[cur] = -2; else{ if(_AVLleftChild[_AVLparent[cur]] == cur) _AVLleftChild[_AVLparent[cur]] = -1; else _AVLrightChild[_AVLparent[cur]] = -1; if(_AVLbalanced) _AVLbalance(_AVLparent[cur]); _AVLparent[cur] = -2; return; }}else if(_AVLdata[cur] < value || index!=-1 && _AVLdata[cur] == value && cur < index) _AVLremove(_AVLrightChild[cur],index, value);else _AVLremove(_AVLleftChild[cur],index, value);_AVLdepth[cur] = max(_AVLgetDepth(_AVLrightChild[cur]),_AVLgetDepth(_AVLleftChild[cur])) + 1; _AVLdescendants[cur] = 1 + _AVLgetDescendants(_AVLrightChild[cur]) + _AVLgetDescendants(_AVLleftChild[cur]); }
public:
   AVLTree(bool bal=true) : _AVLbalanced(bal) { init();}
   void init(){ _AVLroot = -1; _AVLtotal = 0; MEMSET(_AVLleftChild,-1); MEMSET(_AVLrightChild,-1); MEMSET(_AVLparent,-1); MEMSET(_AVLdepth,0); MEMSET(_AVLdescendants,0);}
   void insertIndex(int index, T value){ _AVLinsert(-1,_AVLroot,index,value);}
   void insert(T value){ _AVLinsert(-1,_AVLroot,_AVLtotal,value);}
   void removeIndex(int index) { _AVLremove(_AVLroot, index, _AVLdata[index]); }
   void remove(T value){ _AVLremove(_AVLroot,-1,value); }
};
// END CUT - AVL Trees

// BEGIN CUT - BFS - O(states)
#define _BFS_ROWS 1
#define _BFS_COLS 1
int bfsmatrix[_BFS_ROWS][_BFS_COLS];
bool _BFSvalidMove(int fR, int fC, int dR, int dC){
   cout << "NEED TO PUT SOME MORE CODE HERE" << fR << " " << fC << " " << dR << " " << dC << endl;
   return true;
}
int bfs(int r, int c, int numRows, int numCols, int targetR=INF, int targetC=INF){
       memset(bfsmatrix,-1,sizeof(bfsmatrix));
       queue<int>left; left.push(r); left.push(c); bfsmatrix[r][c] = 0; if(targetR==0&&targetC==0) return 0;
       while(!left.empty()){
         int tR, tC, d, nR, nC; tR =left.front(); left.pop(); tC = left.front(); left.pop(); d = bfsmatrix[tR][tC];
         FOR(i,0,4){
             nR = tR + dr4[i], nC = tC + dc4[i]; if(nR<0||nC<0||nR>=numRows||nC>=numCols||bfsmatrix[nR][nC]!=-1||!_BFSvalidMove(tR,tC,nR,nC)) continue;
             bfsmatrix[nR][nC]=(d+1); left.push(nR); left.push(nC); if(nR==targetR&&nC==targetC) return d+1;
         }
      }
      return -1;
}
// END CUT - BFS

//BEGIN CUT - Binary Indexed Tree - O(log(V))
#define _BIT_SIZE 1
long long _BIT_freq[_BIT_SIZE];
void bit_init(){ MEMSET(_BIT_freq,0);}
long long bit_getCumulative(int pos){ pos++; assert(pos>=0 && pos<_BIT_SIZE); long long ret = 0; while(pos>0){ ret += _BIT_freq[pos]; pos -= (pos & -pos);}return ret;}
long long bit_getSingular(int pos){ pos++; assert(pos>=0 && pos<_BIT_SIZE); long long ret = _BIT_freq[pos]; if(pos > 0){ int z = pos - (pos & -pos); pos--; while(pos!=z){ ret -= _BIT_freq[pos]; pos -= (pos & -pos);}}return ret;}
bool bit_update(int pos, long long delta){ pos++; if(pos<1 || pos>=_BIT_SIZE) return false; while(pos < _BIT_SIZE){ _BIT_freq[pos] += delta; pos += (pos&-pos);}return true;}
        /* find smallest x such that c[x] >= cumFre */
long long bit_find(int cumFre){ long long pos = 0, bitMask=0; FOR(i,0,64) if(SHIFT(i)>=_BIT_SIZE) break; else if(SHIFT(i) & (_BIT_SIZE-1)) bitMask = SHIFT(i); int ret = _BIT_SIZE;while ((bitMask != 0) && (pos < _BIT_SIZE)){  int mid = pos + bitMask; if(mid < _BIT_SIZE){  if (cumFre > _BIT_freq[mid]){ pos = mid; cumFre -= _BIT_freq[mid];}  else ret = min(ret,mid);} bitMask >>= 1;}if(ret == _BIT_SIZE) return -1;return ret-1;}
// END CUT - Binay Indexed Tree

// BEGIN CUT - Binary Search - O(logN) - find the point where it goes from untrue to true... always false at low
long long  binarySearch(long long  low, long long high, bool (* _target) (long long t1)){ while(low < high){ long long mid = low + (high - low) / 2; if(_target(mid)) high = mid; else low = mid+1;} return low;}
long double binarySearch(long double low, long double high, bool (* _target) (long double t1)){ while(low < high-eps){ long double mid = low + (high - low) / 2.0; if(_target(mid)) high = mid; else low = mid; }return low;}
// END CUT - Binary Search

//BEGIN CUT - BitStuff
int numBits(unsigned long long v) {return __builtin_popcount(v>>32) + __builtin_popcount(v & ((SHIFT(32)-1)));}
int highestBit(unsigned long long v) { return (v==0)?-1:(((v>>32)!=0)?63-__builtin_clz(v>>32):31-__builtin_clz(v));}
int lowestBit(unsigned long long v) { return (v==0)?-1:((((v>>32)<<32)==v)?32 + __builtin_ctz(v>>32):__builtin_ctz(v));}
inline void flip(long long &m, int v) { m ^= SHIFT(v);}
inline void flip(int &m, int v) { assert(v<32); m ^= SHIFT(v);}
bitset<8> toBinary(char c) { return bitset<8>(c);}
bitset<32> toBinary(int n) { return bitset<32>(n);}
bitset<64> toBinary(long long n){ return bitset<64>(bitset<64>(n) | (bitset<64>(n>>32)<<32));}
//END CUT - BitStuff

//BEGIN CUT - Choose Function - O(min(B,T-B)^2)
long long choose(long long T, long long B){ long long ret = 1;  vector<long long> top, bottom; if(T<B || B<0) return -1; B = min(B,T-B); FOR(i,0,B){ top.push_back(T-i); bottom.push_back(i+1); } FOR(i,0,top.size()) FOR(j,0,bottom.size()){ if(top[i]==1) break; long long g = gcd(top[i],bottom[j]); top[i]/=g; bottom[j]/=g; if(bottom[j]==1){ swap(bottom[bottom.size()-1],bottom[j--]); bottom.pop_back();} } FOR(i,0,top.size()) ret*=top[i]; return ret;}
// END CUT - Choose Function

// BEGIN CUT - Concatenate - O(N)
string concatenate(vector<string> &str){ string s; FOR(i,0,str.size()) s += str[i]; return s;}
// END CUT - Concatenate

//BEGIN CUT - Disjoint Set Forest - O(m*a(n))		NOTE: First Convert to indeces on the range (0.._MAX_DJSFSIZE]
#define _MAX_DJSFSIZE 1
int _djsParent[_MAX_DJSFSIZE], _djsRank[_MAX_DJSFSIZE];
void djs_init(){ MEMSET(_djsParent,-1); MEMSET(_djsRank,-1);}
bool djs_makeset(int pos){ if(pos < 0 || pos>=_MAX_DJSFSIZE || _djsParent[pos]!=-1) return false;_djsParent[pos]=pos; _djsRank[pos]=0; return true;}
int djs_findset(int pos){ if(_djsParent[pos]!=pos){ _djsParent[pos] = djs_findset(_djsParent[pos]);} return _djsParent[pos];}
bool djs_union(int posA, int posB){ int pA = djs_findset(posA), pB = djs_findset(posB); if(pA==pB) return false; if(_djsRank[pA]>_djsRank[pB]) _djsParent[pB] = pA; else if(_djsRank[pB]>_djsRank[pA]) _djsParent[pA]=pB; else _djsParent[pA]=pB, _djsRank[pA]++; return true;}
//END CUT - Disjoing Set Forest

// BEGIN CUT - Fast Fourier Transform - O(n lg n)
void polyToDFT(vector<complex<long double> >&A, bool inverse){  if(A.size() == 1) return; complex<long double> wn(cos(2*PI/A.size()),sin(2*PI/A.size())), w(1); if(inverse) wn.imag() = -wn.imag(); vector<complex<long double> > A0, A1; FOR(i,0,A.size()) if(i&1) A1.push_back(A[i]); else A0.push_back(A[i]); polyToDFT(A0,inverse), polyToDFT(A1,inverse); FOR(k,0,A.size()/2){ A[k] = A0[k] + w*A1[k]; A[k+A.size()/2] = A0[k] - w*A1[k]; if(inverse) A[k]/=2, A[k+A.size()/2]/=2; w = w * wn;}}
vector<complex<long double> > fft(vector<complex<long double> > &A, vector<complex<long double> > &B){ while(A.size() < B.size()) A.push_back(0); while(B.size() < A.size()) B.push_back(0);  while(A.size() & (A.size()-1)) A.push_back(0), B.push_back(0); FOR(i,0,A.size()) B.push_back(0); while(A.size() < B.size()) A.push_back(0); polyToDFT(A,false), polyToDFT(B,false); vector<complex<long double> > Cy; FOR(i,0,A.size()) Cy.push_back(A[i]*B[i]); polyToDFT(Cy,true); return Cy;}
// END CUT - Fast Fourier Transform

// BEGIN CUT - Flood Fill - O(elements)
#define _FLD_ROWS 1
#define _FLD_COLS 1
bool floodmatrix[_FLD_ROWS][_FLD_COLS];
void initFlood(){ MEMSET(floodmatrix,false);}
int flood(int r, int c, int nR, int nC, bool (*invalid)(int,int)){ if(r<0 || c<0 || r>=nR || c>=nC || floodmatrix[r][c] || invalid(r,c)) return 0; floodmatrix[r][c] = true; int ret =1;      FOR(i,0,4) ret += flood(r+dr4[i],c+dc4[i],nR,nC,invalid); return ret;}
// END CUT - Flood Fill

//BEGIN CUT - Fraction structure
struct frac{
public:   frac(long long A=0, long long B=1):num(A), denom(B){} frac operator=(const frac &rhs) { this->num = rhs.num; this->denom = rhs.denom; return reduce();}
   frac operator*(const frac & rhs){ if(num==0||rhs.num==0) return frac(); long long g1=gcd(abs(num),rhs.denom), g2=gcd(denom,abs(rhs.num)); return frac((num/g1)*(rhs.num/g2),(denom/g2)*(rhs.denom/g1));} frac operator*=(const frac &rhs){return (*this)=operator*(rhs);}
   frac operator+(const frac &rhs){long long _lcm = lcm(denom,rhs.denom); return frac(num*(_lcm/denom) + rhs.num*(_lcm/rhs.denom),_lcm).reduce();} frac operator+=(const frac &rhs){return (*this)=operator+(rhs);}
   frac operator-(const frac &rhs){ return (*this)+frac(-rhs.num,rhs.denom);} frac operator-=(const frac &rhs){return (*this)=operator-(rhs);}
   frac operator/(const frac &rhs){ assert(rhs.num!=0); return (*this)*frac(rhs.denom,rhs.num);} frac operator/=(const frac &rhs){return (*this)=operator/(rhs);}
   bool operator==(frac rhs){ rhs.reduce(); return num==rhs.num && denom==rhs.denom;} bool operator!=(const frac & rhs) { return !((*this)==rhs);}
   bool operator<(const frac &rhs){ long long _lcm = lcm(denom,rhs.denom); return num * (_lcm/denom) < rhs.num * (_lcm/rhs.denom);} bool operator<=(const frac &rhs) { return (*this)==rhs || (*this) < rhs;}
   bool operator>(const frac &rhs){ return !((*this) <= rhs);} bool operator>=(const frac &rhs){ return !((*this)<rhs);}
   frac reduce() { long long g = gcd(num,denom); if(g>1){num/=g,denom/=g;} return (*this);} string toString(){stringstream ss; ss << num << "/" << denom; return ss.str();}
private:    long long num, denom;
};
//END CUT - fraction structure

// BEGIN CUT - Geometry Library = O(dimensions)
template <class T>
T distanceSquared(const vector<T> &p1, const vector<T> &p2){ T ret = 0; FOR(i,0,p1.size()) ret += SQ(p2[i] - p1[i]); return ret;}
template <class T>
inline T distanceSquared(const pair<T,T> p1, const pair<T,T> p2){ return SQ(p2.first - p1.first) + SQ(p2.second - p1.second);}
bool line_intersection2D(const vector<long double> &p1, const vector<long double> &p2, const vector<long double> &q1, const vector<long double> &q2, vector<long double> &r, bool &colinear){ colinear = false; r = vector<long double>(2,0); long double N1, N2, D, u1, u2; N1 = (q2[0] - q1[0]) * (p1[1] - q1[1]) - (q2[1] - q1[1]) * (p1[0] - q1[0]); N2 = (p2[0] - p1[0]) * (p1[1] - q1[1]) - (p2[1] - p1[1]) * (p1[0] - q1[0]);  D  = (q2[1] - q1[1]) * (p2[0] - p1[0]) - (q2[0] - q1[0]) * (p2[1] - p1[1]); if(fabs(D) > eps) { u1 = N1 / D; u2 = N2/D; if(u1 < -eps || u1 > 1+eps || u2 < -eps || u2 > 1+eps) return false; r[0] = p1[0] + (p2[0] - p1[0]) * u1;  r[1] = p1[1] + (p2[1] - p1[0]) * u1; return true;}  if(fabs(N1) > eps && fabs(N2) > eps) return false; else colinear = true; if(p1[0] >= min(q1[0],q2[0]) && p1[0] <= max(q1[0],q2[0]) && p1[1] >= min(q1[1],q2[1]) && p1[1] <= max(q1[1],q2[1]))  { r = p1; return true;}  if(p2[0] >= min(q1[0],q2[0]) && p2[0] <= max(q1[0],q2[0]) && p2[1] >= min(q1[1],q2[1]) && p2[1] <= max(q1[1],q2[1]))  { r = p2; return true;} return false;}
bool line_intersection2D(const pair<long double, long double> &p1, const pair<long double,long double> &p2, const pair<long double,long double> &q1, const pair<long double,long double> &q2, pair<long double, long double> &r, bool &colinear){ vector<long double> pv1(2), pv2(2), qv1(2), qv2(2), rv; pv1[0] = p1.first; pv1[1] = p1.second; pv2[0] = p2.first; pv2[1] = p2.second; qv1[0] = q1.first; qv1[1] = q1.second; qv2[0] = q2.first; qv2[1] = q2.second; bool ret = line_intersection2D(pv1,pv2,qv1,qv2,rv,colinear); r.first = rv[0]; r.second = rv[1]; return ret;}
template <class T>
T dot_product(const vector<T> &p1, const vector<T> &p2){ T ret = 0; FOR(i,0,p1.size()) ret += p1[i] * p2[i];  return ret; }
template <class T>
vector<T> cross_product(const vector<T> &p1, const vector<T> &p2){ vector<T> ret(3);    ret[0] = p1[1] * p2[2] - p1[2] * p2[1]; ret[1] = p1[2] * p2[0] - p1[0] * p2[2]; ret[2] = p1[0] * p2[1] - p1[1] * p2[0]; return ret; }
template <class T>
vector<T> cross_product(const pair<T,T> &p1, const pair<T,T> &p2){ vector<T> v1(3), v2(3); v1[0] = p1.first; v1[1] = p1.second; v2[0] = p2.first; v2[1] = p2.second; return cross_product(v1,v2);}
// END CUT - Geometry Library


// BEGIN CUT - Graph Manipulation - O(elements)
vector<string> rotateR(const vector<string> &orig){ 
  vector<string> ret(orig[0].length()); FOR(i,0,orig[0].length()) FOR(j,0,orig.size()) ret[i].push_back(orig[orig.size()-j-1][i]); return ret;
}
vector<string> flipH(const vector<string> &orig){ vector<string> ret = orig; FOR(i,0,orig.size()) FOR(j,0,orig[0].length()) ret[i][j] = orig[i][orig.size()-j-1]; return ret;}
// END CUT - Graph Manipulation

int _T;
int N, K;

vector<string> start, end;

void dropdown(vector<string> &mat){
  FOR(i,0,mat[0].length()) for(int k=mat.size()-2;k>=0;k--){
      int j = k;
      while(j < mat.size()-1 && mat[j][i] != '.' && mat[j+1][i] == '.') {swap(mat[j+1][i],mat[j][i]); j++;}
  }
}

int dp[2][50][50][4];

enum {RIGHT, DOWN, DDOWNRIGHT, DDOWNLEFT};
string chs = "RB";
int dr[] = {0, -1, -1, -1};
int dc[] = {1,  0,  1, -1};

int chcount(int ch, int r, int c, int type){
    if(r < 0 || r >= end.size() || c < 0 || c >= end[0].length() || end[r][c] != chs[ch]) return 0;
    int &ret = dp[ch][r][c][type]; if(ret!=-1) return ret; return ret = 1 + chcount(ch,r+dr[type],c+dc[type],type);
}

bool hasK(int ch){
  FOR(i,0,end.size()) FOR(j,0,end[0].length()) if(end[i][j] == chs[ch] && 
	(chcount(ch,i,j,RIGHT) >= K || chcount(ch,i,j,DOWN) >= K || chcount(ch,i,j,DDOWNRIGHT) >= K || chcount(ch,i,j,DDOWNLEFT) >= K)) return true;
  return false;
}

int main(){
  cin >> _T;
  FOR(i,0,_T){
    MEMSET(dp,-1);
    cout << "Case #" << (i+1) << ": ";
    cin >> N >> K;
    start.resize(N); FOR(i,0,N) cin >> start[i];
//    reverse(BEGEND(start));
    // printArray(start);
    end = rotateR(start);
    // printArray(end);
    dropdown(end);

    // printArray(end);

    if(hasK(0)){
	if(hasK(1)) cout << "Both";
	else cout << "Red";
    }
    else if(hasK(1)) cout << "Blue";
    else cout << "Neither";

    cout << endl;
  }
  return 0;
}

