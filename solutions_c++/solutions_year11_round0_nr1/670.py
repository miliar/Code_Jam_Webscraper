#include <cstdio>
#include <algorithm>

using namespace std;

int tr,n,pos[3],timep[3];

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&tr);
	for (int test=0;test<tr;test++){
		scanf("%d",&n);
		pos[0]=pos[1]=1,timep[0]=timep[1]=0;
		int flag,now=0;
		for (int i=0;i<n;i++){
			char ch,ch1;
			int d;
			scanf("%c%c%d",&ch1,&ch,&d);
			if (ch=='O') flag=0;
				else flag=1;
			if (abs(pos[flag]-d)<=now-timep[flag])
				now++,timep[flag]=now;
			else
				now=abs(pos[flag]-d)+timep[flag]+1,timep[flag]=now;
			pos[flag]=d;
		}
		printf("Case #%d: %d\n",test+1,now);
	}
	
	return 0;
}
