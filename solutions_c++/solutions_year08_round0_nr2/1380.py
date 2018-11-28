#include<iostream>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
#include<utility>

using namespace std;
using namespace __gnu_cxx;

typedef long long _ll;
typedef vector<int> _vi;
typedef vector<vector<int> > _vvi;
typedef vector<string> _vs;
typedef istringstream _is;
typedef ostringstream _os;

#define INFTY 1000000000
#define PB push_back
#define ALL(v) (v).begin(),(v).end()
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define PRINT(v) FORS(i,v) cerr<<v[i]<<" "; cerr<<endl;
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();(i)++)

struct Train{
	int dep;
	int arr;
	bool dir;
};

inline bool operator<(const Train& A, const Train& B){
	return A.dep < B.dep;
}

struct cmp{
public: bool operator()(int a, int b){ return a>b; }
};

int f(string t){
	int res = (t[0]-'0') * 600;
	res += (t[1]-'0') * 60;
	res += (t[3]-'0') * 10;
	res += (t[4]-'0');
	return res;
}

void do_it(int test){
	int T,NA,NB;
	cin >> T >> NA >> NB;

	vector<Train> v;

	string dep,arr;
	REP(i,NA){
		cin >> dep >> arr;
		Train t;
		t.dep = f(dep);
		t.arr = f(arr);
		t.dir = false;
		v.PB(t);
	}
	REP(i,NB){
		cin >> dep >> arr;
		Train t;
		t.dep = f(dep);
		t.arr = f(arr);
		t.dir = true;
		v.PB(t);
	}

	sort(ALL(v));

	priority_queue<int, vector<int>, cmp> pA,pB;

	int resA=0,resB=0;
	FORS(i,v){
		if(!v[i].dir){
			if(pA.empty() || pA.top() > v[i].dep) resA++;
			else pA.pop();
			pB.push(v[i].arr+T);
		}
		else{
			if(pB.empty() || pB.top() > v[i].dep) resB++;
			else pB.pop();
			pA.push(v[i].arr+T);
		}
	}

	cout << "Case #" << test << ": " << resA << " " << resB << endl;
}

int main(){
	int N;
	cin >> N;
	REP(i,N) do_it(i+1);
	return 0;
}

