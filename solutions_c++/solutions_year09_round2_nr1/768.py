//Decision Tree


// Author: Vijay S, MIT, Anna University.
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
using namespace std;


#define oo (int)1e8
#define LET(a,b) __typeof__(b) a(b)
#define v(x) vector<x>
#define pb push_back
#define sz size()
#define forz(i,n) for(int i = 0; i < (n); i++)
#define foro(i,o) for(int i = 0; i < (o).size(); i++)
#define fore(i,o) for(LET(i,o.begin()); i != (o).end(); i++)
#define all(a) (a).begin(),(a).end()
#define clr(a,v) memset((a),(v),sizeof(a))
#define isto(c,x) ((c).find(x) != (c).end()) 
#define ist(c,x) (find(all(c),x) != (c).end()) 
#define GI ({int t; scanf("%d",&t);t;})

#define dbg(x) (cerr << #x << ": " << x<<'\t')
#define dbge(x) (dbg(x),cerr << endl)
#define iamhere (cout<< "I am here!!\n")

typedef pair<int,int> ii; 
typedef stringstream ss;
typedef long long ll;
typedef long double ld;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef priority_queue<ii,vector<ii>,greater<ii> > p_q;

template<class A, class B> A cvt(B a) { ss in; in << a; A ret; in >> ret; return ret; }
template <class T>
inline void cmax(T &a, T b) { a = max(a,b); } 
template <class T>
inline void cmin(T &a, T b) { a = min(a,b); } 

struct node {
	double prob;
	string feature;
	struct node* left, *right;
};

node* getNode(stringstream& in)
{
	
	while (in.get()!='(');
	
	double prob;
	in >> prob;
	node* N = new node;
	N->prob = prob;
	char c;
	N->feature = "";
	N->left = NULL, N->right = NULL;
	while(true)
	{
		c = in.get();
		if(isalpha(c)) {
			in.unget();

			in >> N->feature;
			N->left = getNode(in);
			N->right = getNode(in);
		}
		if(c == ')')
			break;
	}

	return N;
}

int main()
{
//	ios_base:: sync_with_stdio(false);
	int t = GI;
	forz(tt,t)
	{
		int l = GI;
		getchar();
		vector<string> line(l);
		forz(i,l) {
			
			getline(cin,line[i]);		
			line[i] += " ";
		}
		string tot = accumulate(all(line),string(""));
		stringstream ss(tot);
		node* root = getNode(ss);
		int  A = GI;
		cout << "Case #"<<tt+1<<":"<<endl;
		forz(j,A) {
			set<string> tes;
			double p = 1;
			string aname; cin >> aname;
			int n = GI;
			forz(k,n) { string prop; cin>>prop;tes.insert( prop); }
			node* ptr = root;
			while(ptr != NULL)
			{
				p *= ptr->prob;
				if(tes.count(ptr->feature)) 
					ptr = ptr->left;
				else 
					ptr = ptr->right;
			}
			cout << p<<endl;
		}
	}	
}

