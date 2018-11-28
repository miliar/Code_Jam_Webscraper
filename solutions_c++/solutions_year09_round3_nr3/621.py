#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

int P_[10001];
int Q_[101];

int main(int argc, char *argv[]) {
 	
 	int N, Q, P, C = 0, q, i, j, l, resp, t;
 	
 	cin >> N;
 	while (N-- && ++C) {
		cin >> P >> Q;
		q = Q;
		l = 0;
		while (q--) {
			  cin >> Q_[l++];
  		}  
		resp = (1 << 31) - 1;
		  do {
		  	  memset(P_, -1, sizeof(P_));
		  	  t = 0;
		  	  for (i = 0; i < Q; i++) {
			  	  if (P_[Q_[i] - 1] == -1) {
				  	 	P_[Q_[i] - 1] = 0;	
						for (j = Q_[i] - 2; j >= 0 && P_[j] == -1; j--, t++);
						for (j = Q_[i]; j < P && P_[j] == -1; j++, t++);
			  	  }
			  }
			  //cout << "t: " << t << endl;
		  	  if (t < resp) {
			  	 	resp = t;
	  	 	  }
		  } while (next_permutation(Q_, Q_ + l));
		  cout << "Case #" << C << ": " << resp << endl;  
		  
  	}
 	return 0;
}
