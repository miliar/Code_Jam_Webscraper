#include<cstdio>
#include<queue>
#include<algorithm>
using namespace std;

struct t{
	int start;
	int end;
	int w;
};

int ile[2];
int n;
int na,nb;
int rtime;
int tih,tim;
int tmp;
t all[205];

int cmp(t a, t b){
	if(a.start!=b.start){
		return a.start<b.start;
	}else{
		return a.end<b.end;
	}
}

priority_queue<int> q[2];

int main(){
	scanf("%d",&n);
	for(int dd=1;dd<=n;dd++){
		scanf("%d",&rtime);
		scanf("%d %d",&na,&nb);
		ile[0]=ile[1]=0;
		for(int i=0;i<na;i++){
			scanf("%d:%d",&tih,&tim);
			all[i].start=60*tih+tim;
			scanf("%d:%d",&tih,&tim);
			all[i].end=60*tih+tim;
			all[i].w=0;
		}
		for(int i=0;i<nb;i++){
			scanf("%d:%d",&tih,&tim);
			all[i+na].start=60*tih+tim;
			scanf("%d:%d",&tih,&tim);
			all[i+na].end=60*tih+tim;
			all[i+na].w=1;
		}
		while(!q[0].empty()) q[0].pop();
		while(!q[1].empty()) q[1].pop();
		sort(all,all+na+nb,cmp);
		for(int i=0;i<na+nb;i++){
			//printf("%d %d %d\n",all[i].start,all[i].end,all[i].w);
			/*while(!q[all[i].w].empty()){
				tmp = -q[all[i].w].top();
				if(tmp<all[i].start){
					printf("zdejmuje: %d\n",tmp);
					q[all[i].w].pop();
				}else{
					break;
				}
			}*/
			if(q[all[i].w].empty()){
				ile[all[i].w]++;
				//printf("nie ma nic\n");
			}else{
				tmp = -q[all[i].w].top();
				//printf("%d\n",tmp);
				if(all[i].start>=tmp){
					//printf("jest %d\n",tmp);
					q[all[i].w].pop();
				}else{
					//printf("niestety cos jest nie tak\n");
					ile[all[i].w]++;
				}
			}
			q[all[i].w^1].push(-(all[i].end+rtime));
		}
		printf("Case #%d: %d %d\n",dd,ile[0],ile[1]);
	}
	return 0;
}

