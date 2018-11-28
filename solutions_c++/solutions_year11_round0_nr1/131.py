#include <stdio.h>
#include <string.h>

const int Max = 1024;
int A[Max];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,N;
	scanf("%d",&T);
	for (int t = 1;t <= T;t++){
		scanf("%d",&N);
		int R = 0,x;
		char robot[4];
		int O = 1,B = 1;
		int tO = 0,tB = 0;
		for (int i = 1;i <= N;i++){
			scanf("%s%d",robot,&x);
			if (robot[0] == 'O'){
				int cd = x-O;
				if (cd < 0) cd = -cd;
				int cv = cd > tO?cd-tO+1:1;
				R += cv;
				tB += cv;
				O = x,tO = 0;
			}else{
				int cd = x-B;
				if (cd < 0) cd = -cd;
				int cv = cd > tB?cd-tB+1:1;
				R += cv;
				tO += cv;
				B = x,tB = 0;
			}
			//printf("%d(%d) %d(%d) | %d\n",O,tO,B,tB,R);
		}
		printf("Case #%d: %d\n",t,R);
	}
	//while(1);
	return 0;
}
