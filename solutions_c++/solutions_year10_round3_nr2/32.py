#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<map>
#include<queue>
#include<iostream>
#include<sstream>
using namespace std;
#define LL __int64
LL L,P,C;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,ca,times,cnt;
	cin>>t;
	for(ca=1;ca<=t;ca++){
		cin>>L>>P>>C;
		for(cnt=0;L*C<P;cnt++,L*=C);
		for(times=0;cnt;times++)
			cnt>>=1;
		cout<<"Case #"<<ca<<": "<<times<<endl;
	}
	return 0;
}