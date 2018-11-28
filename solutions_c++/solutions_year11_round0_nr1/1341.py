#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

int T;
int N;
char c[10];
int pos;

int main(){
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		scanf("%d",&N);
		int o = 1, ot = 0;
		int b = 1, bt = 0;
		while (N--){
			scanf("%s %d",c,&pos);
			if (c[0]=='O'){
				ot += abs(pos-o) + 1;
				if (ot<bt+1) ot = bt+1;
				o = pos; 
			}else{
				bt += abs(pos-b) + 1;
				if (bt<ot+1) bt = ot+1;
				b = pos;
			}
		}
			printf("Case #%d: %d\n",t,max(bt,ot));
	}

	return 0;
}
