#define ONLINE_JUDGE
//#define GenerateTest

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <cmath>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <cstdlib>
#include <ctime>
#include <string>
#include <stack>
#include <list>
#include <sstream>
#include <hash_set>
#include <hash_map>

#include "BigInteger\cbignum.h"

using namespace std;
#pragma comment(linker, "/STACK:64777216")

typedef long long LL;
typedef unsigned long long ULL;
typedef cBigNumber cLL;

struct ttree
{
	map<string,ttree*> next;
}*root;
int res;
void add(ttree * root,vector<string> &p,int i = 0,bool is = false)
{
	if(i == p.size())
		return;
	if(root->next.find(p[i]) == root->next.end())
	{
		ttree *n = new ttree();
		root->next.insert(pair<string,ttree*>(p[i],n));

		++res;
	}
	add(root->next.find(p[i])->second,p,i + 1);
}
void deli(ttree *root)
{
	if(!root)
		return;
	map<string,ttree*>::iterator pt = root->next.begin();
	for(;pt != root->next.end();++pt)
	{
		deli(pt->second);
	}
	delete root;

}
void Solve()
{
	int tests;
	cin >> tests;
	for(int number_test = 0;number_test < tests;++number_test)
	{
		cout << "Case #" << number_test + 1 << ": "; 
		int m[2];

		cin >> m[0] >> m[1];
		root = new ttree();
		for(int k = 0;k < 2;++k)
		{
			res = 0;
			int n = m[k];
			for(int i = 0;i < n;++i)
			{
				string s;
				cin >> s;
				vector<string> put;
				for(int i = 0;i < s.size();)
				{
					if(s[i] == '/')
					{
						int j;
						string str;
						for(j = i + 1;j < s.size();++j)
						{
							if(s[j] == '/')
								break;
							str += s[j];
						}
						put.push_back(str);
						i = j;
					}
				}
				add(root,put);
			}
		}
		deli(root);
		cout << res << endl;
	}
}

int main()
{
#ifdef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);

	freopen("output.txt", "wt", stdout);
#endif

#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
//	freopen("output.txt", "wt", stdout);
	
#ifdef GenerateTest
	
	freopen("output.txt", "wt", stdout);

#endif

	clock_t start = clock();
#endif

	Solve();	

#ifndef ONLINE_JUDGE 
	clock_t end = clock();
	cout <<"\n\nTime: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
#endif
	return 0;
}