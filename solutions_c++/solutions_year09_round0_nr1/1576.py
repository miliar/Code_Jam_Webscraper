// BEGIN CUT HERE

// END CUT HERE
#line 5 "ImportsList.cpp"
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)


int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int l, dn, tn;
	fin>>l>>dn>>tn;
	vector<string> map;
	for(int i=0;i<dn;i++){
		string tmp;
		fin>>tmp;
		map.push_back(tmp);
	}
	
	for(int i=0;i<tn;i++){
		string word;
		fin>>word;
		bool used[20][27];
		memset(used,false,sizeof(used));
		
		int cnt=0;
		bool begin=true;
		bool start=false;
		
		for(int j=0;j<word.size();j++){
			
			if(word[j]!='(' && begin){
				used[cnt][word[j]-'a']=true;
				cnt++;
				continue;
			}
			if(word[j]=='('){
				begin=false;
				start=true;
				continue;
			}
			if(word[j]!='(' && word[j]!=')' && start){
				used[cnt][word[j]-'a']=true;
				continue;
			}
			if(word[j]==')'){
				start=false;
				begin=true;
				cnt++;
				continue;
			}
		}
		
		/*
		for(int j=0;j<l;j++){
			for(int k=0;k<26;k++){
				if(used[j][k]){
					cout<<char('a'+k)<<" ";
				}
			}
			cout<<endl;
		}
		*/
		
		int count=0;
		for(int j=0;j<dn;j++){
			bool maybe=true;
			for(int k=0;k<l;k++){
				if(!used[k][map[j][k]-'a']){
					maybe=false;
				}
			}
			if(maybe){
				count++;
			}
		}
		
		fout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}













