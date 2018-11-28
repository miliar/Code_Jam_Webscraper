#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

#include <set>
#include <map>

#include <queue>
#include <deque>
#include <stack>
#include <list>

#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	
	int L, D, N;
	cin>>L>>D>>N;
	
	vector <string> x;
	for(int i = 0; i < D; i++){
		string word;
		cin>>word;
		
		x.push_back(word);
	}
	
	vector <string> y;
	for(int i = 0; i < N; i++){
		string pattern;
		cin>>pattern;
		
		int j = 0;
		int l;
		cout<<"Case #"<<i+1<<": ";
		while(j < pattern.size()){
			if(pattern[j] == '('){
				l = pattern.find(')', j)-j-1;
				string pat = pattern.substr(j+1, l);
				y.push_back(pat);
				j = pattern.find(')', j);
			}else{
				l = 1;
				string pat = pattern.substr(j, 1);
				y.push_back(pat);
			}
			j++;
		}
		
		int c = 0;
		for(int j = 0; j < D; j++){
			int k = 0;
			bool s = true;
			while((k < L) && (s == true)){
				string aux = x[j].substr(k, 1);
				int pos = y[k].find(aux);
				if(pos == -1){
					s = false;
				}
				k++;
			}
		
			if(s){
				c++;
			}
		}
		cout<<c;
		cout<<endl;
		y.clear();
	}
	
	return 0;
}
