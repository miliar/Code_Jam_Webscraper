#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <utility>
#include <sstream>
#include <cstring>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

#define RP(i,s,e) for(int i=s;i<e;i++) 
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin();i!=(x).end();++i)
#define M make_pair
#define pB push_back
#define _1 first
#define _2 second
#define foreach(t,i) RI(i,t)
#define CLEAR(x,v) memset((x),(v),sizeof((x))
#define PRINT(o,b) RI(i,b) o << *i << (--b.end()==i ? "" : " ");
#define PE(s,e) cout << #s << " : "; for(typeof(s) i=s; i!=e; ++i) cout << (*i) << " "; cout << endl;

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<" "; return o;}

//Cake please.

struct node
{
	double p;
	string label;
	node *st1;
	node *st2;
};

int read_node(node *n, const string &w, int o)
{
	//cout << "S " << o << endl;
	n->st1 = NULL;
	n->st2 = NULL;
	n->label = "";
	
	o++;
	int no = o;
	while ((w[no] >= '0' && w[no] <= '9') || w[no] == '.') no++;
	
	string prob = w.substr(o, no - o);
	istringstream ps(prob);
	ps >> n->p;
	//cout << "---" << prob << "---" << endl;
	
	o = no;
	
	if (w[o] == ')') { 
		//cout << "re" << " " << (o + 1) << " " << w[o+1] << endl;
		 return o; }
	
	while (w[no] != '(') no++;
	
	n->label = w.substr(o, no - o);
	
	o = no;
	
	n->st1 = new node();
	o = read_node(n->st1, w, o);
	o++;
	//cout << o << " bw" << endl;
	
	n->st2 = new node();
	o = read_node(n->st2, w, o);
	
	//cout << "r " << o  << " " << w[o] << endl;
	return o + 1;
}

int readint()
{
	string line;
	getline(cin, line);
	istringstream c(line);
	int k;
	c >> k;
	return k;
}

void print_node(node *n, int ti)
{	
	RP(i, 0, ti) cout << "  ";
	cout << n->p << " " << n->label << endl;
	if (n->st1)
	{
		print_node(n->st1, ti+1);
		print_node(n->st2, ti+1);
	}	
}

double prob(node *n, double p, set<string> &t)
{
	p *= n->p;
	
	if (n->st1)
	{
		if (t.count(n->label))
		{
			return prob(n->st1, p, t);
		}
		else
		{
			return prob(n->st2, p, t);
		}
	}
	
	return p;
}

int main()
{
	int vss = readint();
	//cin >> vss;
	RP(cs, 1, vss+1)
	{
		node *base = new node();
		
		int dtl = readint();
		//cout << dtl << endl;
		//cin >> dtl;
		
		stringstream k;
		RP(i, 0, dtl) {
			string l;
			getline(cin, l);
			k << l;
		}
		
		//cout << k.str() << endl;
		stringstream wt;
		string l;
		while (k >> l) { 
			wt << l;
		}
		
		//cout << wt.str() << endl;
		
		read_node(base, wt.str(), 0);		
		//print_node(base, 0);
		
		cout << "Case #" << cs << ":" << endl;
		
		int ams = readint();
		//cout << ams;
		RP(i, 0, ams)
		{
			string line;
			getline(cin, line);
			//cout << line << endl;
			
			istringstream traits(line);
			string name;
			traits >> name;
			
			int tc;
			traits >> tc;
			
			set<string> t;
			RP(j, 0, tc)
			{
				string tt;
				traits >> tt;
				t.insert(tt);
			}
			
			cout << setprecision(7) << fixed << prob(base, 1.0, t) << endl;
		}
		
		//clean up, or don't
	}
	return 0;
}