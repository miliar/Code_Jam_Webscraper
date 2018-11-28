#include <iostream>
#include <vector>
#include <string>
#include <utility>
using namespace std;

typedef pair<int,int> frac;

void solve(vector< vector<int> >& schedule, vector<double>& ans) {
  /*for (int i =0; i< schedule.size(); i++) {
	for (int j =0; j< schedule[0].size(); j++) {
	  cout << schedule[i][j] << " ";
	}
	cout << endl;
	}*/
  size_t N = schedule.size();
  vector<double> wp(N, 0);
  vector< vector<double> > wpm(N, vector<double>(N, 0));
  vector<double> owp(N, 0);
  vector<double> oowp(N, 0);

  for (size_t i = 0; i < N; i++) {
	int win = 0;
	int total = 0;
	for (size_t j = 0; j < N; j++) {
	  if (schedule[i][j] == -1) continue;
	  win += schedule[i][j];
	  total++;
	}
	wp[i] = ((double) win / total);
	for (size_t k = 0; k < N; k++) {
	  if (schedule[i][k] == -1) continue;
	  wpm[i][k] = (win - schedule[i][k]) / (total - 1.0);
	}
  }
					  
  for (size_t i = 0; i < N; i++) {
	int count = 0;
	for (size_t j = 0; j < N; j++) {
	  if (schedule[i][j] == -1) continue;
	  owp[i] += wpm[j][i];
	  count++;
	}
	owp[i] /= count;
  }

  for (size_t i = 0; i < N; i++) {
	int count = 0;
	for (size_t j = 0; j < N; j++) {
	  if (schedule[i][j] == -1) continue;
	  oowp[i] += owp[j];
	  count ++;
	}
	oowp[i] /= count;
  }
  for (size_t i = 0; i < N; i++) {
	ans[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
  }


  return;
}


int main() {
  int T;
  cin >> T;
  
  for (int i = 0; i < T; i++) {
	int N;
	cin >> N;
	vector< vector<int> > schedule(N, vector<int>(N, -1));
	for (int j = 0; j < N; j++) {
	  string s;
	  cin >> s;
	  for (size_t k = 0; k < s.size(); k++) {
		if (s[k] == '0') schedule[j][k] = 0;
		if (s[k] == '1') schedule[j][k] = 1;
	  }
	}
	vector<double> ans(N, 0);
	solve(schedule, ans);
	cout << "Case #" << i + 1 << ":" << endl;
	for (size_t j = 0; j < ans.size(); j++) {
	  cout << ans[j] << endl;
	}
  }
  return 0;
}
	
