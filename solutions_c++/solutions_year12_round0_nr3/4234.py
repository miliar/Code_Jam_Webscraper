#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
#include<sstream>
#include<ctime>
#include<set>
#include<queue>
#include<map>
#include<cstdio>
#include<cmath>
#include<map>
using namespace std;
typedef unsigned long long u64;
typedef long long i64;
typedef unsigned long long u32;
typedef long long i32;
const double EPS = 1e-9;
const double PI = 3.1415926535897932384626433832795;
i64 i64INF = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;
i32 i32INF = 1000 * 1000 * 1000;

int cnt(int n)
{
	int res = 0;
	while(n)
	{
		n /= 10;
		res++;
	}

	return res;
}

bool ok(i64 n, i64 m)
{
	int c = cnt(n);
	int pwd = 1;
	for(int i = 0; i < c-1; i++)
		pwd *= 10;

	for(int i = 0; i < c; i++)
	{
		if(n == m) return true;
		int p = m%10;
		m /= 10;
		m += p*pwd;
	}

	return false;
}

int main()
{
	freopen("codejam.in", "r", stdin);
	freopen("codejam.out", "w", stdout);
	int t;
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		int a, b;
		cin >> a >> b;

		int res = 0;
		for(int n = a; n <= b; n++)
			for(int m = n+1; m <= b; m++)
				if(ok(n, m))
					res++;

		cout << "Case #" << test << ": " << res << endl;
	}

	return 0;
}




/*
vector<string> mul(vector<string> a, vector<string> b)
{
	vector<string> res((a.size()-1)+(b.size()-1)+1);
	for(int i = 0; i < a.size(); i++)
	{
		for(int j = 0; j < b.size(); j++)
		{
			if(!res[i+j].empty()) res[i+j] += "+";
			res[i+j] += a[i]+"*"+b[j];
		}
	}
	return res;
}

string tostr(int a)
{
	string res="";
	if(a > 9) res += '0'+a/10;
	res += '0' + a%10;
	return res;
}

string changeSign(string s)
{
	if(s[0] == '-')
		return "+" + string(s.begin()+1, s.end());
	if(s[0] == '+')
		return "-" + string(s.begin()+1, s.end());
	return "-" + s;
}

/*
1.0
–1.4
–1.8 
–3.5 
–6.3 
–3.4 
–0.7 
–4.4 
–0.1 
–5.7 
–5.6 
–4.2


inline std::string replace(std::string text, std::string s, std::string d)
{
  for(unsigned index=0; index=text.find(s, index), index!=std::string::npos;)
  {
    text.replace(index, s.length(), d);
    index+=d.length();
  }
  return text;
}
/*
  5.0*z-0 
+ 3.7*z-1 
+ 7.8*z-2 
+ 0.2*z-3 
+ 6.9*z-4 
+ 7.9*z-5 
+ 5.4*z-6 
+ 2.5*z-7 
+ 6.5*z-8 
+ 6.8*z-9 

int main()
{
	vector<string> vals;
	vals.push_back("5.0");
	vals.push_back("3.7");
	vals.push_back("7.8");
	vals.push_back("0.2");
	vals.push_back("6.9");
	vals.push_back("7.9");
	vals.push_back("5.4");
	vals.push_back("2.5");
	vals.push_back("6.5");
	vals.push_back("6.8");
	vals.push_back("0.0");
	vals.push_back("0.0");
	vals.push_back("0.0");
	vals.push_back("0.0");
	vals.push_back("0.0");
	vals.push_back("0.0");

	vector<vector<string> > as(6);
	as[0].push_back("1.0");
	as[0].push_back("2.0439");
	as[0].push_back("2.2692");

	as[1].push_back("1.0");
	as[1].push_back("0.8948");
	as[1].push_back("0.2044");

	as[2].push_back("1.0");
	as[2].push_back("-2.4426");
	as[2].push_back("0.0000");

	as[3].push_back("1.0");
	as[3].push_back("-2.6475");
	as[3].push_back("4.0751");

	as[4].push_back("1.0");
	as[4].push_back("1.6394");
	as[4].push_back("1.2874");

	as[5].push_back("1.0");
	as[5].push_back("-0.8879");
	as[5].push_back("4.8073");

	vector<vector<string> > bs(6);
	bs[0].push_back("b(1)");
	bs[0].push_back("b(2)");

	bs[1].push_back("b(3)");
	bs[1].push_back("b(4)");

	bs[2].push_back("b(5)");
	bs[2].push_back("b(6)");

	bs[3].push_back("b(7)");
	bs[3].push_back("b(8)");

	bs[4].push_back("b(9)");
	bs[4].push_back("b(10)");
	
	bs[5].push_back("b(11)");
	bs[5].push_back("b(12)");


	vector<vector<string> > ress(6);

	for(int i = 0; i < 6; i++)
	{
		ress[i] = bs[i];
		for(int j = 0; j < 6; j++)
			if(i != j)
				ress[i] = mul(ress[i], as[j]);
	}


	vector<string> res(ress[0].size());
	for(int i = 0; i < 6; i++)
	{
		for(int j = 0; j < ress[i].size(); j++)
		{
			res[j] += ress[i][j] + " + ";
		}
	}

	for(int i = 0; i < res.size(); i++)
	{
		res[i] = replace(res[i], "1.0*", "");
		res[i] = replace(res[i], "*1.0", "");
		res[i] = string(res[i].begin(), res[i].end()-3);
	}



	srand(time(0));

	

	freopen("out.txt", "w", stdout);

	cout << "function y = f (x)" << endl;
	cout << "y = zeros (" << res.size() << ", 1);" << endl;

	for(int i = 0; i < res.size(); i++)
	{
		cout << "y(" << tostr(i+1) << ")=";
		cout << res[i] + changeSign(vals[i]) << ";" << endl;
	}
	cout << "endfunction" << endl;

	cout << "[x, fval, info] = fsolve (@f, [";
	for(int i = 0; i < 12; i++)
	{
		cout << 2.0*double(rand())/RAND_MAX;
		if(i != 12-1)
			cout << ";";
	}
	cout << "])" << endl;
	

	

	return 0;
}*/