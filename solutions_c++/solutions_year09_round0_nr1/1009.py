//
//  untitled
//
//  Created by  on 2009-09-02.
//  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
//

#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <vector<int> > VVI;
typedef pair <int,int> PII;
typedef pair <int,PII> PIII;
typedef vector <LL> VL;
typedef vector <string> VS;

vector<map<char,int> > memo(50);

int go(VS &v, string &str, int l)
{
	int ret = 0;
	bool in_token = false;
	string curr_tok = "";
	int tok = 0;
	for(int i = 0; i < 50; ++i)
	{
		memo[i].clear();
	}
	for(int i = 0; i < str.size(); ++i)
	{
		if (str[i] == '(') in_token = true;
		else if (str[i] == ')') in_token = false;
		else {
			curr_tok += str[i];
		}
		if (!in_token && curr_tok.size() > 0) {
			for(int j = 0; j < curr_tok.size(); ++j)
			{
				memo[tok][curr_tok[j]] = 1;
			}
			tok++;
			curr_tok = "";
			in_token = false;
		}
	}
	for(int i = 0; i < v.size(); ++i)
	{
		string s = v[i];
		bool good = true;
		for(int j = 0; j < s.size(); ++j)
		{
			if (!memo[j][s[j]]) {
				good = false;
				break;
			}
		}
		if (good) {
			ret++;
		}
	}
	return ret;
}

int main()
{
	int l,d,n;
	scanf("%d %d %d\n",&l,&d,&n);
	VS v;
	for(int i = 0; i < d; ++i)
	{
		string str;
		cin >> str;
		v.push_back(str);
	}
	for(int i = 0; i < n; ++i)
	{
		string str;
		cin >> str;
		int ret = go(v,str,l);
		printf("Case #%d: %d\n", i+1,ret);
	}
	
	return 0;
}