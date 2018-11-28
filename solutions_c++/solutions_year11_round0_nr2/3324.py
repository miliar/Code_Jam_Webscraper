#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)

ifstream fin("C:\\Users\\Администратор\\Downloads\\B-large.in");

string solve(){
	map < string,char > inv,opp;
	string ts;

	int c;
	char c1,c2,c3;
	fin >> c;
	REP(i,c){
		fin >> ts;
		c1=ts[0];
		c2=ts[1];
		c3=ts[2];
		if(c1>c2){
			ts[0]=c2;
			ts[1]=c1;
		}
		ts.resize(2);
		inv[ts]=c3;
	}

	int d;
	fin >> d;
	REP(i,d){
		fin >> ts;
		c1=ts[0];
		c2=ts[1];
		if(c1>c2){
			ts[0]=c2;
			ts[1]=c1;
		}
		opp[ts]=1;
	}

	fin >> d;
	fin >> ts;

	string ret,qq;
	ret="";

	int i;
	i=0;
	int r;
	qq="  ";
	while(i<ts.size()){
		ret+=ts[i];

		r=ret.size();
		if(r>1){
			c1=ret[r-1];
			c2=ret[r-2];
			
			if(c1<c2){
				qq[0]=c1;
				qq[1]=c2;
			} else {
				qq[0]=c2;
				qq[1]=c1;
			}

			if(inv.find(qq)!=inv.end()) {
				c1=inv[qq];
				ret[r-2]=c1;
				ret.resize(r-1);
			}

			r=ret.size();

			REP(q,r-1){
				FOR(w,q+1,r-1){
					if(w==q)continue;
					c1=ret[q];
					c2=ret[w];

					if(c1<c2){
						qq[0]=c1;
						qq[1]=c2;
					} else {
						qq[0]=c2;
						qq[1]=c1;
					}

					if(opp[qq]==1){
						ret = "";
						q=r;
						break;
					}
				}
			}
		}

		i++;
	}


	return ret;
}

int main(){
	int T;
	string sol;
	ofstream fout("I:\\GCJ-Q-B.txt");

	fin >> T;
	cout << T << endl;
	REP(i,T){
		sol = solve();
		fout << "Case #" << i+1 << ": [";
		REP(i,sol.size()-1){
			fout << sol[i] << ", ";
		}
		if(sol.size()>0) fout << sol[sol.size()-1];
		fout << "]" << endl;
	}

	fin.close();
	fout.close();

	system("pause");
	return 0;
}