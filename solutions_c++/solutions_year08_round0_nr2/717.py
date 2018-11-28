#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<algorithm>

using namespace std;

bool comp_second(const pair<int, int>& p1, const pair<int, int>& p2){
  return p1.second < p2.second;
}

int max_match(vector<pair<int, int> >& src_dept, vector<pair<int, int> >& dest_dept, int T){
  int Ns = src_dept.size();
  int Nd = dest_dept.size();
  

  sort(src_dept.begin(), src_dept.end(), comp_second);
  sort(dest_dept.begin(), dest_dept.end());
  int next_id = 0;
  int match = 0;
  for(int is=0;is<Ns;++is){
    for(;next_id<Nd;++next_id){
      if(src_dept[is].second + T <= dest_dept[next_id].first){
	//	cout << src_dept[is].second << " " << dest_dept[next_id].first << endl;
	++match;
	break;
      }
    }
    next_id++;
  }
  return match;
}

int read_time(){
  int h, m;
  char c; cin >> h >> c >> m;
  assert(c==':');
  return h*60 + m;
}

int main(){
  int T; cin >> T;
  for(int t=0;t<T;++t){
    int T, NA, NB;
    cin >> T;
    cin >> NA >> NB;
    
    vector<pair<int, int> > AtoB;
    vector<pair<int, int> > BtoA;
    for(int i=0;i<NA;++i){
      int st, ed;
      st = read_time();
      ed = read_time();
      AtoB.push_back(make_pair(st, ed));
    }
    for(int i=0;i<NB;++i){
      int st, ed;
      st = read_time();
      ed = read_time();
      BtoA.push_back(make_pair(st, ed));
    }
    
    int max_matchAtoB = max_match(AtoB, BtoA, T);
    int max_matchBtoA = max_match(BtoA, AtoB, T);
    //    cout << max_matchAtoB << endl;
    cout << "Case #" << (t+1) << ": " << NA-max_matchBtoA << " " << NB-max_matchAtoB << endl;
    
  }
}
