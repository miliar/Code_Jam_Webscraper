#include<stdio.h>
#define max 100
FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");
struct _TEAM{
	double wp,owp,oowp,rpi;
	int cg,cw;
};
int n;
_TEAM t[max+5];
char sch[max+5][max+5];
void input(){
	fscanf(in,"%d",&n);
	for(int i=0;i<n;i++){
		fscanf(in,"%s",sch[i]);
	}
}
void wp(){
	for(int i=0;i<n;i++){
		t[i].cg=t[i].cw=0;
		for(int j=0;j<n;j++){
			if(sch[i][j]=='.') continue;
			t[i].cg++;
			if(sch[i][j]=='1') t[i].cw++;
		}
		t[i].wp=(double)t[i].cw/t[i].cg;
	}
}
void owp(){
	for(int i=0;i<n;i++){
		double swp=0;
		for(int j=0;j<n;j++){
			if(sch[i][j]=='.') continue;
			if(sch[i][j]=='1') swp+=(double)(t[j].cw)/(t[j].cg-1);
			else swp+=(double)(t[j].cw-1)/(t[j].cg-1);
		}
		t[i].owp=swp/t[i].cg;
	}
}
void oowp(){
	for(int i=0;i<n;i++){
		double sowp=0;
		for(int j=0;j<n;j++){
			if(sch[i][j]=='.') continue;
			sowp+=t[j].owp;
		}
		t[i].oowp=sowp/t[i].cg;
	}
}
void rpi(){
	for(int i=0;i<n;i++){
		t[i].rpi=0.25*t[i].wp+0.50*t[i].owp+0.25*t[i].oowp;
	}
}
void process(){
	wp();
	owp();
	oowp();
	rpi();
}
void output(int tc){
	fprintf(out,"Case #%d:\n",tc);
	for(int i=0;i<n;i++){
		fprintf(out,"%.12lf\n",t[i].rpi);
	}
}
int main(){
	int t;
	fscanf(in,"%d",&t);
	for(int i=0;i<t;i++){
		input();
		process();
		output(i+1);
	}
	return 0;
}
