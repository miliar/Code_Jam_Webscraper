#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
  int num_tests;
  cin >> num_tests;
  for (int test=0;test<num_tests;test++) {
    int n;
    cin >> n;
    vector<pair<int, int> > A; // owner, num
    for (int i=0;i<n;i++) {
      char c; int tmp;
      cin >> c >> tmp;
      A.push_back(make_pair(c=='O', tmp));
    }
    int curPos0 = 1, curPos1 = 1;
    int time0 = 0, time1 = 0;
    int res = 0;
    for (vector<pair<int,int> >::iterator cur_key = A.begin(); cur_key != A.end(); cur_key++) {
      if (!cur_key->first) {//0
	int time = abs(cur_key->second - curPos0) ;
	if (time > time0) 
	  res += time - time0+1;
	else 
	  res+=1;
	if (time > time0)
	  time1 += time-time0+1;
	else 
	  time1 += 1;
	time0 = 0;
	curPos0 = cur_key->second;
      } else { //1
	int time = abs(cur_key->second - curPos1) ;
	if (time > time1)
	  res += time - time1+1;
	else
	  res+=1;
	if (time > time1)
	  time0 += time-time1+1;
	else 
	  time0 += 1;
	time1 = 0;
	curPos1 = cur_key->second;
      }
    }
    cout << "Case #" << test+1 << ": ";
    cout << res << endl;
  }
  return 0;
}
