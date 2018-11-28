
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

void nbtrain(int T, vector<pair<int, int> > VA, vector<pair<int, int> > VB) {

  map<int, int> A, B;

  for(int i = 0; i < VA.size(); i++) {
    A[VA[i].first]--;
    B[VA[i].second + T]++;
  }
  for(int i = 0; i < VB.size(); i++) {
    B[VB[i].first]--;
    A[VB[i].second + T]++;
  }
  int Ma = 0, Mb = 0;

  int N = 0;
  for(map<int, int>::iterator it = A.begin(); it != A.end(); ++it) {
    N += it->second;
    if(N < Ma) Ma = N;
  }

  N = 0;
  for(map<int, int>::iterator it = B.begin(); it != B.end(); ++it) {
    N += it->second;
    if(N < Mb) Mb = N;
  }

  cout << -Ma << " " << -Mb << endl;
}

int main() {
  int N;
  cin >> N;
  for(int i = 1; i <= N; i++) {
    int T, NA, NB;
    cin >> T >> NA >> NB;
    vector<pair<int, int> > VA, VB;

    string tmp;
    getline(cin, tmp);
    for(int k = 0; k < NA; k++) {
      getline(cin, tmp);
      int start = (tmp[0]-'0') * 600 + (tmp[1]-'0') * 60 + (tmp[3]-'0') * 10 + (tmp[4]-'0');
      int end = (tmp[6]-'0') * 600 + (tmp[7]-'0') * 60 + (tmp[9]-'0') * 10 + (tmp[10]-'0');
      VA.push_back(pair<int, int>(start, end));
    }
    for(int k = 0; k < NB; k++) {
      getline(cin, tmp);
      int start = (tmp[0]-'0') * 600 + (tmp[1]-'0') * 60 + (tmp[3]-'0') * 10 + (tmp[4]-'0');
      int end = (tmp[6]-'0') * 600 + (tmp[7]-'0') * 60 + (tmp[9]-'0') * 10 + (tmp[10]-'0');
      VB.push_back(pair<int, int>(start, end));
    }

    cout << "Case #" << i << ": ";
    nbtrain(T, VA, VB);

  }
}
