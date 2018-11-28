#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
#include <memory.h> 

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT((c)), (c).erase(unique(ALL((c))), (c).end())
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define X first
#define Y second

typedef pair<int,int> ii;
typedef vector<int > vi;
typedef vector<vi > vvi;
typedef vector<ii  > vii;
typedef vector<vii  > vvii;
typedef long long ll;

string filename = "A-large";

set<string> features;

struct Node
{
	double p;
	string feature;
	int l, r;
};

string str;
Node tree[50000];
int cur_pos;

void build(int index, string sss)
{
	string feature = "";
	double p;
	int left = -1, right = -1;
	int begin = sss.find_first_of('(');
	int end = sss.find_last_of(')');
	string ts = sss.substr(begin + 1, end - 1 - (begin + 1) + 1);
	int cnt = 0;
	int first_bracket = -1,
		last_bracket = -1;
	REP(i, ts.sz)
	{
		if (ts[i] == '(')
		{
			if (first_bracket == -1)
				first_bracket = i;
			cnt++;
		}
		else if (ts[i] == ')')
		{
			cnt--;
			if (cnt == 0)
			{
				last_bracket = i;
				break;
			}
		}
	}

	if (first_bracket == -1)
	{
		//leave
		istringstream ssin(ts);
		ssin>>p;
		Node node;
		node.p = p;
		node.l = left;
		node.r = right;
		node.feature = feature;
		tree[index] = node;
	}
	else
	{
		istringstream ssin(ts.substr(0, first_bracket));
		ssin>>p>>feature;
		
		left = cur_pos++;
		build(left, ts.substr(first_bracket, last_bracket - first_bracket + 1));
		right = cur_pos++;
		build(right, ts.substr(last_bracket+1, ts.sz - 1 - (last_bracket + 1) + 1));
		Node node;
		node.p = p;
		node.l = left;
		node.r = right;
		node.feature = feature;
		tree[index] = node;
	}
}

double now_p;

void go(int node)
{
	now_p *= tree[node].p;

	if (tree[node].l == -1 || tree[node].r == -1)
		return;

	if (features.find(tree[node].feature) != features.end())
	{
		go(tree[node].l);
	}
	else
	{
		go(tree[node].r);
	}
}

int main()
{	
	string str_fin = filename + ".in", str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);

	int T;
	cin>>T;
	string s;
	REP(t, T)
	{
		vector<double> res;
		int L;
		cin>>L;
		getline(cin, s);
		str = "";
		cur_pos = 0;
		REP(i, L)
		{
			getline(cin, s);
			str += (" " + s);
		}

		build(cur_pos++, str);

		int A;
		cin>>A;
		REP(i, A)
		{
			cin>>s;
			features.clear();
			int k;
			cin>>k;
			REP(j, k)
			{
				cin>>s;
				features.insert(s);
			}

			now_p = 1.0;
			go(0);
			res.pb(now_p);
		}
		cout<<"Case #"<<t+1<<": "<<endl;
		REP(i, res.sz)
			cout<<res[i]<<endl;
	}

	return 0;
}