#include<stdio.h>


int t,tc;
int h,w;
int alt[102][102];
int bs[102][102];
int i,j,k;
int jb,n,o;
int mh,mw;

int ngalir(int sh,int sw){
	if(bs[sh][sw]==0){
		int nh=sh,nw=sw;
		if(alt[sh-1][sw]<alt[nh][nw]){
			nh=sh-1;
			nw=sw;
		}
		if(alt[sh][sw-1]<alt[nh][nw]){
			nh=sh;
			nw=sw-1;
		}
		if(alt[sh][sw+1]<alt[nh][nw]){
			nh=sh;
			nw=sw+1;
		}
		if(alt[sh+1][sw]<alt[nh][nw]){
			nh=sh+1;
			nw=sw;
		}
		if((nh==sh)&&(nw==sw)){
			jb++;
			bs[sh][sw]=jb;
		}
		else{
			bs[sh][sw]=ngalir(nh,nw);
		}
	}
	return bs[sh][sw];
}

int main(){
	freopen("ws22.in","r",stdin);
	freopen("ws22.out","w",stdout);

	scanf("%d",&t);
	for(tc=1;tc<=t;tc++){
		
		scanf("%d %d",&h,&w);

		for(i=0;i<h+2;i++)
			for(j=0;j<w+2;j++){
				alt[i][j]=99999;
				bs[i][j]=0;
			}

		for(i=1;i<=h;i++){
			for(j=1;j<=w;j++){
				scanf("%d",&alt[i][j]);
			}
		}
		/*
		for(i=1;i<=h;i++){
			for(j=1;j<=w;j++){
				printf("%d ",alt[i][j]);
			}
			printf("\n");
		}
		*/
		printf("Case #%d:\n",tc);
		////processs////
		jb=0;
		///cari highest alt yg blom di mark;
		for(i=1;i<=h;i++){
			for(j=1;j<=w;j++){
				printf("%c",ngalir(i,j)+96);
				if(j==w) printf("\n");
				else printf(" ");
			}
		}
		////////////////


	}

	return 0;
}