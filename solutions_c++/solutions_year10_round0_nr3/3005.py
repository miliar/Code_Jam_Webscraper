#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

int main() {

  int T;
  cin >> T;

  // cerr << "T: " << T;
  for(int i = 1; i<= T; i++) {
    unsigned R, k, N;
    cin >> R >> k >> N;

    // printf("R: %d, k: %d, N: %d\n", R, k, N);
    list<int> group_list(1000);
    list<int> boarding_list(N);
    // cout << "begin case 2" << endl;

    for(int j=0; j<N; j++){
      int gi;
      cin >> gi;
      // cout << gi << " ";
      group_list.push_back(gi);
    }

    
    // iterate over the rounds
    int passengers = 0;
    
    for(int round=0; round<R; round++){
      // cout << "running round: "<< round << endl;
      if(group_list.empty()){
	break;
      }

      // process current round
      boarding_list.clear();
      int current_capacity = k;
      while ( current_capacity > 0 && !group_list.empty()){

	int group_size =  group_list.front();

	// cout << "." << passengers << ":" << current_capacity << ":" << group_size << endl;
	if(group_size <= current_capacity){

	  current_capacity -= group_size;
	  passengers += group_size;

	  boarding_list.push_back(group_size);
	  group_list.pop_front();
	  
	} else {
	  current_capacity = 0;
	}
      }

      // This round finished!

      // Move the riding passengers back to the queue
      copy (boarding_list.begin(), boarding_list.end(),      // source
	    back_inserter(group_list));           // destination
      boarding_list.clear();
    }
    cout << "Case #" << i <<": "<< passengers << endl;

  }
}
