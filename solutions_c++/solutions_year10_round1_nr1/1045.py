#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()

bool busca(vector<string> A, string cad) {
	int n = A.S , m = A[0].S;
	for (int a=0;a<n;a++)
		for (int d=-1;d<=1;d++)
			for (int b=0;b<m;b++)
				for (int e=-1;e<=1;e++) {
					if (d==0 && e==0) continue;
					int x=a, y=b;
					string value = "";
					while (x>=0 && x<n && y>=0 && y<m) {
						value = value + A[x][y];
						if (value == cad) {
							return true;
						}
						x+=d;
						y+=e;
					}
				}
	return false;
	
}

string solve(vector<string> v, int k) {
	F(i, v.S) {
		string aux ="";
		F(j, v[0].S) {
			if (v[i][j] != '.')
				aux = aux + v[i][j];
			else
				aux = "." + aux;
		}
		v[i] = aux;
	}
	string s1(k, 'R'), s2(k, 'B');
	if(busca(v,s1)){
		if(busca(v,s2))
			return "Both";
		else
			return "Red";
	}
	else{
		if(busca(v,s2))
			return "Blue";
		else
			return "Neither";
	}
}

int main() {
//	freopen("a.in", "r", stdin);
//	freopen("C:/Users/vudduu/Downloads/A-small-attempt0.in", "r", stdin);
//	freopen("C:/Users/vudduu/Downloads/A-small-attempt0.out", "w", stdout);
	freopen("C:/Users/vudduu/Downloads/A-large.in", "r", stdin);
	freopen("C:/Users/vudduu/Downloads/A-large.out", "w", stdout);
	int NN;
	scanf("%d", &NN);
	for (int caso=1; caso<=NN ;caso++) {
		printf("Case #%d: ", caso);
		int N, K;
		scanf("%d %d", &N, &K);
		vector<string> v(N);
		F(i, N)
			cin>>v[i];
		cout<<solve(v, K)<<endl;
	}
}
