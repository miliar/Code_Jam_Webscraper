#include <iostream>
#include <fstream>

using namespace std;

int p, q;
int qi[101];
int pi[10001];
long int res;

void solve(int ind, int depth, long int resL) {
	//cout << "1 - depth: " << depth << ", indice: " << ind << ", resL: " << resL << "\n";
	pi[ind] = 1;
	int before = 0;
	int after = 0;
	if(depth == 0) {
		resL = p-1;
	} else {	
		for(int j=ind-1; j>=1; j--) {
			if(pi[j]==1)
				break;
			before++;
		}
		for(int j=ind+1; j<=p; j++) {
			if(pi[j]==1)
				break;
			after++;
		}
	}

	//cout << "2 - depth: " << depth << ", before: " << before << ", after: " << after << "\n";
	resL += before + after;

	if(depth>=q-1) {
		//cout << "res: " << res << ", resL: " << resL << "\n";
		if(resL < res)
			res = resL;
		pi[ind] = 0;
		return;
	}

	

	for(int i=0; i<q; i++) {
		if(pi[qi[i]]==0) {
			solve(qi[i], depth+1, resL);
		}
	}
	pi[ind] = 0;
}

int main() {
	int n;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C.out");

	fin >> n;
	for (int i = 0; i < n; i++) {
		res = 20000000L;
		fin >> p >> q;
		//cout << p << " " << q << "\n";
		for (int j = 0; j < q; j++) {
			fin >> qi[j];
		}
		for (int j = 0; j < q; j++) {
			for (int k=1; k<=p; k++)
				pi[k] = 0;
			solve(qi[j], 0, 0);
			
		}
		fout << "Case #" << i+1 << ": " << res << "\n";
	}
}
