#include<iostream>
#include<queue>

using namespace std;

 struct group {
  int g_num;
  bool is_in;
};

int main ()  {
  
  int tt_c;
  cin >> tt_c;

  int i = 0;
  for( ; i < tt_c; i++) {
    int tt_m = 0;
    
    int R = 0;
    int k = 0;
    int N = 0;
    cin >> R >> k >> N;
    
    // Get the start group list
    queue<group> g_queue;
    group  one_group;
    int j = 0;
    for( ; j < N; j++) {
      cin >> one_group.g_num;
      one_group.is_in = false;
      g_queue.push( one_group );
    }

    // Start to run
    j = 0;
    for( ; j < R; j++) {
      int one_m = 0;
      group cur_group = g_queue.front();
      int current_g = cur_group.g_num;
      int current_p = 0;
      current_p += current_g;
      while ( (current_p <= k) && cur_group.is_in == false ) {
	cur_group.is_in = true;
	g_queue.pop();
	g_queue.push( cur_group );
	cur_group = g_queue.front();
	current_g = cur_group.g_num;
	current_p +=current_g;
      }
      one_m = current_p - current_g;
      tt_m += one_m;
      
      int j = 0;
      for( ; j < g_queue.size(); j++) {
	group group_iter = g_queue.front();
	group_iter.is_in = false;
	g_queue.pop();
	g_queue.push( group_iter );
      }
    }

    // Output the result
    cout << "Case #" << i+1 << ": " << tt_m << endl;
  }

  return 0 ;
}
