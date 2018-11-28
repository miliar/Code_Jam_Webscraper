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

#define forn(i, n) for(int i=0;i<int(n);i++)
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
typedef long long ll;

int N, M, n, m;


vector<int> back(int ind, int K){
// 	printf("%i %i\n", ind, K);
	if( ind == K ){
		vector<int> vec; vec.push_back(ind); return vec;
	}
	vector<int> vec = back(ind+1,K);
	int mov = ((ind-1) % (vec.size()+1) );
// 	printf("  %i\n", mov);
	vector<int> res;
	int i, j,k;
	for(i=(int)vec.size()-mov;i<vec.size();i++) res.PB(vec[i]);
	res.PB(ind);
	for(i=0;i<(int)vec.size()-mov;i++)res.PB(vec[i]);
	return res;
}





int main(){
	int i,j ,k, casos;
	scanf("%i", &casos);
// 	printf("HOLfasdf\n");
	for(int h = 0 ;h  < casos ; h ++ ){
// 		printf("HOLA\n");
		int K;
		scanf("%i", &K);
		while(getchar()!='\n');
		vector<int>  vec = back(1,K);
		int cant;scanf("%i", &cant);
// 		string s;
// 		getline(cin,s);
// 		istringstream iss( s );
		printf("Case #%i:", h+1);
		for(i=0;i<cant;i++){
			scanf("%i", &k);
			printf(" %i", vec[k-1]);
		}printf("\n");
	}
	return 0;
}





































