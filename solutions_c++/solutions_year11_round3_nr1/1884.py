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

ifstream fin("I://fin.txt");
ofstream fout("I://out.txt");

void solve(){
	int h,w;
	vector <vector <char> > field;


	fin >> h >> w;
	field.resize(h);

	REP(i,h){
		field[i].resize(w);
		REP(q,w){
			fin >> field[i][q];
		}
	}
	int bad;
	REP(i,h){
		REP(q,w){
			if(field[i][q]=='#'){
				bad=0;
				if(i==h-1)bad=1;
				if(q==w-1)bad=1;
				if(bad){
					fout << "Impossible\n";
					return;
				}
				if(field[i+1][q]!='#')bad=1;
				if(field[i+1][q+1]!='#')bad=1;
				if(field[i][q+1]!='#')bad=1;
				if(bad){
					fout << "Impossible\n";
					return;
				}
				
				field[i][q]='/';
				field[i+1][q]='\\';
				field[i][q+1]='\\';
				field[i+1][q+1]='/';
				
			}
		}
	}

	REP(i,h){
		REP(q,w){
			fout << field[i][q];
		}
		fout << endl;
	}
}


int main(int argc, char *argv[])
{
    int t;

    fin >> t;
	



    REP(i,t){
cout << i+1 << " / " << t << "..." << endl;
        fout << "Case #" << i+1 << ": " << endl;
        solve();
        fout << endl;
    }
    
    fin.close();
    fout.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}