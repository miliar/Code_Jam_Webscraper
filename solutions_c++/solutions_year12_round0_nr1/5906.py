/*
 * A.CPP
 *
 *  Created on: Apr 14, 2012
 *      Author: mohammad
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <cctype>
#include <algorithm>
#include <functional>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

int main()
{
	char arr[28]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a', 'q'};
//	vector<string> input;
//	vector<string> output;
//	for(int i = 0 ; i < 3 ; i ++)
//	{
//		string t;
//		getline(cin,t);
//		input.push_back(t);
//	}
//	for(int i = 0 ; i < 3 ; i++)
//	{
//		string t;
//		getline(cin,t);
//		for(int j = 0 ; j < input[i].size() ; j++)
//		{
//			if(input[i][j]!=' ')
//				arr[input[i][j]-'a'] = t[j];
//		}
//	}
//	cout<<"{";
//	for(int i = 0 ; i < 26 ; i++)
//		cout<<"'"<<arr[i]<<"',";
//	cout<<"}";
//	cout<<endl;
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("a.out","wt",stdout);
	int t;
	cin>>t;
	string n;
	getline(cin,n);
	for(int i = 0 ; i < t ; i++)
	{
		getline(cin,n);
		string res = "";
		for(int j = 0 ; j < n.size() ; j++)
		{
			if(n[j]==' ')
				res+=' ';
			else res+=arr[n[j]-'a'];
		}
		cout<<"Case #"<<i+1	<<": "<<res<<endl;
	}

	return 0;
}


