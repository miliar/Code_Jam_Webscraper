#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include <set>
using namespace std;

#ifndef ONLINE_JUDGE
#include<fstream>
  ifstream in("B-small-attempt2.in.txt");
  ofstream out("b.out");
#define cin in
#define cout out
#endif

//带路径压缩的并查集,用于动态维护查询等价类

#define MAXN 100000
#define _ufind_run(x) for(;p[t=x];x=p[x],p[t]=(p[x]?p[x]:x))
#define _run_both _ufind_run(i);_ufind_run(j)

struct ufind{
	int p[MAXN],t;
	void init(){memset(p,0,sizeof(p));}
	void set_friend(int i,int j){_run_both;p[i]=(i==j?0:j);}
	int is_friend(int i,int j){_run_both;return i==j&&i;}
};

int gcd(int a,int b){
	return b?gcd(b,a%b):a;
}

int main()
{
	int cs;
	cin>>cs;
	
	for(int ct = 1; ct <= cs; ct ++)
	{
		cout << "Case #"<<ct<<": ";

		int a, b, p;

		cin >> a >> b >> p;

		vector<int> prime;
		for(int i = p; i <=b; i ++)
		{
			if(i == 2)
				prime.push_back(i);

			bool found = true;
			for(int j = 2; j < i; j ++)
			{
				if(i % j == 0)
				{
					found  = false;
					break;
				}
			}

			if(found)
				prime.push_back(i);
		}

		ufind uf;
		uf.init();
/*		for(int i = 0; i < prime.size(); i ++)
			for(int j = i + 1; j < prime.size(); j ++)
			{
				long long temp = prime[i];
				temp *= prime[j];
				if(temp >= a && temp <= b)
				{
					uf.set_friend(prime[i], prime[j]);
				}
			}
		for(int i = 0; i < prime.size(); i++)
		{
			int cur = prime[i];
			uf.is_friend(cur,cur);
		}

		set<int> puf;
		for(int i = 0; i < prime.size(); i++)
		{
			int cur = prime[i];
			int parent = uf.p[cur];
			if(parent == 0)
				parent = cur;
			puf.insert(parent);
		}

		int ans = 0;
		
		
		set<int> ttset;
		
		for(int i = a; i <= b; i ++)
		{
			bool found = false;
			for(int j = 0; j < prime.size(); j++)
			{
				if(i % prime[j] == 0)
				{
					int parent = uf.p[prime[j]];
					if(parent == 0)
						parent = prime[j];
					ttset.insert(parent);

					found = true;
					break;
				}
			}
			if(!found)
			{
				ans ++;
			}
		}
		
		ans += ttset.size();
*/
		for(int i = a; i <= b; i++)
			for(int j = i + 1; j <= b; j++)
			{
				int gy = gcd(i,j);
				bool found = false;
				for(int k = 0; k < prime.size(); k ++)
				{
					if(gy  % prime[k] == 0)
					{
						found = true;
						break;
					}
					if(gy < prime[k])
						break;
				}
				if(found)
				{
					uf.set_friend(i,j);
				}
			}
		int ans = 0;
		
		set<int> s;
		for(int i = a; i <= b; i ++)
		{
			uf.is_friend(i,i);
		
		}

		for(int i = a; i<=b; i++)
		{
			int parent = uf.p[i];
			if(parent == 0)
				parent = i;
			s.insert(parent);
		}

		ans = s.size();
		cout <<ans << endl;

	}
}
