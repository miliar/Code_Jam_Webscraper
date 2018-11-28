// Compiler : MS VC++ 8.0
// input  file : d.in
// output file : d.out

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
#include <ctime>
#include <conio.h>
#include <list>

using namespace std;
typedef long long lint;
typedef vector<int> VI; typedef vector<VI> VVI;
typedef vector<lint> VL; typedef vector<VL> VVL;
typedef vector<double> VD; typedef vector<VD> VVD;
typedef vector<char> VC; typedef vector<VC> VVC;
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
typedef pair<int,int> PII;
#define MIN(A,B) if ((B)<(A)) (A)=(B)
#define MAX(A,B) if ((B)>(A)) (A)=(B)
const int inf = 1000100100; // (inf + inf) fits into "int" type.
const double Pi = acos(-1.);
///////////////////////////////////////////////////////////////////////////////////
template <class T>
vector<T> splitString(string s, string sep = " ") {
  vector<T> ret;
  int pos = -1, posPrev = -2;
  do {
    posPrev = pos;
    pos = (int)s.find_first_of(sep, posPrev+1);
    if (pos == -1) pos = (int)s.size();
    if (pos-posPrev > 1) {
      istringstream is(s.substr(posPrev+1,pos-posPrev-1));
      T v; is >> v; ret.push_back(v);
    }
  } while (posPrev < (int)s.size());
  return ret;
}
///////////////////////////////////////////////////////////////////////////////////
string caseNo(int i) {return "Case #" + tostr(i) + ":";}

///////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////

string inputTree;
VS inputAnimals; 

VS treeTokens;
vector<VS> animalTokens;

int na;

typedef map<string,int> FeatureMap;
FeatureMap featureMap;

void addFeatureToFeatureMap(const string& s) {
  if (featureMap.find(s) != featureMap.end()) return;
  int idx = SIZE(featureMap);
  featureMap[s] = idx;
}

bool isNumber(const string& s) {
  assert(SIZE(s) > 0);
  assert(s[0] != '.');
  bool ret = '0' <= s[0] && s[0] <= '9';
  return ret;
}

double strToNum(const string& s) {
  double ret = splitString<double>(s)[0];
  return ret;
}

void fillFeatureMap() {
  treeTokens = splitString<string>(inputTree);
  animalTokens.resize(na);
  REP (a,na) {
    animalTokens[a] = splitString<string>(inputAnimals[a]);
  }

  featureMap.clear();

  FORS (i,treeTokens) {
    string token = treeTokens[i];
    if (token == ")" || token == "(" || isNumber(token))
      continue;
    addFeatureToFeatureMap(token);
  }

  FORS (a,animalTokens) {
    FOR (f, 2, SIZE(animalTokens[a]))
    addFeatureToFeatureMap(animalTokens[a][f]);
  }
}

struct Node {
  double weight;
  int feature;
  int child0, child1;
   
  Node(double _w = -1., int _f = -1, int _c0 = -1, int _c1 = -1) : weight(_w), feature(_f), child0(_c0), child1(_c1) {}
};

vector<Node> tree;

int treeTokenIndex;

const string& getTreeToken() {
  const string& ret = treeTokens[treeTokenIndex++];
  return ret;
}

void ungetTreeToken() {
  treeTokenIndex--;
}

void readNode(int nodeIndex) {
  Node node;
  string s = getTreeToken();
  assert(s == "(");
  node.weight = strToNum(getTreeToken());
  s = getTreeToken();
  if (s != ")") {
    assert(featureMap.count(s) != 0);
    node.feature = featureMap[s];

    tree.push_back(Node());
    node.child0 = SIZE(tree)-1;
    readNode(node.child0);

    tree.push_back(Node());
    node.child1 = SIZE(tree)-1;
    readNode(node.child1);

    s = getTreeToken();
    assert(s == ")");
  }

  tree[nodeIndex] = node;
}

void buildTree() {
  treeTokenIndex = 0;

  tree.clear();
  tree.push_back(Node());

  readNode(0);
}

VD res;

double animalRes(const VI& features, int i) {
  double ret = tree[i].weight;
  if (tree[i].feature == -1)
    return ret;
  double mul = -1;
  if (binary_search(SEQ(features),tree[i].feature))
    mul = animalRes(features, tree[i].child0);
  else
    mul = animalRes(features, tree[i].child1);

  ret *= mul;

  return ret;
}


void calc() {
  res.resize(na);

  REP (a,na) {
    VI features;
    FOR (f,2,SIZE(animalTokens[a])) {
      assert(strToNum(animalTokens[a][1]) == SIZE(animalTokens[a])-2);
      string& token = animalTokens[a][f];
      int idx = featureMap[token];
      features.push_back(idx);
    }
    sort(SEQ(features));
    res[a] = animalRes(features, 0);
  }

}

void solve() {
  fillFeatureMap();
  
  buildTree();

  calc();
}


void main()
{
  clock_t clock_global = clock();
  ifstream ifs("d.in");
  ofstream ofs("d.out"); ofs << setprecision(9);
  int ntests;
  ifs >> ntests;
  getline(ifs,string());

  string s;

  FOR (test,1,ntests+1) {
    clock_t clock_test = clock();
    ofs << caseNo(test);
    cout << caseNo(test) << " ... ";
    //-------------------------------------------------------------
    int nt;
    ifs >> nt; getline(ifs, string());
    inputTree.clear();
    REP (i,nt) {
      getline(ifs,s);
      inputTree += " " + s;
    }
    s.clear();
    FORS (i,inputTree) {
      if (inputTree[i] == ')' || inputTree[i] == '(')
        s += string(" ") + inputTree[i] + " ";
      else
        s += inputTree[i];
    }
    inputTree = s;

    ifs >> na; getline(ifs, string());
    inputAnimals.resize(na);
    REP (i,na)
      getline(ifs,inputAnimals[i]);

    solve();

    FORS (i,res)
      ofs << endl << res[i];
    //-------------------------------------------------------------
    ofs << endl;
    cout << double(clock() - clock_test) / CLOCKS_PER_SEC << " sec.\n";
  }
  ifs.close();
  ofs.close();
  cout << "EXECTION FINISHED IN " << double(clock() - clock_global) / CLOCKS_PER_SEC << " sec.\n";
  _getch();
}
