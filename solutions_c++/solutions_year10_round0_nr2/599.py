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
#include <iomanip>

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
typedef unsigned long long ull;

string filename = "test";

ll mod = 1000000000LL;

class Long{
	ll* mem;
	int len;

	friend ostream& operator<<(ostream& stream, const Long& val);
public:
	Long(){
		len = 1;
		mem = new ll[1];
		mem[0] = 0;
	}

	Long(int l){
		len = l;
		mem = new ll[len];
	}
	Long(string val){
		len = val.sz / 9 + (val.sz%9 ? 1 : 0);
		mem = new ll[len];
		for (int i = val.sz - 1, j = 0; i >= 0; ++j){
			mem[j] = 0;
			for (int k = MAX(0, i - 8); k <= i; ++k){
				mem[j] *= 10;
				mem[j] += (val[k] - '0');
			}
			i -= 9;
		}
	}

	Long(const Long& val){
		len = val.len;
		mem = new ll[len];
		memcpy(mem, val.mem, sizeof(ll)*len);
	}

	Long& operator=(const Long& val){
		len = val.len;
		mem = (ll*)realloc(mem, sizeof(ll)*len);
		memcpy(mem, val.mem, sizeof(ll)*len);
		return *this;
	}

	Long operator+(const Long& a)const{
		Long ret(MAX(len, a.len));
		ll t = 0;
		for (int i = 0; i < MAX(len, a.len); ++i){
			ret.mem[i] = (i < len ? mem[i] : 0) + (i < a.len ? a.mem[i] : 0) + t;
			t = ret.mem[i] / mod;
			ret.mem[i] %= mod;
		}
		if (t != 0){
			ret.mem = (ll*)realloc(ret.mem, sizeof(ll)*(MAX(len, a.len) + 1));
			ret.len++;
			ret.mem[ret.len - 1] = t;
		}
		return ret;
	}

	Long operator-(const Long& a)const{
		Long ret(len);
		ll t = 0;
		for (int i = 0; i < len; ++i){
			ret.mem[i] = mem[i] - (i < a.len ? a.mem[i] : 0) - t;
			if (ret.mem[i] < 0){
				ret.mem[i] += mod;
				t = 1;
			}else{
				t = 0;
			}
		}

		while (ret.mem[ret.len - 1] == 0 && ret.len > 1){
			ret.len--;
		}
		ret.mem = (ll*)realloc(ret.mem, sizeof(ll)*ret.len);

		return ret;
	}

	Long& operator++(){
		ll t = 0;
		for (int i = 0; i < len && t > 0; ++i){
			mem[i] += t;
			t = mem[i] / mod;
			mem[i] %= mod;
		}
		if (t != 0){
			mem = (ll*)realloc(mem, sizeof(ll)*(len + 1));
			len++;
			mem[len - 1] = t;
		}
		return *this;
	}

	bool operator<(const Long& a){
		if (len != a.len)
			return len < a.len;
		for(int i = len - 1; i >= 0; --i)
			if (mem[i] != a.mem[i])
				return mem[i] < a.mem[i];
		return false;
	}

	bool isZero()const{
		if (len > 1)
			return false;
		if (len == 0)
			return true;
		return mem[0] == 0;
	}

	bool operator==(const Long& a){
		if (len != a.len)
			return false;
		for (int i = 0; i < len; ++i)
			if (mem[i] != a.mem[i])
				return false;
		return true;
	}

	bool operator<=(const Long& a)const{
		if (len != a.len)
			return len < a.len;
		for(int i = len - 1; i >= 0; --i)
			if (mem[i] != a.mem[i])
				return mem[i] < a.mem[i];
		return true;
	}

	bool operator>(const Long& a){
		return !((*this) <= a);
	}

	bool operator>=(const Long& a){
		return !((*this) < a);
	}

	Long operator*(const Long& a){
		Long ret(len + a.len);
		memset(ret.mem, 0, sizeof(ll)*ret.len);
		ll t = 0;
		for (int i = 0; i < a.len; ++i){
			for (int j = 0; j < len; ++j){
				ret.mem[i + j] += (a.mem[i]*mem[j] + t);
				t = ret.mem[i + j] / mod;
				ret.mem[i + j] %= mod;
			}
			if (t != 0){
				ret.mem[i + len] = t;
				t = 0;
			}
		}

		while (ret.mem[ret.len - 1] == 0 && ret.len > 1){
			ret.len--;
		}
		ret.mem = (ll*)realloc(ret.mem, sizeof(ll)*ret.len);

		return ret;
	}

	int digits()const{
		if (isZero())
			return 1;
		ll t = mem[len - 1];
		int ret = 0;
		while (t){
			t /= 10;
			ret++;
		}
		ret += (len - 1)*9;
		return ret;
	}

	bool isOne()const{
		if (len != 1)
			return false;
		return mem[0] == 1;
	}

	void shift10(int t){
		int add = t / 9;
		t %= 9;
		if (add){
			mem = (ll*)realloc(mem, sizeof(ll)*(len + add));
			for (int i = len - 1; i >= 0; --i){
				mem[i + add] = mem[i];
				mem[i] = 0;
			}
			len += add;
		}
		ll mul = 1;
		REP(i, t)
			mul *= 10;
		ll tr = 0;
		for (int j = 0; j < len; ++j){
			mem[j] *= mul;
		}
		for (int j = 0; j < len; ++j){
			mem[j] += tr;
			tr = mem[j] / mod;
			mem[j] %= mod;
		}
		if (tr != 0){
			mem = (ll*)realloc(mem, sizeof(ll)*(len + 1));
			len = len + 1;
		}
	}
};

ostream& operator<<(ostream& stream, const Long& val){
	stream << val.mem[val.len - 1];
	for (int i = val.len - 2; i >= 0; --i)
		stream << setfill('0') << setw(9) << val.mem[i];
	return stream;
}

void fmod(const Long& a, const Long& b, Long& mod){
	mod = Long();
	Long left(a);
	int d1 = a.digits();
	int d2 = b.digits();
	while (d1 > d2 + 1)
	{
		Long tmp(b);
		tmp.shift10(d1 - d2 - 1);
		left = left - tmp;
		d1 = left.digits();
	}	
	while (b <= left)
		left = left - b;
	mod = left;
}

Long gcd(const Long& a, const Long& b){
	if (b.isZero())
		return a;
	Long m;
	fmod(a, b, m);
	return gcd(b, m);
}

int main(){
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	
	/*
	int N = 1000;
	cout<<1<<endl;
	cout<<N<<endl;
	REP(i, N){
		if (i)
			cout<<" ";
		int len = rand() % 50;
		cout<<(1 + rand()%9);
		REP(j, len)
			cout<<rand()%10;
	}
	return 0;
	*/

	int T;
	cin>>T;
	for (int test = 0; test < T; ++test){
		int n;
		cin>>n;
		vector<Long> v;
		string str;
		for (int i = 0; i < n; ++i){
			cin>>str;
			v.push_back(Long(str));
		}
		sort(v.begin(), v.end());
		Long res;
		bool one = false;
		for (int i = 0; i < n; ++i){
			for (int j = i + 1; j < n; ++j){
				if (i == 0 && j == 1)
					res = v[j] - v[i];
				else
					res = gcd(res, v[j] - v[i]);
				if (res.isOne()){
					one = true;
					break;
				}
			}
			if (one)
				break;
		}
		Long t;
		fmod(v[0], res, t);
		if (t.isZero())
			res = Long("0");
		else
			res = res - t;
		cout<<"Case #"<<test+1<<": "<<res<<endl;
	}

	return 0;
}