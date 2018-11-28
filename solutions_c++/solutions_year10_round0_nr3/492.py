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
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

class GCJ {
public:
	ll solve(int R, int k, int N, vector <int> g) {
		ll result=0;
		int rotb, rote, cur=0, next;
		ll euro[1001], teuro, reuro=0;
		int calced[1001];
		
		memset(calced, -1, sizeof(calced));
		for(int i=0; i<=1000; i++) {
			if(calced[cur]>=0) {
				rotb=calced[cur]; rote=i; break;
			}
			next=cur;
			teuro=0;
			for(int j=0; j<N; j++) {
				if(teuro+g[next]<=k) {
					teuro+=g[next];
					next=(next+1)%N;
				} else break;
			}
			euro[i]=teuro;
			calced[cur]=i;
			cur=next;
		}
		for(int i=rotb; i<rote; i++) {
			reuro+=euro[i];
		}

		for(int i=0; i<min(rotb, R); i++) {
			result+=euro[i];
		}
		if(R<=rotb) return result;
		R-=rotb;
		result+=R/(rote-rotb)*reuro;
		R=R%(rote-rotb);
		for(int i=0; i<R; i++) {
			result+=euro[rotb+i];
		}

		return result;
	}
};

int main() {
	string prb[12];
	ofstream ofs("output.txt");
	string s, filename;
	char key;
	int n, R, k, N;
	vector <int> g;
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
		ifs >> R; ifs >> k; ifs >> N;
		g.clear(); g.assign(N, 0);
		for(int j=0; j<N; j++) {
			ifs >> g[j];
		}
		ofs << "Case #" << i << ": " << gcj.solve(R, k, N, g) << endl;
	}
}
