#include<stdio.h>
#include<algorithm>
#define max 1000
FILE *in=fopen("INPUT.TXT","r");
FILE *out=fopen("OUTPUT.TXT","w");
struct _WW{
	double b,e,w;
};
double x,s,r,t;
int n;
double res;
_WW w[max+5];
bool compare(_WW a,_WW b){
	return a.w<b.w;
}
void input(){
	fscanf(in,"%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
	for(int i=0;i<n;i++){
		fscanf(in,"%lf%lf%lf",&w[i].b,&w[i].e,&w[i].w);
	}
}
void process(){
	res=0;
	std::sort(w,w+n,compare);
	for(int i=0;i<n;i++) x-=(w[i].e-w[i].b);
	if(t*r>=x){
		t-=(double)x/r;
		res+=(double)x/r;
	}
	else{
		res+=(double)(x-(t*r))/s;
		res+=t;
		t=0;
	}
	for(int i=0;i<n;i++){
		double id=(w[i].e-w[i].b);
		if(t*(r+w[i].w)>=id){
			t-=(double)id/(r+w[i].w);
			res+=(double)id/(r+w[i].w);
		}
		else{
			res+=(double)(id-(t*(r+w[i].w)))/(s+w[i].w);
			res+=t;
			t=0;
		}
	}
}
void output(int tc){
	fprintf(out,"Case #%d: %.7lf\n",tc,res);
}
int main(){
	int t;
	fscanf(in,"%d",&t);
	for(int i=0;i<t;i++){
		input();
		process();
		output(i+1);
	}
	fcloseall();
	return 0;
}
