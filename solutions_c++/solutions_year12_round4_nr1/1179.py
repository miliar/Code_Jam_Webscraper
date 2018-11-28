									/* in the name of Allah */
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <cstdio>
#include <cmath>
#include <map>

using namespace std;

ifstream fin("A_Swinging Wild.in");
ofstream fout("A_Swinging Wild.out");

#define cin fin
#define cout fout
#define P pair<double, double>
#define int64 long long

int n, D;
int d[10010], l[10010];
int c[10010];

int main(){
	int T, test = 0;
	for(cin >> T; T--; ){
		memset(c, -1, sizeof c);
		cin >> n;
		for(int i = 0; i < n; i++)
			cin >> d[i] >> l[i];
		cin >> D;
		string res = "NO";
		int p = 1;
		c[0] = 0;
		for(int i = 0; i < n; i++){
			if(c[i] == -1)
				break;
			int mx = d[i] + min(l[i], d[i] - c[i]);
			if(mx >= D)
				res = "YES";
			while(p < n && d[p] <= mx){
				c[p] = d[i];
				p++;
			}
		}
		cout << "Case #" << ++test << ": " << res << endl;
	}
	return 0;
}