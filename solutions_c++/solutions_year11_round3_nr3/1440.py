#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long Int;
Int num[10000];
int main(){
	int tcase;
	cin>>tcase;
	for(int itcase=1; itcase<=tcase; ++itcase){
		int n;
		Int L,H;
		cin>>n>>L>>H;
		for(int i=0;i<n;++i)
			cin>>num[i];
		Int ans=-1;
		for(Int i=L;i<=H;++i){
			bool ok=true;
			for(int j=0;j<n;++j)
				if(!((i>=num[j] && i%num[j]==0) || (num[j]>=i && num[j]%i==0))){
					ok=false;
					break;
				}
			if(ok){
				ans=i;
				break;
			}
		}
		printf("Case #%d: ", itcase);
		if(ans==-1){
			printf("NO\n");
		}else{
			cout<<ans<<endl;
		}
	}
	return 0;
}
