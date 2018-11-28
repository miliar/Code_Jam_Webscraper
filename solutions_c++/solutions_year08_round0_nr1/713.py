#include <cstdio>
#include <vector>
#include <sstream>
#include <fstream>
#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>



using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FRR(i,a,b) for(int i=b-1;i>=0;i--)
#define VI vector<int>
#define VVI vector< VI >
#define VS vector<string>
#define INF 2000000000
#define sz size()
#define pb push_back
#define mp make_pair
#define ll long long int
#define print(v,n) {FOR(i,0,n)cout<<v[i]<<" ";}cout<<endl;

int queries[1010]; 
int n;
int q;
int fc[110][1010];

int f(int s, int k){
	if(fc[s][k]!=-1)return fc[s][k];
	if(k >= q)return 0;
	if(queries[k] != s)return fc[s][k]  = f(s, k + 1);
	fc[s][k] = INF;
	FOR(i,0,n)if(i != s)fc[s][k] <?= f(i, k+1) + 1;
	return fc[s][k];
}


int main(){
	int tests; scanf("%d", & tests);
	FOR(cases, 0, tests){
		scanf("%d", &n);char tmp[110];
		map<string, int> names;
		cin.getline(tmp, 110);
		FOR(i,0,n){
			cin.getline(tmp, 110);
			string str(tmp);
			names[str] = i;
		}
		int Q;
		scanf("%d", &Q);
		cin.getline(tmp, 110);
		q = 0;
		FOR(i,0,Q){
			cin.getline(tmp, 110);
			string str(tmp); 
			if(names.count(str))queries[q++] = names[str];
		}
		int ret = INF;
		//print(queries, q);
		memset(fc, -1, sizeof(fc));
		FOR(i,0,n)ret <?= f(i, 0);
		cout << "Case #" << cases + 1 <<": " << ret << endl;

	}
}


