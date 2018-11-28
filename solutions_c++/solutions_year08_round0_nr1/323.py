// GCJ_problem.cpp : Defines the entry point for the console application.
#include "stdafx.h"

#include <stdio.h>
#include <tchar.h>

#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <iomanip>
#include <iostream>
#include <cassert>
#include <fstream>

using namespace std;
typedef long long lint;
typedef vector<int> VI; typedef vector<VI> VVI;
typedef vector<lint> VL; typedef vector<VL> VVL;
typedef vector<double> VD; typedef vector<VD> VVD;
typedef vector<string> VS;
#define SIZE(c) ((int)(c).size())
#define SEQ(c) (c).begin(),(c).end()
#define FOR(i,a,b) for(int _U(b),i=(a);i<_U;++i)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int _U(a),i=(b)-1;i>=_U;--i)
#define FORS(i,c) FOR(i,0,SIZE(c))
#define REPD(i,n) FORD(i,0,n)
template<class T>string tostr(T v){ostringstream o;o<<v;return o.str();}
string tostrdouble(double v) {ostringstream o;o<<fixed<<setprecision(7)<<v; return o.str();}
#define UNIQUE(c) {sort(SEQ(c)); (c).erase(unique(SEQ(c)),(c).end());}
#define MIN(A,B) if ((B)<(A)) (A)=(B)
#define MAX(A,B) if ((B)>(A)) (A)=(B)
const int inf = 1000100100;
///////////////////////////////////////////////////////////////////////////////////
string caseNo(int i) {return "Case #" + tostr(i) + ":";}

///////////////////////////////////////////////////////////////////////////////////

int mem[128][1024];

int ns, nq;
VS search1, query1;
VI query;

void encode() {
  map<string,int> mp;
  REP (s,ns) mp[search1[s]] = s;
  query.resize(nq);
  REP (q,nq) query[q] = mp[query1[q]];
}

int calc(int s, int q) {
  if (q == -1) return 0;
  int& ret = mem[s][q];
  if (ret != -1) return ret;
  ret = inf;
  if (s == query[q]) return ret;

  REP (s1,ns) {
    int cur = calc(s1,q-1);
    if (s1 != s) ++cur;
    ret = min(ret, cur);
  }
  return ret;
}

int solve() {
  if (nq == 0) return 0;
  encode();
  memset(mem,-1,sizeof(mem));
  int ret = inf;
  REP (s,ns) {
    int cur = calc(s, nq-1);
    ret = min(ret, cur);
  }
  return ret;
}

///////////////////////////////////////////////////////////////////////////////////

void _tmain(int argc, _TCHAR* argv[])
{
  ifstream ifs("data.in");
  ofstream ofs("data.out");
  int ntests;
  ifs >> ntests;
  getline(ifs,string());
  FOR (test,1,ntests+1) {
    ofs << caseNo(test);
    cout << caseNo(test) << endl;

    string s;
    ifs >> ns;
    getline(ifs,s);
    search1.resize(ns);
    REP (i,ns) getline(ifs, search1[i]);

    ifs >> nq;
    getline(ifs,s);
    query1.resize(nq);
    REP (i,nq) getline(ifs, query1[i]);

    int ret = solve();
    ofs << " " << ret;
    ofs << endl;
  }
}
