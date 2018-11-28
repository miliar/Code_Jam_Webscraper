#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>
#include <string.h>
using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cout<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define i64 long long 
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

vector<int> SplitInt(string &s)
{
	vector<int>Res;int tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}

vector<string> SplitStr(string &s)
{
	vector<string>Res;string tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}
struct Tree
{
	string N;
	double p;
	Tree *L,*R;
	~Tree()
	{
		if (N!="")
		{
			delete L;
			delete R;
		}
	}
	int bTree(string &h,int pos)
	{
//		DEB(h.substr(pos));
		int i=pos;
		string name,rest;
		if (h[i]=='(')
			i++;
		while (h[i]!='('&&h[i]!=')')
		{
			if (isalpha(h[i]))
				name+=h[i];
			else
			{
				
				rest+=h[i];
			}
			i++;
		}
//		DEB(name);
//		DEB(rest);
		if (name=="")
		{
			
			sscanf (rest.c_str(),"%lf",&p);
//			DEB(i);
			return i;
		}
		else
		{
			N=name;
			sscanf (rest.c_str(),"%lf",&p);
			L=new Tree();
			while (h[i]!='(')i++;
			int np=L->bTree(h,i);
			while (h[np]!='(')np++;
			R=new Tree();
			np=R->bTree(h,np);
			return np;
		}
		return 0;
	}
	double evaluate(vector<string> &H)
	{
		if (N=="")
		{
//			DEB(p);
			return p;
		}
		bool ok=false;
		REP(i,SZ(H))
		{
			if (H[i]==N)
			{
				ok=true;
				break;
			}
		}
		if (ok)
		{
//			DEB(p);
			return p*L->evaluate(H);
		}
		else
			return p*R->evaluate(H);
	}
};
char P[12312];
int main ()
{
	int c;
	scanf ("%d",&c);

	FOR(cas,1,c)
	{
		
		int res=0;
		int n;
		
		
		
		scanf ("%d",&n);
		gets(P);
		string ss;
		REP(i,n)
		{
			gets(P);
			//P[strlen (P)-1]='\0';
			ss+=P;
		}
//		DEB(ss);
		Tree *T=new Tree();
		T->bTree(ss,0);
		int q;
		scanf ("%d",&q);
		printf ("Case #%d:\n",cas,res);
		char A[123];;
		REP(i,q)
		{
			int y;
			scanf ("%s%d",A,&y);
			vector<string> An;
			REP(k,y)
			{
				scanf ("%s",P);
				An.PB(P);
			}
			double r=T->evaluate(An);
			printf ("%.6lf\n",r);
		}
		
	}
	return 0;
}

