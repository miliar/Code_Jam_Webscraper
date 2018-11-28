#define _USE_MATH_DEFINES
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <list>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <numeric>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <stack>
#include <queue>
#include <NTL/ZZ.h>
using namespace std;
using namespace NTL;
static const double EPS = 1e-5;
typedef long long ll;

class GCJ {
public:
	bool ifw(vector <string> vs, int N, int K, int r, int c, char C) {
		int dr[4]={1,1,0,1}, dc[4]={0,1,1,-1}, nr, nc;
		bool flag;

		if(vs[r][c]!=C) return false;
		for(int i=0; i<4; i++) {
			nr=r; nc=c;
			flag=true;
			for(int j=1; j<K; j++) {
				nr+=dr[i]; nc+=dc[i];
				if(nr<0 || nr>=N || nc<0 || nc>=N || vs[nr][nc]!=C) {
					flag=false;
					break;
				}
			}
			if(flag) return true;
		}
		return false;
	}

	string solve(int N, int K, vector <string> vs) {
		string result;
		bool b=false, r=false;
		
		for(int i=0; i<N; i++) {
			reverse(vs[i].begin(), vs[i].end());
		}
		for(int i=0; i<N; i++) {
			for(int j=1; j<N; j++) {
				if((vs[i][j]=='R' || vs[i][j]=='B') && vs[i][j-1]=='.') {
					int idx=j-1;
					while(idx>0) {
						if(vs[i][idx-1]=='.') idx--;
						else break;
					}
					swap(vs[i][idx], vs[i][j]);
				}
			}
		}

		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if(ifw(vs, N, K, i, j, 'B')) b=true;
				if(ifw(vs, N, K, i, j, 'R')) r=true;
			}
		}

		if(r && b) result="Both";
		else if(r && !b) result="Red";
		else if(!r && b) result="Blue";
		else result="Neither";

		return result;
	}
};

int main() {
	string prb[12];
	ofstream ofs("output.txt");
	string s, filename;
	char key;
	int n, N, K;
	vector <string> vs;
	GCJ gcj;

	for(int i=0; i<12; i++) {
		prb[i].push_back('A'+i/2);
		if(i%2) prb[i]+="-large";
		else prb[i]+="-small-attempt";
		prb[i]+=".in.txt";
		cout << (char)('a'+i) << ". " << prb[i] << endl;
	}
	do {
		cout << "Choose the input file." << endl;
		cin >> key;
	} while(key-'a'<0 || key-'a'>=12);
	filename=prb[key-'a'];
	if((key-'a'+1)&1) {
		do {
			cout << "Choose number of attempt times." << endl;
			cin >> key;
		} while(key-'0'<0 || key-'9'>0);
		filename.insert(15, 1, key);
	}
	cout << "Filename is " << filename << endl;
	ifstream ifs(filename.c_str());

	ifs >> n; ifs.ignore();
	for(int i=1; i<=n; i++) {
		ifs >> N >> K; ifs.ignore();
		vs.resize(N);
		for(int j=0; j<N; j++) {
			getline(ifs, vs[j]);
		}
		ofs << "Case #" << i << ": " << gcj.solve(N, K, vs) << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)