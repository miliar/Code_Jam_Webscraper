#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

long long gcd(long long b, long long a){
  if(a>b){
	int tmp = a;
	a = b;
	b = tmp;
  }
  // b >= a
  return a!=0 ? gcd(a, b % a) : b;
}

int main(){
  int T; cin >> T;
  for(int t=0;t<T;++t){
	int N,L,H; cin>>N>>L>>H;
	vector<int> freq(N);
	for(int i=0;i<N;++i) cin>>freq[i];
	if(N==1){
	  if(L<=freq[0] and freq[0]<=H){
		cout<<"Case #"<<t+1<<": "<<freq[0]<<endl;
	  }else{
		cout<<"Case #"<<t+1<<": NO"<<endl;
	  }
	  continue;
	}
	sort(freq.begin(),freq.end());
	int ans = -1;
	for(int i=L;i<=H;++i){
	  bool f=true;
	  for(int j=0;j<N;++j){
		if(freq[j]==1) continue;
		if(freq[j]%i!=0 and i%freq[j]!=0) f=false;
		//cout<<freq[j]%i<<" "<<i%freq[j]<<endl; 
	  }
	  if(f){
		ans = i;
		break;
	  }
	}
	cout<<"Case #"<<t+1<<": ";
	if(ans!=-1) cout<<ans;
	else cout<<"NO";
	cout << endl;
  }
  return 0;
}

