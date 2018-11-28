#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int K,n,B,T;
int x[101];
int v[101];

int main(){
	int tc,tt;
	cin>>tc;
	int i;
	for(tt=1;tt<=tc;tt++)
	{
		cout<<"Case #"<<tt<<": ";	
		cin>>n>>K>>B>>T;
		for(i=0;i<n;i++)
			cin>>x[i];
		for(i=0;i<n;i++)
			cin>>v[i];
		int ok = 0,nok = 0;
		int ans = 0;
		for(i=n-1;i>=0&&ok<K;i--){
			if(x[i]+v[i]*T>=B){
				ok++;
				ans+=nok;
				continue;
			}
			nok++;
		}
		if(ok==K)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
