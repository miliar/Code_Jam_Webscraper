#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include<cmath>
#include <map>
using namespace std;
int main() {
	freopen("D-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int cas,i,ans,x,n;int k=1;
	scanf("%d",&cas);
	while(cas--){

		scanf("%d",&n);
		ans=0;
		for(i=1;i<=n;i++){
			scanf("%d",&x);
		 if(x!=i)
			ans++;
		}
		printf("Case #%d: ",k++);
		cout<<ans;
		cout<<".000000"<<endl;
	}
	fclose(stdin);
    fclose(stdout);
	return 0;
}


