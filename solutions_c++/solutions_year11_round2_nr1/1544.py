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

struct WP
{
  WP() : W(0), G(0) {}
  WP(int w, int g) : W(w), G(g) {}
  int W, G;
};

struct Team
{
  vector<WP> m_WPs;
  WP m_WP;
  double OWP;
  double OOWP;
};

void run()
{
  int N;
  gIn >> N;
  ReadToEndLine();

  vector<vector<int> > M(N, vector<int>(N, 0));
  FORD(i, 0, N)
  {
    string str = ReadToEndLine();
    FORS(j, str)
    {
      char ch = str[j];
      if(ch == '1')
        M[i][j] = 1;
      else if(ch == '0')
        M[i][j] = -1;
    }
  }

  //Calc
  vector<Team> T(N);
  FORS(i, M)
  {
    // Total
    T[i].m_WPs.resize(N);
    FORD(j, 0, N)
    {
      if(M[i][j] == 0)
        continue;
      T[i].m_WP.G++;
      if(M[i][j] == 1)
        T[i].m_WP.W++;
    }

    // Except each
    FORD(j, 0, N)
    {
      if(M[i][j] == 0)
      {
        T[i].m_WPs[j] = T[i].m_WP;
      }
      else if(M[i][j] == 1)
      {
        T[i].m_WPs[j].W = T[i].m_WP.W - 1;
        T[i].m_WPs[j].G = T[i].m_WP.G - 1;
      }
      else
      {
        T[i].m_WPs[j].W = T[i].m_WP.W;
        T[i].m_WPs[j].G = T[i].m_WP.G - 1;
      }
    }
  }

  // OWP
  FORD(i, 0, N)
  {
    double OWPs = 0;
    int nCount=0;
    FORD(j, 0, N)
    {
      if(M[i][j] == 0)
        continue;
      OWPs+= (double)T[j].m_WPs[i].W / (double)T[j].m_WPs[i].G;
      ++nCount;
    }
    T[i].OWP = OWPs / (double)nCount;
  }

  // OOWP
  FORD(i, 0, N)
  {
    double OOWPs = 0;
    int nCount=0;
    FORD(j, 0, N)
    {
      if(M[i][j] == 0)
        continue;
      OOWPs+= T[j].OWP;
      ++nCount;
    }
    T[i].OOWP = OOWPs / (double)nCount;
  }

  gOut << "Case #" << gnCase << ": " << endl;
  FORD(i, 0, N)
  {
    double WP = (double)T[i].m_WP.W / (double)T[i].m_WP.G;
    double rRes = 0.25 * WP + 0.50 * T[i].OWP + 0.25 * T[i].OOWP;
    gOut << setprecision (12) << rRes << endl;
  }
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
