#include<string>
#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>

using namespace std;

int main () {
	freopen("perm.in", "rt", stdin);
	freopen("perm.out", "wt", stdout);
	
	int N, k;
	cin >> N;
	string orig;
	vector<int> perm;
	
	for(int tt=1; tt <= N; tt++) {
		perm.clear();
		
		cin >> k;
		cin >> orig;
		
		for(int pp=0; pp<k; pp++)
			perm.push_back(pp);
		
		int best = 1000000000;
		
		do {
			int cur = 0;
			string out = "";
			int omg=perm.size();
		/*	for(int bb=0; bb < perm.size(); bb++)
				cout << perm[bb] << " " << flush;*/
			for(int y=0; y < orig.size()/k; y++)
				for(int x=0; x <k;x++) {
					out += orig[y*k + perm[x]];
				}
			char last = out[0]; 
			cur = 1;
			for(int o=1; o < out.size();o++) {
				if (out[o] == last)
					continue;
				cur++;
				last = out[o];
			}
			best = min(best, cur);
			
		} while(next_permutation(perm.begin(), perm.end()));
		
		cout << "Case #"<<tt<<": "<<best<<endl;
	}
	
	
	return 0;
}
