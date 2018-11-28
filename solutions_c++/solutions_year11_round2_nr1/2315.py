#include<stdio.h>
#define MAX 102
double WP[MAX],OWP[MAX],OOWP[MAX];
double temp_WP[MAX];
char schedule[MAX][MAX];
int T,caseno,n,exclude[MAX];
void init(int flag){
		if(flag==1){//temp_WP
			int i;
			for(i=1;i<=n;i++){
				temp_WP[i]=0.0;
				exclude[i]=0;
		}
	}
		
}

void calculate_WP(){
		int i,j,k;
		int wins=0,total=0;
		for(i=1;i<=n;i++){
			wins=0;total=0;
			for(j=1;j<=n;j++){
				if(schedule[i][j]=='1'){
					wins++;
					total++;
				}
				if(schedule[i][j]=='0'){
					total++;
				}
			}
			WP[i]=(double)wins/(double)total;
		}
}

void calculate_OWP(){
		int i,j,current_team,k;
		int wins=0,total=0;
		int divide_by=0;
		for(current_team=1;current_team<=n;current_team++){
				init(1);
				k=0;
				divide_by=0;
				for(i=1;i<=n;i++){
					wins=0;total=0;
					if(i!=current_team){
						for(j=1;j<=n;j++){
								if(j!=current_team){
									if(schedule[i][j]=='1'){
									wins++;
									total++;
									}
									if(schedule[i][j]=='0'){
										total++;
									}
								}
							}
					}
					if(total!=0){
						temp_WP[i]=(double)wins/(double)total;
						divide_by++;
					}
					else{
						divide_by--;
						exclude[current_team]=1;
					}
		//			if(current_team==4)
		//				printf("%d %f\t",divide_by,temp_WP[i]);
				}
		//		printf("\n");
				
			double sum=0.0;
			divide_by=0;
			for(i=1;i<=n;i++){
					if(schedule[i][current_team]=='.');
					else{
						sum+=temp_WP[i];
						divide_by++;
					}
					
			}
			OWP[current_team]=sum/divide_by;
		}
}

void calculate_OOWP(){
		int i,j,current_team;
		double sum=0.0;
		int divide_by=0;
		for(current_team=1;current_team<=n;current_team++){
				sum=0.0;
				divide_by=0;
				for(i=1;i<=n;i++){
						if(schedule[current_team][i]=='.');
						else{
							sum+=OWP[i];
							divide_by++;
						}
				}
				OOWP[current_team]=sum/divide_by;
		}
}

int main(){
		char c;
		int i,j,k;
		scanf("%d",&T);
		caseno=1;
		while(caseno<=T){
				scanf("%d%c",&n,&c);
				for(i=1;i<=n;i++){
					for(j=1;j<=n;j++){
						scanf("%c",&schedule[i][j]);
					}
					scanf("%c",&c);
				}
		//		for(i=1;i<=n;i++){
		//			for(j=1;j<=n;j++){
		//					printf("%c",schedule[i][j]);
		//			}
		//		printf("\n");	
		//		}
				calculate_WP();
		/*		for(i=1;i<=n;i++){
					printf("%f\t",WP[i]);
				}
				printf("\n");*/
				calculate_OWP();/*
				for(i=1;i<=n;i++){
					printf("%f\t",OWP[i]);
				}
				printf("\n");*/
				calculate_OOWP();/*
				for(i=1;i<=n;i++){
					printf("%f\t",OOWP[i]);
				}
				printf("\n");*/
				printf("Case #%d:\n",caseno);
				for(i=1;i<=n;i++){
						printf("%f\n",0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i]);
				}
				caseno++;
		}
		
		return 0;
}
