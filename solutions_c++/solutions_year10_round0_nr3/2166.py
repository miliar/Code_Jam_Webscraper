#include<stdio.h>
void thame(){
	int round,seat,group,people[1000];
	int sum,s,r;
	int i;
	scanf("%i%i%i",&round,&seat,&group);
	sum=0;
	for(i=0;i<group;i++){
		scanf("%i",&people[i]);
		sum+=people[i];
	}
	if(sum<=seat) printf("%i",sum*round);
	else{
		r=s=sum=0;
		i=0;
		while(r<round){
			s+=people[i];
			if(s>seat){
                  sum+=s-people[i];
                  r++;
                  s=people[i];
            }
            i=(i+1)%group;
		}
		printf("%i",sum);
	}
	
}
int main(){
	int x;
	int i;
	scanf("%i",&x);
	for(i=0;i<x;i++){
		printf("Case #%i: ",i+1);
		thame();
		printf("\n");
	}
	return 0;
}
