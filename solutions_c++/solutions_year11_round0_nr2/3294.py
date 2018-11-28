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
#include <hash_map>

using namespace std;
using namespace stdext;

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

typedef hash_map<string, char> Combine;
typedef hash_map<char, vector<char> > Opposite;

void run()
{
  Combine Comb;
  Opposite Op;

  int C, D, N;
  gIn >> C;
  FORD(i, 0, C)
  {
    string sComb, sFirst;
    gIn >> sComb;
    copy(sComb.begin(), sComb.begin()+2, inserter(sFirst, sFirst.begin()));
    sort(sFirst.begin(), sFirst.end());
    Comb.insert(MP(sFirst, sComb[2]));
  }
  gIn >> D;
  FORD(i, 0, D)
  {
    string sOp;
    gIn >> sOp;
    Op[sOp[0]].push_back(sOp[1]);
    Op[sOp[1]].push_back(sOp[0]);
  }
  gIn >> N;
  string sInput;
  gIn >> sInput;

  vector<char> Res;
  FORS(i, sInput)
  {
    char ch = sInput[i];
    if(Res.empty())
    {
      Res.push_back(ch);
      continue;
    }

    string sComb(1, ch);
    sComb+=Res.back();
    sort(sComb.begin(), sComb.end());
    Combine::iterator pIter = Comb.find(sComb);
    if(pIter != Comb.end())
    {
      Res.pop_back();
      Res.push_back(pIter->second);
      continue;
    }

    Opposite::iterator pOp = Op.find(ch);
    if(pOp != Op.end() && find_first_of(Res.begin(), Res.end(), pOp->second.begin(), pOp->second.end()) != Res.end())
    {
      Res.clear();
      continue;
    }

    Res.push_back(ch);
  }

  gOut << "Case #" << gnCase << ": ";
  gOut << '[';
  FORS(i, Res)
  {
    if(i!=0)
      gOut << ", ";
    gOut << Res[i];
  }
  gOut << ']';
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
