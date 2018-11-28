#include <iostream>
#include <queue>
using namespace std;

#define abs(a) ((a)>0?(a):-(a))

int main(){
  int T;
  cin>>T;
  for(int t=1; t<=T; t++){
    int N;
    cin>>N;
    int state[2];
    int time = 0;
    queue<int> q[2];
    queue<pair<int, int> > cmd;
    state[0] = 1;
    state[1] = 1;
    
    for(int i=0;i<N;i++){
      char b;
      int p;
      cin >> b >> p;
      int idx;
      if(b =='B')
	idx = 0;
      else
	idx = 1;
      q[idx].push(p);
      pair<int, int> next_cmd;
      next_cmd.first = idx;
      next_cmd.second = p;
      cmd.push(next_cmd);
    }

    pair<int, int> next = cmd.front();

    while(!cmd.empty()){
      pair<int,int> next_cmd = cmd.front();
      cmd.pop();
      int idx = next_cmd.first;
      int pos = next_cmd.second; 
      
      int dist = state[idx] - pos;
      dist = abs(dist);
      time += dist+1;

      state[idx] = pos;
      q[idx].pop();
      if(!q[1-idx].empty()){
	  int next_pos = q[1-idx].front();
	  if(next_pos < state[1-idx])
	    state[1-idx] = max(next_pos, state[1-idx] - (dist+1));
	  else
	    state[1-idx] = min(next_pos, state[1-idx] + (dist+1));
	}
    }
    cout << "Case #" << t << ": " << time << endl;
  }
}
