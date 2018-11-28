#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

#define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(
#define FORD(i, a, b) for(int i=(a); i<(b); i++)
#define FORS(i, a) for(int i=(0); i<SIZE(a); i++)
typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64
#define two(X) (1<<(X))//NOTES:two(
#define twoL(X) (((int64)(1))<<(X))//NOTES:twoL(
#define contain(S,X) (((S)&two(X))!=0)//NOTES:contain(
#define containL(S,X) (((S)&twoL(X))!=0)//NOTES:containL(
const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-11;//NOTES:eps
template<class T> inline T sqr(T x){return x*x;}//NOTES:sqr
typedef pair<int,int> ipair;//NOTES:ipair
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//NOTES:lowbit(
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}//NOTES:countbit(

int gnCase;
char gStr[1024];
ifstream gIn; ofstream gOut;
string ReadToEndLine() { string sLine; getline(gIn, sLine); return sLine; }
// sprintf_s(gStr, "%d", );

void mark(vector<vector<bool> > &V, int s, int f, int c1, int c2)
{
  int m = f-s;
}

void run()
{
  int P, N;
  gIn >> P;
  N = 1 << P;
  vector<int> M(N);
  FORD(i, 0, N)
    gIn >> M[i];

  int MM = (1<<P)-1;
  vector<vector<bool> > V(N, vector<bool>(MM, false));

  int j, m=0;
  for(int i=1; i<=P; i++)
  {
    int inS = 1 << (P-i);
    int inC = N/inS;
    int cC = 0;
    for(int k=0; k<inS; k++)
    {
      gIn >>j;
      for(int kk=cC; kk<cC+inC; kk++)
        V[kk][m] = true;
      m++;
      cC+=inC;
    }
  }

  FORS(com, M)
  {
    int curMiss = 0;
    for(int i=0; curMiss!=M[com] && i<SIZE(V[com]); i++)
    {
      if(V[com][i])
      {
        V[com][i] = false;
        curMiss++;
      }
    }
  }

  int count = 0;
  FORD(mat, 0, MM)
  {
    bool need=false;
    FORD(com, 0, N)
    {
      if(V[com][mat])
      {
        need = true;
        break;
      }
    }
    if(need)
      count++;
  }




  gOut << "Case #" << gnCase << ": ";
  gOut << count;
  gOut << endl;
}

void main(int argc, char *argv[])
{
  string sFile(argv[1]);
  gIn.open(sFile.c_str());
  sFile.resize(SIZE(sFile)-2);
  sFile += "out";
  gOut.open(sFile.c_str());

  int CASES;
  gIn >> CASES;
  ReadToEndLine();
  FORD(i, 0, CASES)
  {
    gnCase=i+1;
    run();
  }

  if(gOut.tellp() < 1000)
  {
    gOut.close();
    ifstream fOut(sFile.c_str());
    cout << fOut.rdbuf();
  }
  cout << "Ok" << endl;
  getchar();
}
