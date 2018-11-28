#include <cstdio>
#include <queue>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i  = 0;i<n;i++){
		int pos[2];
		pos[0]=1;pos[1]=1;
		int a;
		scanf("%d",&a);
		queue<int> nextpos[2];
		queue<int> nextbot;
		for(int j = 0;j<a;j++){
			char t;
			scanf("%c",&t);
			while(t != 'O' && t != 'B')scanf("%c",&t);
			int tn;
			scanf("%d",&tn);
			if(t == 'O'){
				nextbot.push(0);
				nextpos[0].push(tn);
			}else{
				nextbot.push(1);
				nextpos[1].push(tn);
			}
		}
		int timer = 0;
		while(!nextbot.empty()){
			timer++;
			int t = nextbot.front();
			if(pos[t] == nextpos[t].front()){
				nextbot.pop();
				nextpos[t].pop();
			}else{
				if(nextpos[t].front()-pos[t] < 0)pos[t]--;
				if(nextpos[t].front()-pos[t] > 0)pos[t]++;
			}
			if(nextpos[abs(t-1)].front()-pos[abs(t-1)] < 0)pos[abs(t-1)]--;
			if(nextpos[abs(t-1)].front()-pos[abs(t-1)] > 0)pos[abs(t-1)]++;
		}
		printf("Case #%d: %d\n",i+1,timer);
	}
	return 0;
	
}