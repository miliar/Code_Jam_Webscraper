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

int main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;++t){
	int R,C;
	cin>>R>>C;
	vector<string> line(R);

	REP(y,R){
	  cin>>line[y];
	}

	double imp = false;
	REP(y,R){
	  REP(x,C){
		if(line[y][x] == '#'){
		  if(x+1==C || y+1==R){
			imp = true;
			break;
		  }

		  if(line[y][x+1] != '#' || line[y+1][x] != '#' || line[y+1][x+1] != '#'){
			imp = true;
			break;
		  }

		  line[y][x] = line[y+1][x+1] = '/';
		  line[y][x+1] = line[y+1][x] = '\\';
		}
	  }
	  if(imp)break;
	}
	
	cout<<"Case #"<<t<<": "<<endl;
	if(imp){
	  cout<<"Impossible"<<endl;
	}
	else{
	  REP(i,R)
		cout<<line[i]<<endl;
	}
  }

  return 0;
}
