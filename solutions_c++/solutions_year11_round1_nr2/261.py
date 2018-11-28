#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <time.h>


typedef long long LL;
typedef unsigned long long ULL;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

using namespace std;

int T;
vector<string> s;
string alf;
int n,m;

int Calc(int chosen, vector<string>& ss,int pos){
	if(pos == 26) return 0;
	char c = alf[pos];
	bool any = false;
	for(int i=0;i<ss.size();i++) if(ss[i].find(c) != -1){
		any = true;
		break;
	}
	if(!any) return Calc(chosen, ss, pos + 1);

	int col = 0;
	for(int i=0;i<s[chosen].length();i++) if(s[chosen][i] == c){
		col = 1;
		break;
	}
	vector<string> v;
	for(int i=0;i<ss.size();i++)if(ss[i].length() == s[chosen].length()){
		bool good = true;
		for(int j=0;j<s[chosen].length();j++)
			if(s[chosen][j] == c && ss[i][j] != c || s[chosen][j] != c && ss[i][j] == c ){
				good = false;
				break;
			}
		if(good) v.push_back(ss[i]);
	}
	return Calc(chosen, v, pos +1 ) + 1 - col;
}

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		
		cin >> n >> m;
		s.resize(n);
		for(int i=0;i<n;i++) cin >> s[i];

		printf("Case #%d:",_);
		for(int i=0;i<m;i++){
			int mx = -1, mi = 0;
			cin >> alf;
			for(int j=0;j<n;j++){
				vector<string> ss;
				for(int k=0;k<n;k++) if(s[k].length() == s[j].length()) ss.push_back(s[k]);
				int t = Calc(j, ss, 0);
				if(t > mx){
					mx = t;
					mi = j;
				}
			}
			cout << " " << s[mi];
		}
		cout << endl;
	}
	return 0;
}
