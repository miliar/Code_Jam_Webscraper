// Marcin Wrochna
// g++ -O2
// IDE: geany
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PI;
#define MP make_pair
#define REP(x,n) for(int x=0; x<(int)(n); ++x)
#define REB(b,x,n) for(int x=b; x<(int)(n); ++x)
#define REPD(x,n) for(int x=(n)-1; x>=0; --x)
#define PB push_back
#define XX first
#define YY second
const int INF = 1000000001;
const double EPS = 10e-9;

struct Tree
{
	double weight;
	string feat;
	Tree *subYes, *subNo;
	Tree (double w, string f) : weight(w), feat(f) {}
};

Tree* getTree()
{
	double weight;
	scanf(" ( %lf ", &weight);
	char c=getc(stdin);
	while(c==' ' || c=='\n') c=getc(stdin);
	if(c==')')  return new Tree(weight,")");
	else ungetc(c, stdin);
	char feat[15];
	scanf("%s", feat);
	Tree* t = new Tree(weight,feat);
	t->subYes = getTree();
	t->subNo = getTree();
	scanf(" )");
	return t;	
}

void destr(Tree* t)
{
	if(t->feat!=")")
	{
		destr(t->subYes);
		destr(t->subNo);
	}
	delete t;
}

void doit() {
	int L;
	scanf("%d\n",&L);
	Tree* root=getTree();
	int A;
	scanf("%d\n",&A);
	REP(a,A)
	{
		
		char buf[15]; int n;
		scanf("%s %d", buf, &n);
		set<string> feats;
		REP(i,n) { scanf("%s",buf); feats.insert(buf); }
		double result = 1;
		Tree* pos = root;
		for(;;)
		{
			result *= pos->weight;
			if(pos->feat==")") break;
			if(feats.find(pos->feat)!=feats.end())
				pos = pos->subYes;
			else
				pos = pos->subNo;
		}
		printf("%.8lf\n", result);
	}
	destr(root);
}

int main()
{
	int NCase;
	scanf("%d\n",&NCase);
	REP(ncase,NCase) {
		printf("Case #%d:\n", ncase+1);
		doit();
	}

	return 0;
}
