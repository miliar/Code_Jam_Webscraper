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

string s;

char ch[1100000];
int main()
{
	freopen("in.txt","r",stdin);	
	freopen("out.txt","w",stdout);	
	
	int TTT; scanf("%d",&TTT);
	FOR(Case,1,TTT+1)
	{
		scanf("%s",ch); s=string(ch);

		int p=s.sz-2;
		while(p>=0) { if (s[p+1]<=s[p]) --p; else break; }
		printf("Case #%d: ",Case);
		if (p<0)
		{
			s+="0";
			sort(ALL(s)); 
			int mn=-1;
			FOR(i,0,s.sz) if (s[i]!='0') { mn=s[i]-'0'; s.erase(i,1);  break; }
			string t;
			t+=(char)('0'+mn);
			t+=s;
			printf("%s",t.c_str());
		}
		else
		{
			string h=s.substr(p+1);
			sort(ALL(h));
			int mn=0;
			FOR(i,0,h.sz) if (s[p]<h[i]) { mn=h[i]-'0'; h.erase(i,1); break; }
			h+=s[p];
			s[p]='0'+mn;
			s=s.substr(0,p+1);
			sort(ALL(h));
			s+=h;
			printf("%s",s.c_str());
		}

		printf("\n");
	}
	
	return 0;
}
