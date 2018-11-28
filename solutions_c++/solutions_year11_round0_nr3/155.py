#include<iostream>
#include<vector>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;


int main(){
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	int TC=0,tem,temp,ans,mm,T,n;
	scanf("%d",&T);
	while(T--){TC++;
		scanf("%d",&n);
		ans=0;tem=0;mm=0x3fffffff;
		while(n--){
			scanf("%d",&temp);
			mm = min(mm,temp);
			ans+=temp;
			tem^=temp;
		}
		printf("Case #%d: ",TC);
		if(tem)printf("NO\n");
		else printf("%d\n",ans-mm);
	}
}
