// ============================================================================
//   [ Filename    ]  pb.cpp
//   [ Description ]  
//   [ Created     ]  西元2011年05月07日 13時23分55秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

class Sol
{
public:
   Sol() {
      memset(trans_, 0, sizeof(trans_));
      memset(oppos_, 0, sizeof(oppos_));
   }
   void read() {
      int n;
      char str[10];
      cin >> n;
      for (int i = 0; i < n; ++i) {
         cin >> str;
         trans_[str[0]][str[1]] = trans_[str[1]][str[0]] = str[2];
      }
      cin >> n;
      for (int i = 0; i < n; ++i) {
         cin >> str;
         oppos_[str[0]][str[1]] = oppos_[str[1]][str[0]] = true;
      }
      cin >> n >> input_;
   }
   void append(char x) {
      if (seq_.empty()) {
         seq_.push_back(x);
         return;
      }
      char last = seq_.back();
      if (trans_[x][last]) {
         seq_.pop_back();
         seq_.push_back(trans_[x][last]);
      }
      else {
         seq_.push_back(x);
         for (int i = 0; i < seq_.size()-1; ++i)
            if (oppos_[x][seq_[i]]) {
               seq_.clear();
               break;
            }
      }
   }
   void solve(int caseNo) {
      read();
      for (string::iterator it = input_.begin(); it != input_.end(); ++it)
         append(*it);
      cout << "Case #" << caseNo << ": [";
      if (seq_.empty()) {
         cout << "]" << endl;
         return;
      }
      cout << seq_[0];
      for (int i = 1; i < seq_.size(); ++i)
         cout << ", " << seq_[i];
      cout << "]" << endl;
   }
private:
   char trans_[256][256];
   bool oppos_[256][256];
   vector<char> seq_;
   string input_;
};

int main()
{
   int N;
   cin >> N;
   for (int i = 1; i <= N; ++i) {
      Sol s;
      s.solve(i);
   }
   return 0;
}
