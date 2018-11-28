#include <iostream>
using namespace std;
int main(){
	int i,j,t,n,k,ans;
	freopen("A-large-1.txt","r",stdin);
	freopen("Output.txt","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%d%d",&n,&k);
		ans=1;
		for(j=0;j<n;j++) ans*=2;
		k%=ans;
		if(k==ans-1) printf("Case #%d: ON\n",i);
        else printf("Case #%d: OFF\n",i);	
	}
	return 0;
}