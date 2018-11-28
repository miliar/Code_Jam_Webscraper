#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define bits(x) __builtin_popcount(x)

#define MAX 120

vector<string> tabla;
int tot[MAX];
double wp[MAX], o[MAX], oo[MAX];
double op[MAX][MAX];

int main(){
	int casos,cc,n;
	cin>>casos;
	
	for (cc=0;cc<casos;cc++) {
		printf("Case #%d:\n",cc+1);
		cin>>n;
		tabla.clear();
		string tmp;
		for (int i=0;i<n;i++) {
			cin>>tmp;
			tabla.push_back(tmp);
		}
		for (int i=0;i<n;i++) {
			tot[i]=0;
			wp[i]=0.0;
			for (int j=0;j<n;j++) {
				if (tabla[i][j]!='.') tot[i]++;
				if (tabla[i][j]=='1') wp[i]++;
			}
			wp[i]/=tot[i];
		}
		for (int i=0;i<n;i++) for (int j=0;j<n;j++) if (tabla[i][j]!='.'){
			op[i][j]=(wp[i]*tot[i]-(tabla[i][j]=='1'?1:0))/(tot[i]-1);
		}
		for (int i=0;i<n;i++) {
			o[i]=0.0;
			for (int j=0;j<n;j++) if (tabla[i][j]!='.') {
				o[i]+=op[j][i];
			}
			o[i]/=tot[i];
		}
		for (int i=0;i<n;i++) {
			oo[i]=0.0;
			for (int j=0;j<n;j++) if (tabla[i][j]!='.') {
				oo[i]+=o[j];
			}
			oo[i]/=tot[i];
		}
		for (int i=0;i<n;i++) {
			printf("%.9f\n",wp[i]/4+o[i]/2+oo[i]/4);
		}
	}
	return 0;
}
