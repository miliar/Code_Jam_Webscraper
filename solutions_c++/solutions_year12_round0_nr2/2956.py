#include <iostream>
#include <algorithm> 
#include <vector>
#include <cstdio> 

using namespace std; 

#define REP(i, to) for(int i=0; i<to; i++)
typedef long long int LLI;

int main()
{
  int T;
  int N, S, P;
  cin >> T;
  
  for(int c=1; c<=T; c++){
    vector<int> G;
    cin >> N >> S >> P;
    REP(i, N){
      int x;
      cin >> x;
      G.push_back(x);
    }
    sort(G.begin(), G.end(), greater<int>()); 
    int result = 0;
    REP(i, G.size()){
      if(G[i] >= 3*P - 2) result++;
      else if(P>1 && G[i] >= 3*P - 4 && S>0) {
        S--;
        result++;
      }
    }
    cout << "Case #"<<c <<": " << result << endl;
  }
	return 0;
}
