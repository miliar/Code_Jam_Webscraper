#include<iostream>
#include<vector>
#include<set>
#include<algorithm>

using namespace std;

bool pred(int a, int b){
  return a>b;
}

int main(){
  int Q;
  ios::sync_with_stdio(false);
  cin >> Q;
  for(int q=1;q<=Q;q++){
    int P, K, L;
    cin >> P >> K >> L;
    vector<int> freq(L,0);
    for(int i=0;i<L;i++){
      cin >> freq[i];
    }
    sort(freq.begin(),freq.end(),pred);
    long long mn=1;
    int ind = 0;
    long long sum=0;
    while(ind < freq.size() && mn<=P){
      for(int i=0;i<K && ind < freq.size();i++,ind++){
	sum+=mn*(long long)freq[ind];
      }
      mn++;
    }
    if(ind<freq.size())cout<<"Case #"<<q<<": Impossible"<<endl;
    else cout<<"Case #"<<q<<": "<<sum<<endl;
  }
}
