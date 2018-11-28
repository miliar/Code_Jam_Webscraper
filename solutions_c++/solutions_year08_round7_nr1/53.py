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
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
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
#define MM 11011
vector<int> edges[MM];
int dp[MM];
int back(int mix){
	int i,j ,k;
	int & res = dp[mix];
	if(res >= 0 ) return res;
	res = 0;
	vector<int> aux;
	REP(i, edges[mix].size()){
		aux.PB(back(edges[mix][i]));
	}
	sort(aux.begin(), aux.end());
	reverse(aux.begin(), aux.end());
	int p = 0;
	REP(i, aux.size()){
		res = max( res, aux[i] + p  );
		if( aux[i] != 0 ) p++;
	}
// 	printf("..%i\n", mix);
// 	REP(i, aux.size()) printf("%i  ", aux[i]);
// 	printf(" answ :  %i\n", res);
	res = max ( res, p + 1 );
	return res;
}
int main(){
	int i,j ,k;int casos;
	cin >> casos; // scanf("%i", &casos);
	for(int h = 0 ; h < casos; h ++ ){
		for(i=0;i<MM;i++) edges[i].clear();
		cout << "Case #"<<h+1<<": ";
		int N;
		
		cin >> N;
		map<string,int > indice; int ind = 1;
		memset(dp, -1, sizeof(dp));
		for(i=0;i<N;i++){
			
			string smix;
			cin >> smix;
			if( indice[smix] == 0 ) {
				indice[smix] = ind;
				ind++;
			}
			int mix = indice[smix];
			int cant;
			cin >> cant;
// 			cout << cant << endl;
// 			cout<< cant << endl;
			for(j=0;j<cant;j++){
				string s;
				cin >> s;
				
				if( indice[s] == 0 ) {
// 					cout << s << endl;
					indice[s] = ind;
					ind++;
				}
				int ss; 
				ss = indice[s];
				if(islower(s[0])){
					dp[ss] = 0;
				}edges[mix].PB(ss);
			}
		}
// 		for(int i=1;i<4;i++){
// 			REP(j, edges[i].size()) printf("%i ", edges[i][j]);
// 			printf("\n");
// 		}
		cout <<back(1) << endl;
	}
	return 0;
}
