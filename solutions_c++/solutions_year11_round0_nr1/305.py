// ============================================================================
//   [ Filename    ]  pa.cpp
//   [ Description ]  
//   [ Created     ]  西元2011年05月07日 12時57分10秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>
#include <vector>

using namespace std;

class Sol
{
public:
   Sol():time_(0) {
      pos_[0] = pos_[1] = 1;
      lastMove_[0] = lastMove_[1] = 0;
   }
   void read()
   {
      int n;
      cin >> n;
      while (n--) {
         char x[3];
         int pos;
         cin >> x >> pos;
         seq_.push_back(make_pair((x[0] == 'O' ? 0 : 1), pos));
      }
   }
   void move(int idx, int to) {
      int diff = to - pos_[idx];
      if (diff < 0)
         diff = -diff;
      if (diff <= time_ - lastMove_[idx]) {
         pos_[idx] = to;
         lastMove_[idx] += diff;
      }
      else {
         time_ = lastMove_[idx] + diff;
         lastMove_[idx] = time_;
         pos_[idx] = to;
      }
   }
   void solve(int caseNo) {
      read();
      for (int i = 0; i < seq_.size(); ++i) {
         int idx = seq_[i].first;
         int pos = seq_[i].second;
         move(idx, pos);
         time_++;
         lastMove_[idx] = time_;
      }
      cout << "Case #" << caseNo << ": " << time_ << endl;
   }
private:
   vector<pair<int,int> > seq_;
   int time_;
   int pos_[2];
   int lastMove_[2];
};

int main() {
   int N;
   cin >> N;
   for (int i = 1; i <= N; ++i) {
      Sol s;
      s.solve(i);
   }
   return 0;
}
