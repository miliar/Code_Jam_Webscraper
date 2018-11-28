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

int nRides, nSize, nGroups;
struct Group
{
  int nSize;
  int nNext;
  int nMoney;
};
vector<Group> G;

int GetGroupIndex(int nIndex)
{
  return nIndex % nGroups;
}

Group& GetGroup(int nIndex)
{
  return G[GetGroupIndex(nIndex)];
}

void CalcInit(int nIndex)
{
  int nMoney=0;
  int nNext;
  for(nNext=0; nNext<nGroups; nNext++)
  {
    if(nMoney+GetGroup(nNext+nIndex).nSize > nSize)
      break;
    nMoney+=GetGroup(nNext+nIndex).nSize;
  }

  GetGroup(nIndex).nMoney = nMoney;
  GetGroup(nIndex).nNext = GetGroupIndex(nIndex+nNext);
}

void run()
{
  gIn >> nRides >> nSize >> nGroups;
  G.clear();
  G.resize(nGroups);
  FORS(i, G)
    gIn >> G[i].nSize;

  // Calculate next & money
  FORS(i, G)
    CalcInit(i);

  // Rides
  int nCurGroup = 0;
  int64 nMoney = 0;
  FORD(i, 0, nRides)
  {
    nMoney+=G[nCurGroup].nMoney;
    nCurGroup = G[nCurGroup].nNext;
  }

  gOut << "Case #" << gnCase << ": ";
  gOut << nMoney;
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
