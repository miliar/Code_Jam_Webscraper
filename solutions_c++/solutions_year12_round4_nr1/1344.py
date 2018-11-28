#include<cstdio>
#include<vector>
#include<stack>

using namespace std;

struct vine {
	int length;
	int dist;
	int maxrange;
};

int main() {
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		int N;
		scanf("%d",&N);
		vector<vine> vines;
		int D;
		stack<int> updated;
		vines.resize(N);
		for(int n=0;n<N;n++)
			scanf("%d %d",&(vines[n].dist),&(vines[n].length));
		updated.push(0);
		vines[0].maxrange = vines[0].dist;
		scanf("%d",&D);
		bool found = false;
		while(!updated.empty()) {
			int cur = updated.top(); updated.pop();
			if( vines[cur].dist + vines[cur].maxrange >= D) {
				found = true;
				break;
			}
			for(int i=cur+1;vines[i].dist<=vines[cur].dist+vines[cur].maxrange;i++) {
				if(i<0||i>=N)
					break;
				int newmaxrange = vines[i].dist - vines[cur].dist;
				if(newmaxrange > vines[i].maxrange && vines[i].maxrange < vines[i].length) {
					vines[i].maxrange = newmaxrange;
					updated.push(i);
					if(vines[i].maxrange >vines[i].length)
						vines[i].maxrange = vines[i].length;
				}
			}
			for(int i=cur-1;vines[i].dist>=vines[cur].dist-vines[cur].maxrange;i++) {
				if(i<0||i>=N)
					break;
				int newmaxrange = vines[cur].dist - vines[i].dist;
				if(newmaxrange > vines[i].maxrange && vines[i].maxrange < vines[i].length) {
					vines[i].maxrange = newmaxrange;
					updated.push(i);
					if(vines[i].maxrange >vines[i].length)
						vines[i].maxrange = vines[i].length;
				}
			}
		}
		if( found ) {
			printf("Case #%d: YES\n",t);
		} else {
			printf("Case #%d: NO\n",t);
		}
	}
	return 0;
}
