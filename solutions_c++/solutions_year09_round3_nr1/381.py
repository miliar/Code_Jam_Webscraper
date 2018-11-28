#pragma region MyTemplate
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;

typedef unsigned long long ll;
typedef long double ld;
typedef vector<int> ivec;
typedef vector<string> svec;
typedef vector<double> dvec;
typedef pair<int,int> ipair;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define PRECISION(fout, caseid, obj, i) fout<<"Case #"<<caseid<<": "<<setw(i)<<setprecision(i)<<left<<setfill('0')<<showpoint<<obj<<endl

#define MAXCHILD 10
class TREE{
public:
	TREE():p(NULL),childno(0){
		chi = new TREE*[MAXCHILD];
	}
	int childno;
	TREE *p;
	TREE **chi;
	//other data member:
};
#pragma endregion

int T, base;
ifstream fin;
ofstream fout;
map<char,int> ch;

int main(){
	fin.open("A-large.in");
//	fout.open("small-result.txt");
	fout.open("large-result.txt");

	string s;
	getline(fin, s);
	stringstream ss(s);
	ss>>T;
	For(caseid,1,T){
		//Read Input Data:
		string s;
		getline(fin,s);
		ch.clear();
		Rep(i,s.size()){
			ch.insert(MP(s[i],-1));
		}

		//Compute:
		base = ch.size();
		cout<<base<<" "<<s.size()<<endl;
		ll ans;
		ch[s[0]]=1;
		int k=0;
		ans = 1;
		For(i, 1, s.size()-1){
			if(ch[s[i]]==-1){
				ch[s[i]]=k;
				k++;
				if(k==1){ k=2;}
			}
			ans *= base;
			ans += ch[s[i]];
		}

		if(base == 1){
			if(s.size()>1){
				ans = (1<<s.size()) -1;
			}
		}

		//Output:
		fout<<"Case #"<<caseid<<": "<<ans<<endl;
	}
	fin.close();
	fout.close();
	cin>>T;
}
