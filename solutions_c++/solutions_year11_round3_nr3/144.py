#include <iostream>
using namespace std;
typedef long long LL;
int main() {
    int T;
    cin >> T;
    for(int z=1; z<=T; z++) {
        int N;
        LL L,H;
        cin >> N >> L >> H;
        vector<LL> notes;
        while(N--) {
	  LL x;
	  cin >> x;
	  notes.PB(x);
        }
        sort(notes.begin(), notes.end());
        for(int i=0; i<=n; i++) {
	  LL nww_left = 1;
	  for(int j=0; j<i; j++)
	      nww_left = nww(nww_left, notes[j]);
	  
	  LL nwd_right = -1;
	  for(int j=i; j<n; j++) {
	      if(nwd_right == -1)
		nwd_right = notes[j];
	      else
		nwd_right = nwd(nwd_right, notes[j]);
	  }
	  
	  LL actL = truL(L, nww_left);
	  LL actR = truR(R, nww_right);
	  
        }
        
    }
    return 0;
}