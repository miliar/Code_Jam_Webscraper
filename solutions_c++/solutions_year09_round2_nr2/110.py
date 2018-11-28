#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int main()
{
  int i, sc, T;
  string N;
  cin >> T;
  for(sc = 1; sc <= T; ++sc) {
    cin >> N;
    if(next_permutation(N.begin(), N.end())) {
      cout << "Case #" << sc << ": " << N << endl;
    } else {
      int ct[10] = {0};
      string res = "";
      for(i=0; i<N.length(); ++i)
	ct[N[i]-'0']++;
      for(i=1; i<=9; ++i) {
	if(ct[i] != 0) {
	  res += (char)(i + '0');
	  ct[i]--;
	  break;
	}
      }
      for(int j=0; j<=ct[0]; ++j)
	res += "0";
      for(; i<=9; ++i) {
	while(ct[i] > 0) {
	  res += (char)(i + '0'); 
	  ct[i]--;
	}
      }
      cout << "Case #" << sc << ": " << res << endl;
    }
  }
  return 0;
}
