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
	int N,L,H;
	cin>>N>>L>>H;

	vector<int> freq(N);
	REP(i,N){
	  cin>>freq[i];
	  //cout<<freq[i]<<" ";
	}

	int ff = L-1;
	REPS(f,L,H+1){
	  int ok = 1;
	  REP(i,N){
		if(!((f % freq[i]==0) || (freq[i] % f==0))){
		  ok = 0;break;
		}
	  }
	  if(ok){
		ff = f;
		break;
	  }
	}
	
	cout<<"Case #"<<t<<": ";
	if(ff<L)cout<<"NO"<<endl;
	else cout<<ff<<endl;
  }

  return 0;
}
