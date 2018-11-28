
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<string.h>
#include<cstring>
#include<stack>
#include<queue>
#include<cassert>

using namespace std;

#define LL long long int 
#define PII pair<int,int> 

int main(){
	int i,n,test,t,x,c,ans,sum;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
		ans=sum=0;
		c=1e7;
		scanf("%d",&n);
		while(n--){
			scanf("%d",&x);
			sum+=x;
			c=min(c,x);
			ans^=x;
		}
		if(ans==0)
			printf("Case #%d: %d\n",test,sum-c);
		else
			printf("Case #%d: NO\n",test);
		
	}
	return 0;
}
