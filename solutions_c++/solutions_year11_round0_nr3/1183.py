#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int test,n,testcase;

int main(){
	freopen("i.txt","r",stdin);
	testcase=1;
	for (scanf("%d",&test);test--;testcase++){
		scanf("%d",&n);
		printf("Case #%d: ",testcase);
		int ans=0,opt=-1;
		long long tot=0;
		for (int i=1;i<=n;i++){
			int x;
			scanf("%d",&x);
			ans^=x;
			tot+=x;
			if (opt==-1 || opt>x) opt=x;
		}
		if (ans) puts("NO");
			else cout<<tot-opt<<endl;
	}
	return 0;
}
