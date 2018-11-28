#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>

#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>

#define REP(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(__typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SIZE(x)   (int)(x).size()
#define SORT(x) sort(ALL(x))
using namespace std;
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
int N, arr[1010];
int dp[111][1010];
int S;
int back(int ind, int place){
	if( place == N ) return 0;
	int & res = dp[ind][place];
	if( res >= 0 ) return res;
	res = 1000000;
	if( ind == arr[place] ){
		for(int i = 1;  i <= S ; i++)if( i != ind ){
			res = min ( res, back(i,place+1) + 1 );
		}
	}else res = back(ind,place+1);
	return res;
}
int main(){
	int i,j ,k;
	string s;
	map<string,int> ind;
	int indice = 0;
	int casos; cin >> casos;
	for(int h = 0 ; h < casos ; h ++ ){
		ind.clear(), indice = 1;
		memset(dp , -1, sizeof(dp));
		cin >> S;
		while( getchar() != '\n');
		REP(i, S){
			getline(cin, s);
			if( ind[s] == 0 ){
				ind[s] = indice++;
			}
		}
		cin >> N;
		char c;
		while((c=getchar()) != '\n' && c != EOF);
		REP(i, N){
			getline(cin,s);
			arr[i] = ind[s];
		}
		printf("Case #%i: ", h+1);
		if( N )printf("%i\n", back(arr[0],0)-1);
		else printf("0\n");
	}return 0;
}
