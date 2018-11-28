#include <conio.h>
#include <stdio.h>
#include <iostream.h>
#include <stdlib.h>
int taua,taub;
struct time{
	int h,m;
};
void hoanvi(struct time &a,struct time &b){
	struct time t;
	t=a;a=b;b=t;
}
void xoapt(int &n,struct time start[250],struct time end[250],int vitri){
	for (int i=vitri;i<n-1;i++){
		hoanvi(start[i],start[i+1]);hoanvi(end[i],end[i+1]);
	}
	--n;
}
void chen(int &n,struct time start[250],struct time end[250],struct time x){
	for (int i=0;i<n;i++){
		if (end[i].h==-1) {++i; continue;}
		if (start[i].h>x.h) break;
		else if (start[i].h==x.h&&start[i].m>=x.m) break;
	}
	if (i<n){
		int vitri=i;++n;
		for (i=n;i>vitri;i--){
			start[i]=start[i-1];	end[i]=end[i-1];
		}
		start[vitri]=x;	end[vitri].h=-1;
	}
}
main()
{
	FILE *fptr,*fout;
	char filena[]="d:\\bt c\\de\\google\\loai\\b.txt";
	char naout[]="d:\\bt c\\de\\google\\loai\\bout.txt";
	if ((fptr=fopen(filena,"r"))==NULL) {
		printf("file co loi ");
		exit(0);
	}
	fout=fopen(naout,"w+");
	int ntime,ptime,j,turn,na,nb,i;
	struct time starta[250],startb[250],enda[250],endb[250];
	char c;
	fscanf(fptr,"%d",&ntime);
	for (ptime=0;ptime<ntime;ptime++){
		fscanf(fptr,"%d%d%d",&turn,&na,&nb);
		for (j=0;j<na;j++){
			starta[j].h=enda[j].h=starta[j].m=enda[j].m=0;
			c=fgetc(fptr);c=fgetc(fptr);starta[j].h=(c-'0')*10;
			c=fgetc(fptr);starta[j].h+=(c-'0');c=fgetc(fptr);c=fgetc(fptr);
			starta[j].m=(c-'0')*10;	c=fgetc(fptr);starta[j].m+=c-'0';

			c=fgetc(fptr);c=fgetc(fptr);enda[j].h=(c-'0')*10;
			c=fgetc(fptr);enda[j].h+=(c-'0');c=fgetc(fptr);c=fgetc(fptr);
			enda[j].m=(c-'0')*10;c=fgetc(fptr);enda[j].m+=c-'0';
		}
		for (j=0;j<nb;j++){
			startb[j].h=endb[j].h=startb[j].m=endb[j].m=0;
			c=fgetc(fptr);c=fgetc(fptr);startb[j].h=(c-'0')*10;
			c=fgetc(fptr);startb[j].h+=(c-'0');c=fgetc(fptr);c=fgetc(fptr);
			startb[j].m=(c-'0')*10;c=fgetc(fptr);startb[j].m+=c-'0';

			c=fgetc(fptr);c=fgetc(fptr);
			endb[j].h=(c-'0')*10;c=fgetc(fptr);endb[j].h+=(c-'0');
			c=fgetc(fptr);c=fgetc(fptr);endb[j].m=(c-'0')*10;
			c=fgetc(fptr);endb[j].m+=c-'0';
		}
		for (i=0;i<na-1;i++)
			for (j=na-2;j>=i;j--){
				if (starta[j].h>starta[j+1].h){
					hoanvi(starta[j],starta[j+1]);	hoanvi(enda[j],enda[j+1]);
				}
				else if (starta[j].h==starta[j+1].h)
					if (starta[j].m>starta[j+1].m){
						hoanvi(starta[j],starta[j+1]);	hoanvi(enda[j],enda[j+1]);
					}
			}
		for (i=0;i<nb-1;i++)
			for (j=nb-2;j>=i;j--){
				if (startb[j].h>startb[j+1].h){
					hoanvi(startb[j],startb[j+1]);	hoanvi(endb[j],endb[j+1]);
				}
				else if (startb[j].h==startb[j+1].h)
					if (startb[j].m>startb[j+1].m){
						hoanvi(startb[j],startb[j+1]);					hoanvi(endb[j],endb[j+1]);
					}
			}
		printf("%d\n",ptime+1);
		for (i=0;i<na;i++) printf("%2d:%2d %2d:%2d\n",starta[i].h,starta[i].m,enda[i].h,enda[i].m);
		printf("\n");
		for (i=0;i<nb;i++) printf("%2d:%2d %2d:%2d\n",startb[i].h,startb[i].m,endb[i].h,endb[i].m);
		printf("\n\n");
		getch();
		i=0;j=0; int br=0;
		taua=0;taub=0;
		struct time tam;
		while (i<na&&j<nb){
			int t;
			do{
				t=0;
				while (enda[i].h==-1&&i<na) {
					tam.m=enda[i+1].m+turn;	tam.h=enda[i+1].h+tam.m/60;tam.m%=60;
					chen(nb,startb,endb,tam);
					i=i+2; t=1;
				}
				while (endb[j].h==-1&&j<nb) {
					tam.m=endb[j+1].m+turn;	tam.h=endb[j+1].h+tam.m/60;tam.m%=60;
					chen(na,starta,enda,tam);
					j=j+2; t=1;
				}
				if (i>=na||j>=nb) {br=1; break;}
			}while (t!=0);
			if (br) break;
			if (starta[i].h<startb[j].h){
				++taua;
				tam.m=enda[i].m+turn;tam.h=enda[i].h+tam.m/60;tam.m%=60;
				chen(nb,startb,endb,tam);
				++i;
//				xoapt(na,starta,enda,i);
			} else if (starta[i].h>startb[j].h){
				++taub;
				tam.m=endb[j].m+turn;tam.h=endb[j].h+tam.m/60;tam.m%=60;
				chen(na,starta,enda,tam);
				++j;
//				xoapt(nb,startb,endb,j);
			}
			else {
				if (starta[i].m<startb[j].m){
					++taua;
					tam.m=enda[i].m+turn;tam.h=enda[i].h+tam.m/60;tam.m%=60;
					chen(nb,startb,endb,tam);
					++i;
//					xoapt(na,starta,enda,i);
				} else {
					++taub;
					tam.m=endb[j].m+turn;tam.h=endb[j].h+tam.m/60;tam.m%=60;
					chen(na,starta,enda,tam);
					++j;
//					xoapt(nb,startb,endb,j);
				}
			}
		}
		while (i<na) if (enda[i].h==-1) i+=2;else {++taua;++i;}
		while (j<nb) if (endb[j].h==-1) j+=2;else {++taub;++j;}

		fprintf(fout,"Case #%d: %d %d\n",ptime+1,taua,taub);
	}
}