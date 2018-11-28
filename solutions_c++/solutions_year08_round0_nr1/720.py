#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<string>
#include<cassert>
#include<algorithm>

using namespace std;

struct state_t {
  int sid, qnum;
  int cost;
  
  state_t(int s, int q, int c) : sid(s), qnum(q), cost(c) {}
};

bool operator>(const state_t& s1, const state_t& s2){
  return s1.cost > s2.cost;
}

bool done[101][1002];

int main(){
  int T; cin >> T;
  string sk;
  for(int t=0;t<T;++t){
    int S; cin >> S; std::getline(cin, sk);

    vector<string> engines(S);
    for(int i=0;i<S;++i) getline(cin, engines[i]);

    int Q; cin >> Q; getline(cin, sk);
    vector<string> queries(Q); 
    for(int i=0;i<Q;++i) getline(cin, queries[i]);

    priority_queue<state_t, vector<state_t>, greater<state_t> > pq;

    if(Q==0){
      cout << "Case #" << (t+1) << ": " << 0 << endl;
      goto next;
    }
    for(int i=0;i<S;++i){
      if(engines[i] != queries[0])
	pq.push(state_t(i, 0, 0));
    }
    memset(done, 0, sizeof(done));

    while(!pq.empty()){
      const state_t st = pq.top(); pq.pop();
      if(!done[st.sid][st.qnum]){
	if(st.qnum == Q-1){
	  cout << "Case #" << (t+1) << ": " << st.cost << endl;
	  break;
	}
	done[st.sid][st.qnum] = true;

	assert(st.qnum+1 < queries.size());
	
	if(queries[st.qnum+1] == engines[st.sid]){
	  for(int i=0;i<S;++i){
	    if(i!=st.sid){
	      pq.push(state_t(i, st.qnum+1, st.cost+1));
	    }
	  }
	}else{  
	  pq.push(state_t(st.sid, st.qnum+1, st.cost));
	}
      }
    }
  next:;

  }
}
