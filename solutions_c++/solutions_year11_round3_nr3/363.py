#include <iostream>

using namespace  std;

int n,minf,maxf;
int f[200];

bool concord( int me ) 
{
	
	for(int i = 0;i<n;i++)
		if (!(f[i]/me*me==f[i])&&!(me/f[i]*f[i]==me))
			return false;
	return true;
}

void compute() {
	cin>>n>>minf>>maxf;
	for(int i = 0;i<n;i++)
		cin>>f[i];
	bool harm = false;
	for(int i = minf;i<=maxf;i++) {
		if (concord(i)) {
			cout<<i<<"\n";
			return ;
		}
	}
	cout<<"NO\n";

}
int main() {
	int ncase;
	cin>>ncase;
	for(int i = 0;i<ncase;i++) {
		cout<<"Case #"<<i+1<<": ";
		compute();
	}
}