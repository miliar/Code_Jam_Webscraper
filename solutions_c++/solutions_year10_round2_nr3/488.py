

#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i = a; i <b ; i++)
#define FRR(i,a,b) for(int i = b - 1; i >=a ; i--)
#define sz size()
#define pb push_back
#define VI vector<int>
#define VVI vector<VI>
#define eps 1e-9
#define mp make_pair()
#define SS stringstream

int getRank(int m, int c){
	int ret = 0;
	FOR(i,0,c)if(m&(1 << i))ret++;
	return ret;
		
}

int main(){
	int cases;
	cin >> cases;
	FOR(caseNum, 0, cases){
		int n;
		cin >> n;
		int ans = 0;
		FOR(m,0,1<<n){
			if(m&1)continue;
			int c=n;
			bool good = true;
			while(good){
				if(c == 1)break;
				if(m & (1 << (c-1))){
					int d = getRank(m,c);
					if(d == c)good = false;
					else c = d;
				}
				else good = false;
			}
			ans+=good;	
		}
		ans=ans%100003;
		cout << "Case #" << caseNum+1 << ": " << ans << endl;
	}
	
}