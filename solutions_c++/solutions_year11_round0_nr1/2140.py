#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;



int main(){
	int cases;
	scanf("%d",&cases);
	int bloc, btime, oloc,otime,pushes,goal;
	char current[10];
	for(int c=1; c<=cases; ++c){
		bloc=oloc=1;
		btime=otime=0;
		scanf("%d",&pushes);
		for(int p=0; p<pushes; ++p){
			scanf("%s %d",current, &goal);
			if(current[0]=='O'){
				otime=max(btime+1,otime+abs(goal-oloc)+1);
				oloc=goal;
			}else{
				btime=max(otime+1,btime+abs(goal-bloc)+1);
				bloc=goal;
			}
			//printf("O=%d at time %d, B=%d at time %d\n",oloc,otime,bloc,btime);		
		}
		printf("Case #%d: %d\n",c,max(btime,otime));
	}
	return 0;
}

