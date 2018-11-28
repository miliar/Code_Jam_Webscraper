#include <iostream>

using namespace std;

main(){
  int T;
  cin >> T;

  for(int t = 0;t < T;t++){
    long long R,k,N;
    cin >> R >> k >> N;

    long long g[N];
    for(int i = 0;i < N;i++){
      cin >> g[i];
    }

    int startindex=0;
    long long result = 0;
    for(int r = 0;r < R;r++){
      long long summation = 0;

      summation += g[startindex];
      int next;
      for(next = (startindex+1) % N;next != startindex;next = (next+1) % N){
	//cout << "next=" << next << " value=" << g[next] << endl;
	if(summation + g[next] > k)

	  break;
	summation += g[next];
      }
      result += summation;
      startindex = next;
    }
    cout << "Case #" << (t+1) << ": " << result << endl;
  }
  return 0;
}
