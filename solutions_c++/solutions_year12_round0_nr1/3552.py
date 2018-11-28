/*
 * A.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: B2lawa
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
char mp[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	freopen("in.in","rt",stdin);
	freopen("out.out","wt",stdout);
	int t;
	cin>>t;
	string s;
	getline(cin,s);
	for(int tt=1;tt<=t;++tt)
	{
		string res="";
		getline(cin,s);
		for(int i=0;i<(int)s.size();++i)
			res+=( (s[i]==' ') ? ' ' : mp[s[i]-'a']);
		cout<<"Case #"<<tt<<": "<<res<<endl;
	}
}
