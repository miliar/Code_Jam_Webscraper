#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>

int N,M;
struct s_d{
	char s[100];
	int x;
}dd[10000000];
int dn;

inline void hmy(char *s,int wh){
	int sn,i,ct=0;
	char *s2;
	s2=strtok(s,"/");
	strcpy(dd[dn].s,s2);
	dd[dn++].x=wh;
	while(s2=strtok(0,"/")){
		strcpy(dd[dn].s,dd[dn-1].s);
		strcat(dd[dn].s,s2);
		dd[dn++].x=wh;
	}
}
void pnt(){
	int i;
	for(i=0;i<dn;i++)
		printf("==%s==%d==\n",dd[i].s,dd[i].x);
}

main(){
	int zz,zn,i,ans,mn,xx,k,kk,j;
	char ss[100000];
	scanf("%d",&zz);
	for(zn=1;zn<=zz;zn++){
		scanf("%d%d",&N,&M);
		dn=0;
		for(i=0;i<N;i++){
			scanf("%s",ss);
			hmy(ss,0);
		}
		for(i=0;i<M;i++){
			scanf("%s",ss);
			hmy(ss,1);
		}
		//pnt();
		//pnt();
		/********************************/
		for(i=0,kk=0;i<dn;i++){
			for(j=0;j<i;j++){
				if(strcmp(dd[i].s,dd[j].s)==0)break;
			}
			if(i==j&&dd[i].x==1)kk++;
		}
		
		printf("Case #%d: %d",zn,kk);
		printf("\n");
	}
}
