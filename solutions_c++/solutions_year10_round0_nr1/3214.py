#include<iostream>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,n,k,cases;
	scanf("%d",&cases);
	for(i = 1;i <= cases;i ++) {
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i);
		puts( (k + 1) % (1<<n) == 0 ? "ON" : "OFF");
	}
}