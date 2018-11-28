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
  int T;
  cin>>T;

  REP(i,T){
	int N;
	cin>>N;

	vector<int> cans(N);
	int par = 0;
	int minc = INT_MAX;
	int sumc = 0;
	REP(j,N){
	  int c;
	  cin>>c;

	  par ^= c;
	  sumc += c;
	  minc = min(minc,c);
	}

	cout<<"Case #"<<i+1<<": ";
	if(par != 0){
	  cout<<"NO"<<endl;
	}
	else{
	  cout<<sumc-minc<<endl;
	}
	  
  }

  return 0;
}
