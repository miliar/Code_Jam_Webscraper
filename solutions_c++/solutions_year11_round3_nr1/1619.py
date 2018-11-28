#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
//#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
using namespace std;

//ifstream cin("A-small-attempt0.in");
//ofstream cout("Asmall0.out");

ifstream cin("A-Large.in");
ofstream cout("A-Large.out");



int main(){
	int T;
	cin >> T;
	int R,C;
	for(int i=0;i<T;i++){
		cin >> R >> C;
		vector <string> vs;
		for(int j=0;j<R;j++){
			string s;
			cin >> s;
			vs.push_back(s);
		}
		bool yes = true;
		for(int j=0;j<R;j++){
			for(int k=0;k<C;k++){
				if(vs[j][k]=='#'){
					if(j==R-1) {yes = false; continue;};
					if(k==C-1) {yes = false; continue;}
					if(vs[j][k+1] != '#') {yes= false; continue;}
					if(vs[j+1][k+1] != '#'){yes = false; continue;}
					if(vs[j+1][k] != '#'){yes = false; continue;}
					vs[j][k] = '/';
					vs[j][k+1] = '\\';
					vs[j+1][k] = '\\';
					vs[j+1][k+1] = '/';
					
					
				}				
			}
		}
		cout << "Case #" << i+1 << ":" << endl;
		if(yes){
			
			for(int k=0;k<vs.size();k++){
				cout << vs[k] << endl;
			}
		}
		else
			cout << "Impossible" << endl;
	}
	system("pause");
	return 0;

}