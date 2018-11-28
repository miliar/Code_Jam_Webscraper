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
#include <queue>
#include <fstream>

using namespace std;
vector <string> dict;
vector<vector <string> > vs;

int main(){
	int L,D,N;
	cin >> L >> D >> N;
	string a,b;
	int i,j,k,m;
	for(i = 0 ; i < D; ++i){
		cin >> a;
		dict.push_back(a);
	}
	for(i = 0; i < N; ++i){
	//	cout<<"hello"<<endl;
		cin >> a;
		for(j = 0; j < a.size(); ++j){
			if(a[j] == '('){
				a[j] = ' ';
				while(a[j] != ')')++j;
				a[j] = ' ';
			}
			else{ 
				a.insert(j," ");
				j++;
			}
		}
	//	cout<<a<<endl;
		stringstream ss;
		ss << a;
		vector <string> t,boob;
		while(ss >> b)t.push_back(b);
		
		for(j = 0;j < t.size(); ++j){
			string ttt="";
			for(k = 0; k < 26; ++k){
				ttt += '0';
			}
			for(k = 0; k < t[j].size(); ++k){
				ttt[t[j][k]-'a'] = '1';
			}
			boob.push_back(ttt);
		}	
		vs.push_back(boob);
	}
//	for(i = 0;i < dict.size(); ++i)cout<<dict[i]<<" ";cout<<endl;

	vector <int> cnt(N);
	for(i = 0; i < N; ++i){
		for(j = 0; j < D; ++j){
			bool b = 1;
			for(m = 0 ; m < L; ++m){
				if(vs[i][m][dict[j][m] - 'a'] == '0'){
					b = 0;
					break;
				}
			}
			if(b)++cnt[i];
		}
	}
	for(i = 1; i <= N; ++i)
	cout<<"Case #"<<i<<": "<<cnt[i-1]<<endl;
}