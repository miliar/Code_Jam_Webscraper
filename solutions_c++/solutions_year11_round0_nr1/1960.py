#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define REPS(i,s,e) for(int i=s;i<e;++i)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define SORT(c) sort((c).begin,(c).end);
#define DSORT(c) sort((c).begin,(c).end,greater<__typeof((c).begin())>());

int next(char c,int from,vector<pair<char,int> > &d){
  REPS(i,from,d.size()){
	if(d[i].first == c)return d[i].second;
  }
  return 0;
}

int main(){
  int N;
  cin>>N;

  REP(i,N){
	int K;
	cin>>K;

	cerr<<"###case #"<<i+1<<" : "<<K<<endl;

	//input
	vector<pair<char,int> > d(K);
	REP(j,K){
	  cin>>d[j].first;
	  cin>>d[j].second;
	  //cerr<<"###"<<d[j].first<<":"<<d[j].second<<endl;
	}

	int b = 1;
	int o = 1;
	int tsum = 0;
	int n;

	//calc
	REP(j,K){
	  char h = d[j].first; // hall
	  int p = d[j].second; // pos

	  if(h == 'O'){
		int t = abs(o-p)+1;
		tsum += t;
		o = p;

		n = next('B',j+1,d);
		b = n + max(abs(n-b)-t,0);
	  }
	  else{
		int t = abs(b-p)+1;
		tsum += t;
		b = p;

		n = next('O',j+1,d);
		o = n + max(abs(n-o)-t,0);
	  }
	}

	cout<<"Case #"<<1+i<<": "<<tsum<<endl;
  }

  return 0;
}
