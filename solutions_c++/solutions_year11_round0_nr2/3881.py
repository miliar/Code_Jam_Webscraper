#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <list>
#include <map>
#include <queue>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef queue<int> QI;
typedef vector<char> VC;

struct block{
	char a;
	char b;
	char c;
};

void main()
{
	int t,c,d,n, jtemp, ctemp;
	int adda=-1, addb=-1, suba=-1, subb=-1;
	int addj;
	string str;
	block add,sub;
	ifstream in;
	in.open("asd7.txt");
	ofstream out;
	out.open("out2.txt");
		
	in>>t;
	REP(i,t)
	{
		in>>d;
		add.a = NULL; add.b = NULL; add.c = NULL; 
		REP(j,d)
		{
			in>>add.a;
			in>>add.b;
			in>>add.c;
		}
		in>>n;
		sub.a = NULL; sub.b = NULL; 
		REP(j,n)
		{
			in>>sub.a;
			in>>sub.b;
		}

		
		in>>c;
		ctemp = c;
		in>>str;

		for(int j=0;j<c;j++)
		{
			if(str[j] == add.a && !(add.a==add.b && adda!=-1)) 
				{adda=j;}
			else if( str[j] == add.b) 
				{addb=j;}

			jtemp=j;

			if(adda != -1 && addb != -1)
			{
				if(suba == adda || suba == addb)
					suba =-1;
				if(subb == adda || subb == addb)
					subb =-1;
				str.erase(min(adda,addb),1);
				str[min(adda,addb)]= add.c ;
				j=min(adda,addb);
				c--;
				adda=-1; addb=-1;
			}

			if(j!=c)
			{
				if(str[j] == sub.a && suba==-1)
					suba =j;
				else if(str[j] == sub.b && subb==-1)
					subb=j;
			}
			

			if(jtemp-adda >0) 
				adda = -1;
			if (jtemp- addb>0)
				addb = -1;

			if(suba != -1 && subb != -1)
			{
				//int dist = abs(subb-suba);
				str.erase(0,j+1);	
				suba=-1; subb=-1;
				c-=j+1; j=-1; 
				adda = -1; addb = -1;
			}			
		}
		out<<"Case #"<<i+1<<": [";
		REP(k,str.length()-1)
			out<<str[k]<<", ";
		if(!str.empty())
			out<<str[str.length()-1];
		out<<"]"<<endl;
		adda =-1; addb =-1; suba=-1; subb=-1;
		
	}
}