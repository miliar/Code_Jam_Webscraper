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

string s="welcome to code jam";
int L=s.length();
vector< vector<int> > tree;

void DFS(int pre, int l, int pos, long long &cnt){
	//cout<<l<<" "<<L<<" "<<s[l]<<" "<<pre<<" "<<pos<<" "<<cnt<<endl;
	if(pos<pre){	return;}
	if(l==L-1){
		//cout<<endl;
		cnt++;	return;
	}
	
	pre=pos;
	for(int i=0;i<tree[l+1].size();i++){
		DFS(pre,l+1,tree[l+1][i],cnt);
	}
}

int main(){
	ifstream fin("C-small-attempt0.in");
	freopen("C-small-attempt0.out","w",stdout);
	
	int N;
	fin>>N;
	string text;
	getline(fin,text);
	for(int r=1;r<=N;r++){
		long long cnt=0;
		tree.clear();
		
		getline(fin,text);
		
		
		for(int i=0;i<s.length();i++){
			vector<int> tt;
			for(int j=0;j<text.length();j++){
				if(text[j]==s[i]){
					tt.push_back(j);
				}
			}
			tree.push_back(tt);
		}

		int pre=-1;
		for(int i=0;i<tree[0].size();i++){
			DFS(pre,0,tree[0][i],cnt);
		}
		
		cnt = cnt%10000;
		printf("Case #%d: %04d\n",r,cnt);
	}
}