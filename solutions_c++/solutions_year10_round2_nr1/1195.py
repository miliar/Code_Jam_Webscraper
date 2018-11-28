#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <numeric>
#include <fstream>

using namespace std;
#define ALL(c) c.begin(), c.end()
#define pb push_back
#define lg length
#define sz size
#define forn(i,n) for(i=0;i<n;i++)
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

map <string,bool> dir;
vector <string> v;
int rta;

void crear_dir(int k, int current) {
	int j;
	if(!dir[v[current].substr(0,k)]) {
		// Buscar padre:
		j = k-1;
		while(j>=0 && v[current][j]!='/') j--;
		// Ver si el padre existe:
		if(j!=0 && !dir[v[current].substr(0,j)]) {
			crear_dir(j,current);	
		}
		dir[v[current].substr(0,k)] = true;
		rta++;
	}
}
main () {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int T,N,M;
	int t,i,j;

	fin>>T;
	for(t=1;t<=T;t++) {
		// Init:
		rta = 0;
		dir.clear();
		v.clear();
		// Read:
		fin>>N>>M;
		fin.get();
		for(i=0;i<N;i++) {
			char temp[200];
			fin.getline(temp,200,'\n');
			dir[temp] = true;
		}
		for(i=0;i<M;i++) {
			char temp[200];
			fin.getline(temp,200,'\n');
			v.push_back(temp);
		}
		// Algoritmo:
		dir["/"] = true;
		sort(ALL(v));
		for(i=0;i<M;i++) {
			crear_dir(v[i].length(),i);
		}
		// output:
		fout<<"Case #"<<t<<": "<<rta<<endl;
	}
return 0;	
}
