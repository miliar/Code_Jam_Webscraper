#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)

using namespace std;

struct mytype{
	int t, idx;
	bool start;
	
	mytype(){
	}
	
	mytype(int _t, int _idx, bool _start){
		t = _t;
		idx = _idx;
		start = _start;
	}
	
	friend bool operator <(const mytype &a, const mytype &b){
		if (a.t == b.t)
			return !a.start && b.start;
		return a.t < b.t;
	}
};

int main(){
	int tests;
	ifstream fin("Bl.in");
	ofstream fout("Bl.out");
	fin >> tests;
	vector <mytype> lines;
	int turnt, na, nb;
	string tmp;
	ffor (test, 1, tests + 1){
		lines.clear();
		fin >> turnt;
		fin >> na >> nb;
		getline(fin, tmp);
		FOR (i, na){
			getline(fin, tmp);
			int h = (tmp[0] - '0') * 10 + tmp[1] - '0';
			h *= 60;
			int m = (tmp[3] - '0') * 10 + tmp[4] - '0';
			lines.pb(mytype(h + m, i, true));
			
			h = (tmp[6] - '0') * 10 + tmp[7] - '0';
			h *= 60;
			m = (tmp[9] - '0') * 10 + tmp[10] - '0';
			lines.pb(mytype(h + m + turnt, i, false));
		}

		FOR (i, nb){
			getline(fin, tmp);
			int h = (tmp[0] - '0') * 10 + tmp[1] - '0';
			h *= 60;
			int m = (tmp[3] - '0') * 10 + tmp[4] - '0';
			lines.pb(mytype(h + m, i + na, true));
			
			h = (tmp[6] - '0') * 10 + tmp[7] - '0';
			h *= 60;
			m = (tmp[9] - '0') * 10 + tmp[10] - '0';
			lines.pb(mytype(h + m + turnt, i + na, false));
		}
		sort(all(lines));
		int reta = 0, retb = 0, fa = 0, fb = 0;
		
		FOR (i, lines.sz){
			// begin of line
			if (lines[i].start){
				if (lines[i].idx < na){
					if (fa > 0)
						fa--;
					else
						reta++;
				}
				else{
					if (fb > 0)
						fb--;
					else
						retb++;
				}
			}
			else{
				if (lines[i].idx < na)
					fb++;
				else
					fa++;
			}
		}
		fout << "Case #" << test <<": " << reta << " " << retb << endl;
		cout << reta << " " << retb << endl;
	}
	system("pause");
	fin.close();
	return 0;
}
