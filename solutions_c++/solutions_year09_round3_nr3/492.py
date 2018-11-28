#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <list>
#include <map>
#include <set>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
using namespace std;
#define REP(i,a,b) for(i=a;i<b;++i)
#define rep(i,n) REP(i,0,n)


int nTestCase, testCase;
int i, j, k, l;
long int ans, tmpAns;
int arrP[102];
vector<int> arrQ;
int P, Q, p, q;
long long int fact[6];

int main(){
	fact[0] = 1;
	REP(i,1,5+1){
		fact[i] = i*fact[i-1];
	}
	cin >> nTestCase;
	//getline(cin, str);
	for(testCase=0; testCase<nTestCase; ++testCase){
		cin >> P;
		cin >> Q;
		ans = 0;
		arrQ.clear();
		rep(i,Q){
			cin >> l;
			arrQ.push_back(l);
		}
		rep(j, fact[Q]){
			REP(i,1,P+1){
				arrP[i] = 0;
			}
			arrP[0] = arrP[P+1] = 1;

			tmpAns = 0;
			rep(i,Q){
				arrP[arrQ[i]] = 1;
				int q1 = arrQ[i]-1;
				while(!arrP[q1]){
					++tmpAns;
					--q1;
				}
				q1 = arrQ[i]+1;
				while(!arrP[q1]){
					++tmpAns;
					++q1;
				}
			}
			if(j == 0)
				ans = tmpAns;
			else if(tmpAns < ans)
				ans = tmpAns;
			next_permutation(arrQ.begin(), arrQ.end());
		}
		cout << "Case #" << testCase+1 << ": " << ans << endl;
	}

	return 0;
}
