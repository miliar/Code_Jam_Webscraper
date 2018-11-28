#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;

#define fore(i,n) for(int i = 0; i < (n); i++)
#define fort(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

#define M 1000000000
#define err(...) fprintf(stderr, __VA_ARGS__)

#define maxn 1010

struct bint
{
	vector<int> v;
	bint(int xx = 0)
	{
		v.push_back(xx);
	}
	void fix()
	{
		while(v.size() > 1 && v.back() == 0) v.pop_back();
	}
	bint operator- (bint y)
	{
		bint res;
		res.v = v;
		int l = y.v.size(), pp = 0;
		fore(i,l)
		{
			res.v[i] -= pp;
			pp = 0;
			if(res.v[i] < y.v[i])
			{
				res.v[i] += M;
				pp = 1;
			}
			res.v[i] -= y.v[i];
		}
		for(int i = l; pp; i++)
		{
			res.v[i] -= pp;
			if(res.v[i] < 0)
			{
				res.v[i] += M;
				pp = 1;
			}
			else pp = 0;
		}
		res.fix();
		return res;
	}
	bint operator+ (bint y)
	{
		bint res;
		res.v = v;
		while(res.v.size() < y.v.size()) res.v.push_back(0);
		int pp = 0;
		fore(i,res.v.size())
		{
			int cur = i < y.v.size() ? y.v[i] : 0;
			res.v[i] += cur + pp;
			pp = 0;
			if(res.v[i] >= M)
			{
				res.v[i] -= M;
				pp = 1;
			}
		}
		if(pp) res.v.push_back(1);
		res.fix();
		return res;
	}
	bint mno(int Q, bint y)
	{
		bint res;
		fore(i,Q) res = res + y;
		return res;
	}
	bint operator% (bint y)
	{
		bint res;
		res.v = v;
		bint temp;
		temp = y;
		int q;
		for(q = 0; temp < res; q++) temp = mno(10,temp);
		for(; q >= 0; q--)
		{
			temp = y;
			fore(i,q) temp = mno(10,temp);
			while(! (res < temp)) res = res - temp;
		}
		/*
		printf("  "); print();
		printf("%% "); y.print();
		printf("= "); res.print();
		*/
		return res;
	}
	void read()
	{
		char temp[66];
		scanf("%s", temp);
		int n;
		for(n=0; temp[n]; n++) ;
		v.clear();
		for(int i = 0; i < n; i+= 9)
		{
			int cur = 0;
			for(int j = n-i-9; j < n-i; j++) cur = cur * 10 + (j < 0 ? 0 : temp[j] - '0');
			v.push_back(cur);
		}
		//printf("wczytal "); print();
	}
	void print()
	{
		printf("%d", v[v.size()-1]);
		for(int i = v.size()-2; i >= 0; i--) printf("%09d", v[i]);
		printf("\n");
	}
	bool operator== (bint y)
	{
		return v == y.v;
	}
	bool operator< (bint y) const
	{
		if(v.size() != y.v.size()) return v.size() < y.v.size();
		for(int i = v.size() - 1; i >= 0; i--) if(v[i] != y.v[i]) return v[i] < y.v[i];
		return 0;
	}
};

int n;
bint t[maxn];

bint gcd(bint a, bint b)
{
	if(b == 0) return a;
	return gcd(b,a%b);
}

void test()
{
	bint A,T;
	scanf("%d", &n);
	fore(i,n) t[i].read();
	sort(t,t+n);
	fore(i,n) fore(j,i) T = gcd(t[i]-t[j],T);
	T.print();
	A = t[0] % T;
	A = T - A;
	A = A % T;
	A.print();
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ", TT);
		test();
	}
}
