#include<stdio.h>
#include<stdlib.h>
int main(){
	int T;
	int N;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		scanf("%d ",&N);
		int o = 1;
		int b = 1;
		char pre_c = '\0';
		int ans = 0;
		int this_path = 0;
		int pre_path = 0;
		for(int i=0;i<N;i++){
			char tmpc;
			int tmp;
			scanf("%c %d ",&tmpc,&tmp);
			if(tmpc == pre_c){
				if(tmpc == 'B'){
					ans += abs(tmp - b) + 1;
					pre_path += abs(tmp - b) + 1;
					b = tmp;
				}else if(tmpc == 'O'){
					ans += abs(tmp - o) + 1;
					pre_path += abs(tmp - o) + 1;
					o = tmp;
				}		
			}else{

				if(tmpc == 'B'){
					this_path = abs(tmp - b) + 1;
					b = tmp;
				}else if(tmpc == 'O'){
					this_path = abs(tmp - o) + 1;
					o = tmp;
				}		
				if(pre_path >= this_path){
					ans += 1;
					pre_path = 1;
				}else{
					ans += (this_path - pre_path);
					pre_path = this_path - pre_path ;
				}
			}
			pre_c = tmpc;
		}
		printf("Case #%d: %d\n",t + 1,ans);
	}
	return 0;
}
