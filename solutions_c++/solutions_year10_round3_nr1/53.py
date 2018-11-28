#include <iostream>

using namespace std;

typedef pair<int,int> data;

main(){
  int T;
  cin >> T;

  for(int t = 0;t < T;t++){
    long long N;
    cin >> N;

    data wire[N];
    for(int i = 0;i < N;i++){
      int x,y;
      cin >> wire[i].first >> wire[i].second;
    }

    int result = 0;
    for(int i = 0;i < N;i++){
      for(int j = i+1;j < N;j++){
	if(wire[i].first < wire[j].first && wire[i].second >  wire[j].second
	    || wire[i].first > wire[j].first && wire[i].second <  wire[j].second)
	  result++;
      }
    }
    cout << "Case #" << (t+1) << ": " << result << endl;
  }
  return 0;
}
