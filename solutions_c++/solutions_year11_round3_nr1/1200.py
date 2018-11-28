//============================================================================
// Name        : round1A_1.cpp
// Author      : Toqa Osama
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <list>

using namespace std;

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test,R,C;
	cin>>test;
	for(int t = 1;t<=test;t++)
	{
		cin>>R>>C;
		vector<string> s(R);
		vector< vector<char> > res(R);
		for(int i = 0;i<R;i++){
			cin>>s[i];
			vector<char> w(C);
			res[i] = w;
		}
		bool f = true;
		cout<<"Case #"<<t<<":\n";
		for(int i = 0;i<R;i++)
		{
			for(int j = 0;j<s[i].size();j++)
			{
				if(s[i][j] == '.'){
					res[i][j]  = '.';
					s[i][j] = '*';
				}
				else if(s[i][j] == '#')
				{
					if(i+1<R&&j+1<C){
					if(s[i+1][j]=='#'&&s[i][j+1]=='#'&&s[i+1][j+1]=='#')
					{
						s[i+1][j]=s[i][j+1]=s[i+1][j+1]=s[i][j] ='*';
						res[i+1][j+1]=res[i][j] ='/';
						res[i+1][j]=res[i][j+1]='\\';
					}
					else{
											cout<<"Impossible\n";
											i = R;
											f = false;
											break;
					}
					}
					else{
						cout<<"Impossible\n";
						i = R;
						f = false;
						break;
					}
				}
			}
		}
		if(f==true)
		for(int i = 0;i<R;i++)
		{
			for(int j = 0;j<C;j++)
			cout<<res[i][j];
			cout<<endl;
		}
	}
	return 0;
}
