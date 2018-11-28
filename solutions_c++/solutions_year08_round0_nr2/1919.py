#include<stdio.h>
#include<stdlib.h>
int main(){
	int ca,te,t,nb,na,tmp,ansa,ansb,at,bt,qq,check;
	int timead[66],timeaa[66],timebd[66],timeba[66],useda[66],usedb[66],mina,minb,flaga,flagb;
	int h,m,i,j,tmpa,tmpb,now;
	scanf("%d",&ca);
	for(te=0;te<ca;te++){
		printf("Case #%d: ",te+1);
		scanf("%d",&t);
		scanf("%d %d",&na,&nb);
		for(i=0;i<na;i++){
			scanf("%d:%d",&h,&m);
			timead[i] = h*60 + m - t;
			scanf("%d:%d",&h,&m);
			timeaa[i] = h*60 + m;
		}
		for(i=0;i<nb;i++){
			scanf("%d:%d",&h,&m);
			timebd[i] = h*60 + m - t;
			scanf("%d:%d",&h,&m);
			timeba[i] = h*60 + m;
		}
		for(i=0;i<na;i++){
			for(j=0;j<na-1;j++){
				if(timead[j] > timead[j+1]){
					tmp = timead[j];
					timead[j] = timead[j+1];
					timead[j+1] = tmp;
					tmp = timeaa[j];
					timeaa[j] = timeaa[j+1];
					timeaa[j+1] = tmp;
				}
			}
		}
		for(i=0;i<nb;i++){
			for(j=0;j<nb-1;j++){
				if(timebd[j] > timebd[j+1]){
					tmp = timebd[j];
					timebd[j] = timebd[j+1];
					timebd[j+1] = tmp;
					tmp = timeba[j];
					timeba[j] = timeba[j+1];
					timeba[j+1] = tmp;
				}
			}
		}
		at = 0;
		bt = 0;
		ansa = ansb = 0;
		for(i=0;i<na;i++)
			useda[i] = 0;
		for(i=0;i<nb;i++)
			usedb[i] = 0;
		now = 0;
		while(1){
			mina = 99999;
			minb = 99999;
			tmpa = at;
			tmpb = bt;
			for(i=0;i<na;i++){
				if(mina > timead[i] && useda[i] == 0){
					flaga = i;
					mina = timead[i];
				}
			}

			for(i=0;i<nb;i++){
				if(minb > timebd[i] && usedb[i] == 0){
					minb = timebd[i];
					flagb = i;
				}
			}
			if(mina == 99999 && minb == 99999)
				break;
			if(mina < minb)
				now = mina;
			else
				now = minb;
			for(i=0;i<na;i++){
				if(useda[i] == 1 && timeaa[i] <= now){
					useda[i] = 2;
					bt++;
				}
			}
			for(i=0;i<nb;i++){
				if(usedb[i] == 1 && timeba[i] <= now){
					usedb[i] = 2;
					at++;
				}
			}
			if(mina < minb){
				useda[flaga] = 1;
				if(at == 0){
					ansa++;
				}else{
					at--;
				}
				now = mina;
			}else{
				usedb[flagb] = 1;
				if(bt == 0){
					ansb++;
				}else{
					bt--;
				}
				now = minb;
			}
		}
		printf("%d %d\n",ansa,ansb);
	}
	return 0;
}
