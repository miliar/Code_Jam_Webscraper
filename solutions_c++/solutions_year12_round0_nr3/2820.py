#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
void kuriagari(char tansaku[],int keta){
	int i=0;
	while(tansaku[i]>9){
		tansaku[i+1] += tansaku[i]/10;
		tansaku[i] = tansaku[i] - (tansaku[i]/10)*10;
		i++;
	}
}

void kasan(char tansaku[],int keta){
	tansaku[0]+=1;
	if(tansaku[0]>9) kuriagari(tansaku,keta);
}

int settei(char tansaku[],int n){
	int i=6,j=0;
	int num=1000000;
	for(;i>=0;i--){
		if(num<=n){
			if(j==0) j=i+1;
			tansaku[i]=n/num;
			n-=num*(n/num);
		}
		num = num/10;
	}
	return j;
}
int big(char tansaku[],char* big,int keta){
	int i=keta-1;
	for(;i>=0;i--){
		if(tansaku[i]>*(big+i)) return 0; //¬‚³‚¢
		if(tansaku[i]<*(big+i)) return 1; //‘å‚«‚¢
	}
	return 2; //“™‚µ‚¢
}

void refresh(char gyo[]){
	for(int i=0;i<7;i++){
		gyo[i]=0;
	}
}


int main(){
	FILE *fp,*fp2;
	fp=fopen("C-large.in","r");
	fp2=fopen("answerClarge.out","w");
	char input[256];
	fgets(input,256,fp);
	int count=atoi(input);
	char tansaku[7]={0,0,0,0,0,0,0};
	char *hikakuyou = (char *)malloc(14);
	char bignum[7] ={0,0,0,0,0,0,0};
	char smallnum[7] ={0,0,0,0,0,0,0};
	int hakken=0;
	char kiroku1[7] = {0,0,0,0,0,0,0};
	char kiroku2[7] = {0,0,0,0,0,0,0};
	char kiroku3[7] = {0,0,0,0,0,0,0};
	char kiroku4[7] = {0,0,0,0,0,0,0};
	char kiroku5[7] = {0,0,0,0,0,0,0};
	char kiroku6[7] = {0,0,0,0,0,0,0};
	char kiroku7[7] = {0,0,0,0,0,0,0};
	char* kiroku[] = {kiroku1,kiroku2,kiroku3,kiroku4,kiroku5,kiroku6,kiroku7};
	char *kk;
	int a,b,c;
	int j=1;
	int keta;
	int answer=0;
	while(fgets(input,256,fp) != NULL){
		refresh(tansaku);
		refresh(bignum);
		refresh(smallnum);
		refresh(hikakuyou);
		refresh(hikakuyou+7);
		answer=0;
		sscanf(input,"%d %d",&a,&b);
		c=b;
		b=b-a;
		keta=settei(tansaku,a);
		memcpy(smallnum,tansaku,7);
		settei(bignum,c);
		kasan(tansaku,keta);
		while(b>0){
			memcpy(hikakuyou,tansaku,keta);
			
			
			for(int i=0;i<keta-1;i++){
				/*roop*/
				kk = hikakuyou+keta;
				*kk=*hikakuyou;
				hikakuyou +=1;
				
				if(big(hikakuyou,tansaku,keta)==1&&big(hikakuyou,bignum,keta)&&big(smallnum,hikakuyou,keta)){
					
					answer++;hakken++;
					memcpy(kiroku[hakken-1],hikakuyou,keta);
					//fprintf(fp2,"%dsuc:%d%d%d%d%d%d , %d%d%d%d%d%d\n", answer,tansaku[5],tansaku[4],tansaku[3],tansaku[2],tansaku[1],tansaku[0],hikakuyou[5],hikakuyou[4],hikakuyou[3],hikakuyou[2],hikakuyou[1],hikakuyou[0]);
					for(int n=0;n<hakken-1;n++){
						if(big(kiroku[n],hikakuyou,keta)==2){
							refresh(kiroku[hakken-1]);
							answer--;
							
							break;
						}
					}
				}
			}
			hikakuyou=hikakuyou - keta +1;
			for(int n=0;n<7;n++){
				refresh(kiroku[n]);
			}
			refresh(hikakuyou);
			refresh(hikakuyou+7);
			/*
			if(hakken>0){
			fprintf(fp2,"num=%d%d%d%d%d\n",tansaku[4],tansaku[3],tansaku[2],tansaku[1],tansaku[0]);
			fprintf(fp2,"hakken=%d\n",hakken);
			}
			*/
			kasan(tansaku,keta);
			hakken=0;
			b--;
		}
		fprintf(fp2,"Case #%d: %d\n",j,answer);
		j++;
		count--;
		if(count==0) break;
	}
		free(hikakuyou);
		fclose(fp);
		fclose(fp2);
}