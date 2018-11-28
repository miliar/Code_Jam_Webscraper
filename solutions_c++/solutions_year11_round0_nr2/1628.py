#include <iostream>
#include <string>
#include <vector>
using namespace std;

void init(vector<pair<int, int> >& flag)
{
  for (unsigned int i = 0; i < flag.size(); ++i)
    flag[i].first = flag[i].second = 0;
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t < T+1; ++t) {

    int C;
    cin >> C;
    vector<string> c(C);
    for (int i = 0; i < C; ++i)
      cin >> c[i];

    int D;
    cin >> D;
    vector<string> d(D);
    vector<pair<int, int> > flag(D);
    for (int i = 0; i < D; ++i) {
      cin >> d[i];
      flag[i].first = flag[i].second = 0;
    }

    int N;
    cin >> N;
    string n;
    cin >> n;

    vector<char> ans;
    for (unsigned int i = 0; i < n.size(); ++i) {
      bool change = false;
      if (!ans.empty()) {
	char prev = '\0';
	int back = ans.size()-1;
	for (unsigned int j = 0; j < c.size(); ++j) {
	  if ((ans[back] == c[j][0] && n[i] == c[j][1]) ||
	      (ans[back] == c[j][1] && n[i] == c[j][0])) {
	    prev = ans[back];
	    ans[back] = c[j][2];
	    change = true;
	    break;
	  }
	}
	if (change) {
	  for (unsigned int j = 0; j < d.size(); ++j) {
	    if (d[j][0] == prev)
	      flag[j].first -= 1;
	    else if (d[j][1] == prev)
	      flag[j].second -= 1;
	  }
	}
      }
      if (!change) {
	for (unsigned int j = 0; j < d.size(); ++j) {
	  if (n[i] == d[j][0])
	    flag[j].first += 1;
	  else if (n[i] == d[j][1])
	    flag[j].second += 1;
	}

	bool del = false;
	for (unsigned int j = 0; j < flag.size(); ++j) {
	  if (flag[j].first > 0 && flag[j].second > 0) {
	    del = true;
	    break;
	  }
	}

	if (del) {
	  ans.clear();
	  init(flag);
	} else {
	  ans.push_back(n[i]);
	}
      }
    }

    cout << "Case #" << t << ": [";
    if (!ans.empty()) {
      cout << ans[0];
      for (unsigned int i = 1; i < ans.size(); ++i)
	cout << ", " << ans[i];
    }
    cout << "]" << endl;
  }
  return 0;
}
