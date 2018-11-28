#include <cstdio>
#include <queue>
using namespace std;

queue <int> groups;
queue <int> temp;

int main() {
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);

	int T;
	scanf("%d",&T);

	for(int caseNum=1;caseNum<=T;caseNum++) {
		int money = 0;
		int R,k,N;
		scanf("%d %d %d",&R,&k,&N);
		for(int i=0;i<N;i++) {
			int groupSize;
		 	scanf("%d",&groupSize);
			groups.push(groupSize);
		}

		for(int i=0;i<R;i++) {
			int seatsLeft = k;
			while(!groups.empty() && groups.front()<=seatsLeft) {
				seatsLeft -= groups.front();
				money += groups.front();
				temp.push(groups.front());
				groups.pop();
			}
			
			while(!temp.empty()) {
				groups.push(temp.front());
				temp.pop();
			}
		}
		printf("Case #%d: %d\n",caseNum,money);

		while(!groups.empty()) {
			groups.pop();
		}
	}
	return 0;
}
