#include<iostream>

using namespace std;

int t,n,k;
void solve(int x){
	cin>>n>>k;
	if( ( (k+1) % (1<<n) )==0) cout<<"Case #"<<x<<": ON"<<endl;
	else  cout<<"Case #"<<x<<": OFF"<<endl;

}

int main(){
freopen("A.in","r",stdin);
freopen("A.out","w",stdout);
cin>>t;
for(int i=1;i<=t;i++)
	solve(i);

return 0;
}