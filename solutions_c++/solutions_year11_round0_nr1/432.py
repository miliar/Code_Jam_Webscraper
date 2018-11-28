#include <stdio.h>

int n;

int dat[103][2];

int main(){
	int T;
	int testcase = 0;
	scanf("%d",&T);
	while(T--> 0 ){
		++testcase;
		printf("Case #%d: ",testcase);
		scanf("%d",&n);
		for(int i = 0;i < n; i++){
			char order[4];
			int pos;
			scanf("%s",order);
			scanf("%d",&pos);
			if(order[0] == 'O'){
				dat[i][0] = 0;
			}else{
				dat[i][0] = 1;
			}
			dat[i][1] = pos;
		}

		int ans = 0;
		int p1 = 1, p2 = 1;
		int i = 0;
		for(;i < n;ans++){
			int butpress = 0;
			if(dat[i][0] == 0 && dat[i][1] == p1){
				i ++;
				butpress = 1;
			}else{
				for(int j = i;j < n;j ++){
					if(dat[j][0] == 0){
						if(dat[j][1] > p1) {
							p1 ++;
						}else if(dat[j][1] < p1){
							p1 --;
						}
						break;
					}
				}
			}
			if(dat[i][0] == 1 && dat[i][1] == p2 && butpress == 0){
				i ++;
			}else{
				for(int j = i;j < n;j ++){
					if(dat[j][0] == 1){
						if(dat[j][1] > p2) {
							p2 ++;
						}else if(dat[j][1] < p2){
							p2 --;
						}
						break;
					}
				}
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}

