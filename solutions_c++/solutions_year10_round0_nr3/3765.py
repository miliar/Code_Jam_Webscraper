#include <stdio.h>

int main(){
	int tcase=0;
	int cases,runs,limit,groups;
	int euros;
	int persons[10];
	int pointer;
	int temp;
	scanf("%d",&cases);
	for(tcase=1;tcase<=cases;++tcase){
		scanf("%d %d %d",&runs,&limit,&groups);
		for(int i=0;i<groups;++i){
			scanf("%d",persons+i);	
		}
		printf("Case #%d: ",tcase);
		pointer=0;
		euros=0;
		for(int i=0;i<runs;++i){
			temp=0;
			for(int j=0;j<groups;++j){
				if(temp+persons[pointer]<=limit){
					temp+=persons[pointer];
					pointer=(pointer+1) % groups;
				}else{
					break;	
				}
			}
			euros+=temp;
		}
		printf("%d\n",euros);
	}
	return 0;	
}