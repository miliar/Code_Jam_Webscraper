#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;


void solve(vector< vector<int> >& combine, vector< vector<int> >& opposed, vector<int> n) {
  vector<int> ans;
  vector<int> flag(26, 0);
  size_t N = n.size();
  if (N == 0) {
	cout << "[]" << endl;
	return;
  }
  ans.push_back(n[0]);
  flag[n[0]]++;

  for(size_t i = 1; i < N; i++) {
	
	int tc = combine[ ans.back() ][ n[i] ];
	if (tc != -1) {
	  flag[ ans.back() ]--;
	  ans.pop_back();
	  ans.push_back(tc);
	  flag[ tc ] ++;
	  continue;
	}

	for (size_t j = 0; j < opposed[ n[i] ].size(); j++) {
	  if (flag[ opposed[ n[i] ][j] ] == 0) continue;

	  ans.clear();
	  for (size_t k = 0; k < flag.size(); k++) {
		flag[k] = 0;
	  }
	  if (i == N - 1) {
		cout << "[]" << endl;
		return;
	  }
	  i++;
	  ans.push_back(n[i]);
	  flag[n[i]]++;
	  goto LABEL;
	}
	ans.push_back(n[i]);
	flag[n[i]]++;
  LABEL:
	;
  }
  string prefix = "";
  cout << "[";
  for(size_t i = 0; i < ans.size(); i++) {
	cout << prefix << (char)('A' + ans[i]);
	prefix = ", ";
  }
  cout << "]" << endl;
  return;
}

int main() {
  int T = 0;
  cin >> T;
  for (int i = 0; i < T; i++) {
	int C, D, N;
	cin >> C;
	vector< vector<int> > combine(26, vector<int>(26, -1));
	vector< vector<int> > opposed(26);

	string n;
	for (int j = 0; j < C; j++) {
	  string s;
	  cin >> s;
	  combine[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
	  combine[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
	}
	cin >> D;
	for (int j = 0; j < D; j++) {
	  string s;
	  cin >> s;
	  opposed[s[0] - 'A'].push_back(s[1] - 'A');
	  opposed[s[1] - 'A'].push_back(s[0] - 'A');
	}
	cin >> N;
	cin >> n;
	vector<int> ns;
	for(size_t j = 0; j < n.size(); j++) {
	  ns.push_back(n[j] - 'A');
	}
	cout << "Case #" << i + 1 << ": ";
	solve(combine, opposed, ns);
  }
  return 0;
}
