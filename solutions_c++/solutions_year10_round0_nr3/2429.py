#include<iostream>
#include<string>

using namespace std;

int arr[1000];
int p[1000];
int sum[1000];

int main() {
  int T, R, k, N;
 cin >> T;
for (int n = 0; n< T; ++n) {
  cin>>R>>k>>N;
  p[0]=sum[0] = 0;
  int s = 0;
  for (int i = 0; i< N; ++i) cin>>arr[i];
  do { sum[0]+=arr[p[0]]; p[0] = (p[0]+1)%N;} 
    while(p[0] && sum[0] + arr[p[0]] <= k);
  for (int i = 1; i < N; ++i) {
    p[i] = p[i-1]; sum[i] = sum[i-1];
    sum[i] -= arr[i-1];
    while(sum[i] + arr[p[i]] <= k) {sum[i]+=arr[p[i]];p[i]=(p[i]+1)%N;if(p[i]==i) break;}
  }
  s = 0;
  int ind = 0;
  for (int i = 0; i < R; ++i) {
    s += sum[ind];
    ind = p[ind];
  }
  cout<<"Case #"<<n+1<<": "<<s<<endl;
}
  return 0;
}
