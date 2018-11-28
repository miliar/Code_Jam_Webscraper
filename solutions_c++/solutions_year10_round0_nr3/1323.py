#include<iostream>
#include<algorithm>
#include<vector>
#include<numeric>

using namespace std;

int main() {
  vector <vector <long> > rounds;
  vector <long> trip_amount, groups;
  int T, N;
  long R, k, g;
  cin >> T;
  for (int t=1; t<=T; t++) {
    cin >> R >> k >> N;
    rounds.clear(); trip_amount.clear(); groups.clear();
    for (int i=0; i<N; i++) {
      cin >> g;
      groups.push_back(g);
    }
    int r=0;
    long offset=-1, amount=0;
    while (r<R) {
      r++;
      rounds.push_back(groups);
      int i=0;
      long filled=0;
      while(i<N && ((filled+groups[i]) <= k)) {
        filled+=groups[i];
        i++;
      }
      trip_amount.push_back(filled);
      rotate(groups.begin(), groups.begin()+i, groups.end());
      for (int j=0; j<rounds.size(); j++) if (rounds[j]==groups) offset=j;
      if (offset >= 0) break;
    }
    offset=max((long)0,offset);
    amount += accumulate(trip_amount.begin(), trip_amount.begin()+offset,0);
    amount += ((R-offset)/(rounds.size()-offset))* \
        accumulate(trip_amount.begin()+offset, trip_amount.end(), 0);
    amount += accumulate(trip_amount.begin()+offset, trip_amount.begin()+ \
        ((R-offset)%(rounds.size()-offset)) + offset,0);
    cout << "Case #" << t << ": " << amount << endl;
  }
}
