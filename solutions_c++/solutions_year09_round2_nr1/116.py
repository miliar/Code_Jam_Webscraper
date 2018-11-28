#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <string>
#include <ctime>
#include <queue>
#include <memory.h>
#include <cstdio>
using namespace std;

typedef unsigned int uint;
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define sz size()
#define pb push_back
#define mp make_pair
#define ALL(a) (a).begin(), (a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b);i>=_b;--i)
#define ABS(a) ((a)<0?-(a):(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define HAS(v,k) ((v).find(k)!=(v).end())
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define sqr(a) ((a)*(a))
#pragma comment(linker,"/STACK:64000000")

int gcd(int a, int b) { return (!a)?b:gcd(b%a,a); }
int lcm(int a, int b) { return a/gcd(a,b)*b; }
const LL MOD=1LL;
const double eps  = 1e-12;
template<class T,class Q>
void convert(T src,Q &dst) 
{ostringstream oss; oss << src; istringstream iss(oss.str()); iss>>dst;}

#define PREV(a) ((a)&(a-1))
#define NEXT(a) ((a<<1)-PREV(a))
typedef int matrix[128][128];

map<string,int> ID;
int getid(string &s) { if (!HAS(ID,s)) { int t=ID.sz; ID[s]=t; } return ID[s]; }

struct node
{
	int id;
	int t,f;
	double p;
	int leaf;
};
node tree[1000000]; 
int size;
void init() {size=1; ID.clear();}

string S;
int pos;
void rec(int p)
{
	double a=0;
	pos++;
	while(isdigit(S[pos]))
	{
		a*=10.0; a+=S[pos]-'0';
		++pos;
	}
	if (S[pos]=='.') 
	{
		pos++;
		int c=0;
		int b=0;
		while(isdigit(S[pos]))
		{
			b*=10; b+=S[pos]-'0';
			++c;
			++pos;
		}
		a+=b/pow(10.0,1.0*c);
	}
	if (S[pos]==')') // leaf
	{
		tree[p].leaf=1;
		tree[p].p=a;
		++pos;
	}
	else
	{
		string h; while(isalpha(S[pos])) h+=S[pos++];
		tree[p].leaf=0;
		tree[p].id=getid(h);
		tree[p].p=a;
		tree[p].t=size++;
		rec(size-1);
		tree[p].f=size++;
		rec(size-1);

		++pos;
	}
}


set<int> ids;
double go()
{
	int p=0;
	double r=1.0;
	while(!tree[p].leaf)
	{
		r*=tree[p].p;
		if (HAS(ids,tree[p].id)) p=tree[p].t; else p=tree[p].f;
	}
	r*=tree[p].p;
	return r;
}

char ch[1100000];
int main()
{
	freopen("in.txt","r",stdin);	
	freopen("out.txt","w",stdout);	
	
	int TTT; gets(ch); sscanf(ch,"%d",&TTT);
	FOR(Case,1,TTT+1)
	{
		gets(ch);
		int L; sscanf(ch,"%d",&L);
		string s;
		FOR(i,0,L)
		{
			gets(ch); s+=string(ch);
		}
		string ss(s.sz,'0'); int t=0;
		FOR(i,0,s.sz) if (s[i]!=' ') ss[t++]=s[i];
		ss=ss.substr(0,t);
		S=ss;
		pos=0;
		init();
		rec(0);

		if (size>1000000) { cout << "WRONG\n"; return 0;  }
		
		printf("Case #%d:\n",Case);
		gets(ch); int n; sscanf(ch,"%d",&n);
		FOR(i,0,n)
		{
			string s; gets(ch); string tmp(ch);
			istringstream iss(tmp);
			iss >> s;
			int k=0;
			iss >> k;
			ids.clear();
			FOR(i,0,k) { string h; iss >> h; ids.insert(getid(h)); }
			printf("%.7lf\n",go());
		}
	}
	
	return 0;
}
