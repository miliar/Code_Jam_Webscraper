
#include <iostream>

using namespace std;

int main () {
  int nt;
  cin>>nt;
  for (int test=1; test<=nt; test++) {
	int n,k;
	cin>>n>>k;
	k%=(1<<n);
	cout<<"Case #"<<test<<": ";
	if (k==(1<<n)-1) cout<<"ON"<<endl; else cout<<"OFF"<<endl;
  }

  return 0;
}
