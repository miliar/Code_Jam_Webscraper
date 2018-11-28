#include<iostream>
#include<algorithm>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<cassert>
#include<numeric>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<deque>
#include <algorithm>
#include <string>
#include <vector>
#include <ctype.h>
#include <math.h>


using namespace std;


typedef long long ll;

typedef long long int64;
typedef long double double64;
typedef unsigned long long uint64;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)


using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int L,D,N;
	string input[5000];
	cin >> L >> D >> N;

	FOR(i,D){
		cin >> input[i];
	}
	FOR(i, N){
		vector<char> pattern[15];
		string inStr;
		cin >> inStr;
		bool isOR = false;
		int count=0;
		FOR(j, inStr.size()){
			if( inStr[j] == '(' ) isOR = true;
			else if( inStr[j] == ')' ){ isOR = false; count++; }
			else { 
				pattern[count].push_back(inStr[j]);
				if(!isOR) count++;
			}
		}
		
		int solve = 0;
		FOR(k,D){
			bool isMatch = true;
			FOR(m, L){
				bool isIn = false;
				FOR(n, pattern[m].size()){
					if(pattern[m][n] == input[k][m]){
						isIn = true;
						break;
					}
				}
				if( isIn != true ){
					isMatch = false;
					break;
				}
			}
			if(isMatch) solve++;
		}
		cout << "Case #" << i+1 << ": " << solve << endl;
	}
	return 0;
}
