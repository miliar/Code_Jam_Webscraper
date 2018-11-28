#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;
int X[8];
int Y[8];

int main(){
freopen("A-small-attempt0.in","r",stdin);
freopen("A-small-attempt0.out","w",stdout);

int cases;
int T;
cin>>T;
for(cases=1;cases<=T;++cases)
{
	int n;
	int i;
	cin>>n;
	for(i=0;i<n;++i)
		cin>>X[i];
	for(i=0;i<n;++i)
		cin>>Y[i];
	sort(X,X+n);
	sort(Y,Y+n,greater<int>());
	int sum=0;
	for(i=0;i<n;++i)
		sum+=X[i]*Y[i];
	cout<<"Case #"<<cases<<": "<<sum<<endl;
}
return 0;
}