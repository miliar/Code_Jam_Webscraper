#include <stdio.h>
#include <algorithm>
using namespace std;

int main(){
	int ntc;
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		int n,pos,posO=1,posB=1,idleO=0,idleB=0,res=0;
		char color,pcolor='A';
		scanf("%d",&n);
		for (int i=0;i<n;i++){
			scanf(" %c %d",&color,&pos);
			if (color==pcolor){
				if (color=='O'){
					int t=abs(posO-pos)+1;
					posO=pos;
					idleB+=t;
					res+=t;
					pcolor='O';
				}
				else{
					int t=abs(posB-pos)+1;
					posB=pos;
					idleO+=t;
					res+=t;
					pcolor='B';
				}
			}
			else{
				if (color=='O'){
					int t=abs(posO-pos);
					if (idleO>t) t=0;
					else t-=idleO;
					posO=pos;
					idleO=0;
					idleB=t+1;
					res+=(t+1);
					pcolor='O';
				}
				else{
					int t=abs(posB-pos);
					if (idleB>t) t=0;
					else t-=idleB;
					posB=pos;
					idleB=0;
					idleO=t+1;
					res+=(t+1);
					pcolor='B';
				}
			}
		}
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}