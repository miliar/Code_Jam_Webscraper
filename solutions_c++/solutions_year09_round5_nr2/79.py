#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <map>
#include <set>
using namespace std;

#define PT pair<int,int >
#define MP make_pair
#define VI vector<int >
map<pair<pair<int,int>,pair<vector<int>,long long> >,long long> memo;

const long long MOD = 10009;

int gg[1050][30];

int factor[10];
string ss;//expr to do
int N;

long long func(VI &ctr)
{
	long long out = 1;
	for(int i=0;i<ctr.size();++i)
	{
		out *= ctr[i];
		out %= MOD;
	}
	return out%MOD;
}

long long invv[25];
long long powmod(long long n,long long p,long long MOD)
{
	n %= MOD;
/*	if(MOD != 2)
	{
		p %= MOD-1;
	}*/
	long long out = 1,z = n;
	for(long long i=1;i<=p;i<<=1)
	{
		if((p&i) != 0)
		{
			out *= z;
			out %= MOD;
		}
		z *= z;
		z %= MOD;
	}
	return out;
}

long long dp(int at,int left,VI ctr,long long tt)
{
	if(left == 0)
	{
		return (func(ctr)*tt)%MOD;
	}
	//if(N-at < left){return 0LL;}
	if(at == N)
	{
		if(left == 0)
		{
			return (func(ctr)*tt)%MOD;
		}
		else
		{
			return 0LL;
		}
	}
	pair<pair<int,int>,pair<vector<int>,long long> >  zz= MP(MP(at,left),MP(ctr,tt));
	if(memo.find(zz) != memo.end()){return memo[zz];}
	long long ret = 0LL;
//	if(N-(at+1) >= left)
	{
		ret += dp(at+1,left,ctr,tt);
		ret %= MOD;
	}
	//if(N-at >= left-1)
	{
		for(int q=1;q<=left;++q)
		{
			for(int i=0;i<ctr.size();++i)
			{
				ctr[i] += gg[at][ss[i]-'a'];// * factor[i];
				ctr[i] %= MOD;
			}
			ret += dp(at+1,left-q,ctr,(tt*invv[q])%MOD);
			ret %= MOD;
		}
	}
	memo[zz] = ret;
	return ret;
}


int main(int argc,char **argv)
{
	int CASES;
	cin >> CASES;
	long long tmp =1;
	for(int i=1;i<25;++i)
	{
		tmp *= i;
		invv[i] = powmod(tmp,MOD-2,MOD);
	}
	for(int cn=1;cn<=CASES;++cn)
	{
		string expr;
		cin >> expr;
		for(int i=0;i<expr.size();++i)
		{if(expr[i]=='+'){expr[i] = ' ';}}
		istringstream iss(expr);
		vector<string> todo;todo.clear();
		while(iss >> expr)
		{todo.push_back(expr);}
		int K;
		cin >> K;
		vector<long long> out(10,0LL);
		cin >> N;
		memset(gg,0,sizeof(gg));
		for(int i=0;i<N;++i)
		{
			cin >> expr;
			for(int j=0;j<expr.size();++j)
			{
				++gg[i][expr[j]-'a'];
			}			
	/*		for(int j=0;j<26;++j)
			{
				cerr << gg[i][j] << " ";
			}cerr << endl;*/
		}
		for(int i=0;i<todo.size();++i)
		{
		/*	ss.clear();
			int idx = 0;
			vector<int> v(26,0);
			for(int j=0;j<todo[i].size();++j)
			{
				++v[todo[i][j]-'a'];
			}
			for(int j=0;j<26;++j)
			{
				if(v[j])
				{ss.push_back('a'+j);factor[idx++] = v[j];}
			}
			//cerr << todo[i] << endl;
			//for(int i=0;i<idx;++i)
			//{cerr << factor[i] << " ";}cerr << endl;*/
			ss = todo[i];
			memo.clear();
			for(int j=0;j<K;++j)
			{
				long long a = dp(0,j+1,vector<int>(todo[i].size(),0),1);
			//	cerr << a << " ";
				out[j] += a;
				out[j] %= MOD;
			}
			//cerr << endl;
		}
		for(int i=0;i<10;++i)
		{
			for(int j=0;j<=i;++j)
			{
				out[i] *= j+1;
				out[i] %= MOD;
			}
		}

		printf("Case #%d:",cn);
		for(int i=0;i<K;++i)
		{printf(" %lld",(out[i]%MOD));}//%d\n",cn,out);
		printf("\n");
		fflush(stdout);
	}
	return 0;
};
