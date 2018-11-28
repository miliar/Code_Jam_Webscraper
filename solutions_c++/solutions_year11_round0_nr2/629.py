#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
struct com{
	char a;
	char b;
	char c;
};
struct opp{
	char a;
	bool aa;
	char b;
	bool bb;
};
struct com coms[36];
struct opp opps[28];
char out[100];
int num=0;
char now=NULL;
char last=NULL;
void clear(){
	for(int i=0;i<28;i++){
		opps[i].aa=false;
		opps[i].bb=false;
	}
	last=NULL;
	now=NULL;
	num=0;
}
void clear_all(){
	for(int i=0;i<36;i++){
		coms[i].a=NULL;
		coms[i].b=NULL;
		coms[i].c=NULL;
	}
	for(int i=0;i<28;i++){
		opps[i].a=NULL;
		opps[i].b=NULL;
		opps[i].aa=false;
		opps[i].bb=false;
	}
	last=NULL;
	now=NULL;
	num=0;
}
void run(int casen) {
	int c=0;
	int d=0;
	int n=0;
	clear_all();
	scanf("%d",&c);
	for(int i=0;i<c;i++){
		scanf("%c",&now);
		scanf("%c",&now);
		coms[i].a=now;
		
		scanf("%c",&now);
		coms[i].b=now;
		
		scanf("%c",&now);
		coms[i].c=now;
	}
	scanf("%d",&d);
	for(int i=0;i<d;i++){
		scanf("%c",&now);
		scanf("%c",&now);
		opps[i].a=now;
		
		scanf("%c",&now);
		opps[i].b=now;
	}
	scanf("%d",&n);
	
	
	scanf("%c",&now);
	for(int i=0;i<n;i++){
		
		scanf("%c",&now);
		
		//normol
		
		
		//com
		if(last!=NULL){
			//printf("com\n");
			for(int i=0;i<c;i++){
				if((last==coms[i].a  && now==coms[i].b)||(last==coms[i].b  && now==coms[i].a)){
					last=coms[i].c;
					now=NULL;
				//printf("com--%c\n",last);
				}
			}
			//opp
		}
		if(now!=NULL){
			//printf("opp\n");
			
			for(int i=0;i<d;i++){
				if(last==opps[i].a){
				
					opps[i].aa=true;
					
				}
				if(last==opps[i].b){
				
					opps[i].bb=true;
					
				}
				if(now==opps[i].a){
				
					//opps[i].aa=true;
					if(opps[i].bb==true){
						clear();
					}
				}
				if(now==opps[i].b){
				
					//opps[i].bb=true;
					if(opps[i].aa==true){
						clear();
					}
				}
			}
		}
		if(last==NULL){
			last=now;
			now=NULL;
			continue;
		}
		if(now!=NULL){
			out[num]=last;
			num++;
			last=now;
			now=NULL;
		}
	}
	if(last!=NULL){
		out[num]=last;
		num++;
	}
	printf("Case #%d: [",casen);
	for(int i=0;i<num;i++){
		if(i==0)
			printf("%c",out[i]);
		else
			printf(", %c",out[i]);
	}
	printf("]\n");
}

int main(int argc, char* argv[]) {
	int ncases=0;
	freopen(argv[1], "rt", stdin);
	freopen("A.out", "wt", stdout);
	scanf("%d",&ncases); 
	for(int i=1;i<=ncases;i++) 
	run(i);
	return 0;
}
