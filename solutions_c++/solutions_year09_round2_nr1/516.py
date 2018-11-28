// codejam.cpp : Defines the entry point for the console application.
#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>


using namespace std;

typedef long long int64;
#define For(i,n) for (i=0;i<n;i++) 

int i,j,k,n,m,tests,t,kol;

string s;


string itos(int64 a) {stringstream s; s<<a; return s.str();}
int64 stoi(string a) {stringstream s; s<<a; int64 b; s>>b; return b;}
string dtos (double a){char buf[100]; sprintf(buf,"%.6",a); return string(buf);}
double stod(string a) {stringstream s; s<<a; double b; s>>b; return b;}

struct Node{
	double p;
	string feat;
	int l,r,up;
	bool isleft;
};
vector <Node> T;
set<string> Al;

void rec(int start, int finish, int up, bool isleft)
{
	Node N;
	N.isleft = isleft;
	N.l = -1;
	N.r = -1;



	int i1, i2;
	i1=start;
	while (s[i1]!='(') i1++;
	i1++;
	while (s[i1]==' ') i1++;

	i2=finish;
	while(s[i2]!=')') i2--;
	i2--;
	
	string x = "";
	int j1 = i1;
	while (s[j1]!=' ' && s[j1]!=')') {x =  x+s[j1];  j1++;}
	N.p = stod(x);
	
	int j2 = j1;
	while (s[j2]==' ') j2++;

	if (s[j2]!=')'){
		while (s[j2]!=' ' && s[j2]!='('){
			N.feat = N.feat + s[j2];
			j2++;
		}

		N.up = up;
		T.push_back(N);
		int po = T.size()-1;

		int depth = 0,c1;
		bool isleft =true;
		for (int a = j2; a<=i2; a++){
			if (s[a]=='(') 
			{	depth++;
				if (depth==1) c1=a; 
			}
			if (s[a]==')')
			{	depth--;
				if (depth==0) {
					rec(c1,a,po,isleft);
					isleft = !isleft;
				}
			}
		}

	}
	else
	{
		N.up = up;
		T.push_back(N);
	}
}

double glres;

double rec2(int v, double p)
{
	if (glres>-0.5)
		return 0;

	p = p * T[v].p;
	
	if (T[v].l ==-1 && T[v].r ==-1){
			glres=p;
		return p;
	}

	if (Al.find( T[v].feat)!=Al.end() )
		rec2(T[v].l,p);
	else
		rec2(T[v].r,p);
}
int main()
{
	ifstream inp("a-large.in");
	ofstream out("a-large.out");
	
	inp>>tests;
	For(t,tests)
	{
		T.clear();
		kol = 0;
		out<<"Case #"<<t+1<<": "<<endl;
		
		string tmp;
		s = "";
		inp>>n;
		For(i,n){
			getline(inp,tmp);
			if (tmp=="") getline(inp,tmp); 
			s = s + tmp;
		}

		rec(0,s.length()-1,-1,false);

		//==build tree
		For(i,T.size())
			if (i>0){
			if (T[i].isleft)
				T[T[i].up].l = i;
			else
			T[T[i].up].r = i;
			}
		//==
		inp>>n;
		
		string tt;
		For(i,n)
		{
			Al.clear();
			inp>>tt>>m;
			For(j,m)
			{
				inp>>tt;
				Al.insert(tt);
			}
			
			glres = -1;
			double res = rec2(0,1.0);
			out.precision(8);
			out<<glres<<endl;
		}
			
		
	}

	return 0;
}

