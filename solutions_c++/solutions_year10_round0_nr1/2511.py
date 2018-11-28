#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main() {
  int N;
cin>>N;
for (int i = 0; i < N; ++i) {
  int x, y; cin>>x>>y;
cout<<"Case #"<<i+1<<": ";
long long z = (1LL<<x) - 1;
cout<<((z & y) == z ? "ON" : "OFF");
cout<<endl;
}

return 0;
}
