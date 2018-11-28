#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main() {
  int NTests;
  cin >> NTests;
  for (int test=0;test<NTests;test++) {
    vector<vector<bool> > is_combine('Z'-'A'+1,vector<bool>('Z'-'A'+1,false));
    vector<vector<char> > combine('Z'-'A'+1,vector<char>('Z'-'A'+1,' '));
    vector<vector<bool> > is_negate('Z'-'A'+1,vector<bool>('Z'-'A'+1,false));
    vector<char> res;
    int C;
    cin >> C;
    for (int i=0;i<C;i++) {
      char a,b,c;
      cin >> a >> b >> c;
      is_combine[a-'A'][b-'A'] = is_combine[b-'A'][a-'A'] = true;
      combine[a-'A'][b-'A'] = combine[b-'A'][a-'A'] = c;
    }
    int D;
    cin >> D;
    for (int i=0;i<D;i++) {
      char a,b;
      cin >> a >> b;
      is_negate[a-'A'][b-'A'] = is_negate[b-'A'][a-'A'] = true;
    }
    int N;
    cin >> N;
    for (int i=0;i<N;i++) {
      char cur;
      cin >> cur;
      if (res.empty()) {
	res.push_back(cur);
	continue;
      }
      if (is_combine[res[res.size()-1]-'A'][cur-'A']) {
	char push_ = combine[res[res.size()-1]-'A'][cur-'A'];
	res.pop_back();
	res.push_back(push_);
	continue;
      }
      bool fl = false;
      for (int j=0;j<res.size();j++) {
	if (is_negate[res[j]-'A'][cur-'A']) {
	  res.clear();
	  fl = true;
	  break;
	}
      }
      if (fl) continue;
      res.push_back(cur);
    }
    cout << "Case #" << test+1 << ": [";
    if (res.size()!=0)
      for (int i=0;i<res.size()-1;i++)
	cout << res[i] << ", ";
    if (res.size()!=0)
      cout << res[res.size()-1];
    cout << "]" << endl;
  }
  return 0;
}
