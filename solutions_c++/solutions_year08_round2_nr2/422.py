#include<vector>
#include<set>
#include<iostream>
#include<algorithm>

using namespace std;

int par[1000010];
int sz[1000010];
vector<int> primes;

int find(int ind){
  if(par[ind]==-1)return ind;
  par[ind]=find(par[ind]);
  return par[ind];
}

void sieve_primes(){
  primes.push_back(2);
  for(int i=3;i<1000000;i+=2){
    bool ok = true;
    for(int j=0;j<primes.size() && primes[j]*primes[j]<=i;j++){
      if(i%primes[j]==0){ok=false;break;}
    }
    if(ok)primes.push_back(i);
  }
}

int main(){
  ios::sync_with_stdio(false);
  int C;
  cin >> C;
  sieve_primes();
  for(int q = 1; q <= C; q++){
    memset(par,-1,sizeof(par));
    memset(sz,0,sizeof(sz));
    long long A,B,P;
    cin >> A >> B >> P;
    vector<int> up(lower_bound(primes.begin(),primes.end(),P), primes.end());
    long long diff = B-A;
    //    cout<<up[0]<<" "<<A<<" "<<B<<" "<<P<<up[up.size()-1]<<endl;
    vector<int> mp(up.size(),-1);
    for(int i=0;i<=diff;i++){
      //      cout<<i<<" "<<par[0]<<endl;
      vector<int> pds;
      for(int j=0;j<up.size() && up[j] <= diff;j++){
	if((A+i)%up[j]==0){
	  pds.push_back(j);
	}
      }
      for(vector<int>::iterator it=pds.begin();it!=pds.end();it++){
	if(mp[*it]!=-1){
	  int ind = find(mp[*it]);
	  int sind = find(i);
	  if(ind==sind)continue;
	  if(sz[ind]<sz[sind]){
	    par[ind]=sind;
	    sz[sind]++;
	  }else{
	    par[sind]=ind;
	    sz[ind]++;
	  }
	}else{
	  mp[*it]=i;
	}
      }
    }
    int ret = count(par, par + diff + 1, -1);
    cout<<"Case #"<<q<<": "<<ret<<endl;
  }
}
