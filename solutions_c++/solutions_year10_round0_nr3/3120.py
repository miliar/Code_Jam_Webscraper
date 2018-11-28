#include<iostream>
#include<queue>
using namespace std;

int r,k,n,a[1010],cases;
queue<int> q;

void work() {
	int i,j,t,sum = 0,s = 0;
	for(i = 1;i <= r;i ++) {
		for(j = 1;j <= n;j ++) {
			t = q.front();
			if(sum + t <= k) {
				q.pop();
				sum += t;
				q.push(t);
			}
			else
				break;
		}
		s += sum;
		sum = 0;
	}
	printf("Case #%d: ",++ cases);
	printf("%d\n",s);
}

int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,t,cases;
	scanf("%d",&cases);
	for(i = 1;i <= cases;i ++) {
		scanf("%d%d%d",&r,&k,&n);
		while(!q.empty()) {
			q.pop();
		}
		for(j = 1;j <= n;j ++) {
			scanf("%d",&t);
			q.push(t);
		}
		
		work();
	}
}