#include<algorithm>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<iostream>
#include<cctype>
#include<cmath>
#include<iterator>
#include<cstdlib>
#include<sstream>
#include<cstdio>
#include<cassert>
#include<climits>
#include<string>
#include<map>
#include<set>
#include<stack>
#include<numeric>
#include<complex>
#include<valarray>


#define FOR(i,a,b) for(int i=a; i<b; i++)
#define F(i,n) for(int i=0; i<n; i++)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define LL long long
#define VI vector<int>

using namespace std;

int main() {
	int N; cin>>N;
	int caseN = 0;
	while(N--) {
		caseN++;
		int n;
		cin >> n;
		vector<char> all; VI o; VI b;
		char ch; int num;
		F(i,n) {
			cin >> ch >> num;
			if(ch == 'O') {
				o.pb(num);
			} else {
				b.pb(num);
			}
			all.pb(ch);
		}
		int ctrO=0, ctrB=0, ctrAll=0;
		int locO=1, locB=1;
		int totalTime=0;
		int totalCount=0;
		
		bool existsB = (b.size() > 0);
		bool existsO = (o.size() > 0);
		
		while(totalCount < n) {
		/*	cout << "total count  = " << totalCount << endl;
			cout << "currently processing " << all[ctrAll] << endl;
			cout << "value of o[ctrO] = " << o[ctrO] << endl;
			cout << "value of locO = " << locO << endl;*/
			//cin >> ch;
			totalTime++;
//			cout << "all[ctrAll]= " << all[ctrAll] << endl;
			if(all[ctrAll] == 'O') {
//			cout << "inside " << endl;
				if(existsO && locO == o[ctrO]) {
					ctrO++;
					totalCount++;
					ctrAll++;
				}
				else if(existsO && locO < o[ctrO]) {
					locO++;
				}
				else if (existsO) {
					locO--;
				}
				
				if(existsB && locB < b[ctrB]) {
					locB++;
				}
				else if( existsB && locB > b[ctrB]) {
					locB--;
				}
			}
			
			else if(all[ctrAll] == 'B' ) {
				if(existsB && locB == b[ctrB]) {
					ctrB++;
					totalCount++;
					ctrAll++;
				}
				else if(existsB && locB < b[ctrB]) {
					locB++;
				}
				else if(existsB){
					locB--;
				}
				
				if(existsO && locO < o[ctrO]) {
					locO++;
				}
				else if(existsO && locO > o[ctrO]) {
					locO--;
				}
			}
		}
		cout << "Case #" << caseN << ": " << totalTime << endl;
				
	}	
	return 0;
}
