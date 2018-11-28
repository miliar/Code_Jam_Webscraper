#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <functional>
#include <vector>

using namespace std;
int n;
char m[50][50];

int getans(int d){
	if(d==n)return 0;
	int i,j,ri,ci,ret=0;
	for(i=d;i<n;i++){
		ci=-1;
		for(j=d;j<n;j++)if(m[i][j]=='1')ci=j;
		if(ci<d+1){
			ri=i;
			break;
		}
	}
	if(ri>d)for(i=ri;i>d;i--){
		for(j=d;j<n;j++)swap(m[i][j],m[i-1][j]);
		ret++;
	}
	ret+=getans(d+1);
	return ret;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,Q,i;
	scanf("%d",&Q);
	for(T=1;T<=Q;T++){
		scanf("%d",&n);
		gets(m[0]);
		for(i=0;i<n;i++)gets(m[i]);

		printf("Case #%d: %d\n",T,getans(0));
	}
	return 0;
}
