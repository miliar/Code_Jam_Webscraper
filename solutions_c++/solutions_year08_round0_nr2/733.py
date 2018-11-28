#include <cstdio>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int N,NA,NB,TA;

int trains[2],ans[2];

//0 trem avaible a
//1 trem avaible b
//2 trem parte a
//3 trem parte b

struct event {
	int tipo, h;

	event(int t,int hora) {
		tipo=t;
		h=hora;
	}
	bool operator<(const event& e) const {
		if(h==e.h) {
			return tipo>e.tipo;
		}
		return h>e.h;
	}
};

priority_queue<event> q;

int main(void) {
	cin >> N;
	for(int T=1;T<=N;T++) {
		trains[0]=trains[1]=ans[0]=ans[1]=0;
		printf("Case #%d: ",T);
		cin >> TA >> NA >> NB;
		for(int i=0;i<NA;i++) {
			int j,k;
			scanf("%d:%d",&j,&k);
			j=j*60+k;
			q.push(event(2,j));
			scanf("%d:%d",&j,&k);
			j=j*60+k+TA;
			q.push(event(1,j));
		}
		for(int i=0;i<NB;i++) {
			int j,k;
			scanf("%d:%d",&j,&k);
			j=j*60+k;
			q.push(event(3,j));
			scanf("%d:%d",&j,&k);
			j=j*60+k+TA;
			q.push(event(0,j));
		}

		while(!q.empty()) {
			switch(q.top().tipo) {
				case 0:
					trains[0]++;
					break;
				case 1:
					trains[1]++;
					break;
				case 2:
					trains[0]--;
					while(trains[0]<=0) {
						ans[0]++;
						trains[0]++;
					}
					break;
				case 3:
					trains[1]--;
					while(trains[1]<=0) {
						ans[1]++;
						trains[1]++;
					}
					break;
			}
			q.pop();
		}
		printf("%d %d\n",max(0,ans[0]-1),max(0,ans[1]-1));
	}
	return 0;
}
