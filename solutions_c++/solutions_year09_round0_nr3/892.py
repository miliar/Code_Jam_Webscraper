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
string ow;

string gcj = "welcome to code jam";
		
int *sv;
int bl, sl;

int dn(int sp, int bp)
{
	if (sp == sl) { return 1; }
	if (bp == bl) return 0;
	
	if (sv[bp * sl + sp] != -1) return sv[bp * sl + sp];
	
	sv[bp * sl + sp] = 0;
	sv[bp * sl + sp] += dn(sp, bp + 1);
	if (ow[bp] == gcj[sp]) sv[bp * sl + sp] += dn(sp + 1, bp + 1);
	sv[bp * sl + sp] %= 10000;
	
	return sv[bp * sl + sp];
}

int main()
{
	int n;
	
	string l;
	getline(cin, l);
	istringstream nnnn(l);
	nnnn >> n;
	
	RP(cs, 1, n + 1)
	{
		string w;
		getline(cin, w);
		
		ow = "";
		R(i, w) if (gcj.find(w[i]) != string::npos) ow += w[i];
		//ow = w;
		
		bl = ow.size();
		sl = gcj.size();
		
		sv = new int[bl * sl];
		RP(i, 0, bl * sl) sv[i] = -1;
		
		int nn = dn(0, 0);
		
		/*
		for (int i = 0; i < bl; ++i)
		{
			for (int j = 0; j < sl; ++j)
			{
				cout << sv[i * sl + j] << " ";
			}
			cout << endl;
		}
		*/
		
		//int nn = sv[0];
		
		delete[] sv;
		
		cout << "Case #" << cs << ": " << setw(4) << setfill('0') << nn << endl;
	}
	
	return 0;
}