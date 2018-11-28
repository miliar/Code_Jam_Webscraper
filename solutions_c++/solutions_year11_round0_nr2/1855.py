#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <list>

using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define REPS(i,s,e) for(int i=s;i<e;++i)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define SORT(c) sort((c).begin,(c).end);
#define DSORT(c) sort((c).begin,(c).end,greater<__typeof((c).begin())>());

char combine[256][256];
bool oppose[256][256];

int main(){
  int N;
  cin>>N;

  REP(i,N){
	cerr<<"###case #"<<i+1<<endl;

	//clear table
	REP(x,256){
	  REP(y,256){
		combine[x][y] = 0;
		oppose[x][y] = false;
	  }
	}

	//read combile table
	int cn;
	cin>>cn;
	REP(c,cn){
	  string s;
	  cin>>s;
	  combine[s[0]][s[1]] = combine[s[1]][s[0]] = s[2];
	}

	//read oppse table
	int on;
	cin>>on;
	REP(o,on){
	  string s;
	  cin>>s;
	  oppose[s[0]][s[1]] = oppose[s[1]][s[0]] = true;
	}

	list<char> seq;
	int sn,j;
	char to;
	cin>>sn;
	REP(j,sn){
	  char c;
	  cin>>c;

	  if(seq.empty()){
		seq.push_back(c);
		continue;
	  }

	  //combine
	  int lastc = seq.back();
	  if((to = combine[c][lastc]) != 0){
		seq.pop_back();
		seq.push_back(to);
		continue;
	  }

	  //oppose
	  FOR(it,seq){
		if(oppose[*it][c]){
		  seq.clear();
		  goto loop_end;
		}
	  }

	  seq.push_back(c);
loop_end:
	  ;
	  //cerr<<"["<<c<<"]"<<endl;
	}

	cout<<"Case #"<<1+i<<": "<<"[";
	bool f = false;
	for(list<char>::iterator it = seq.begin(); it != seq.end(); ++it){
	  if(f){
		cout<<", ";
	  }
	  if(!f)f=true;

	  cout<<*it;
	}
	cout<<"]"<<endl;
  }

  return 0;
}
