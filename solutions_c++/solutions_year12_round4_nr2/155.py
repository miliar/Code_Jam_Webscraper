#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<cassert>
#define EPS 0.1
using namespace std;
struct dc{
	double rds;
	int id;
	bool operator<(const dc cp)const{
		if(rds!=cp.rds)
			return rds<cp.rds;
		return id<cp.id;
	}
};
double rdm(){
	double r=((double)rand())/((double)(RAND_MAX));
	assert(0.<=r && r<=1.);
	return r;
}
int t,n;
double w,l;
dc dcs[1002];
double lc[1002][2];
int aid[1002];
double dt(double a, double b, double c, double d){
	return (c-a)*(c-a)+(d-b)*(d-b);
}
bool mt(int d){
	for(int j=0;j<d;j++){
		if(dt(lc[d][0],lc[d][1],lc[j][0],lc[j][1])<(1+EPS)*(dcs[j].rds+dcs[d].rds)*(dcs[j].rds+dcs[d].rds))
			return false;
	}
	return true;
}
int main(){
	srand(48175);
	scanf("%d",&t);
	for(int z=1;z<=t;z++){
		scanf("%d %lf %lf",&n,&w,&l);
		for(int i=0;i<n;i++){
			//cin>>r[i];
			scanf("%lf",&(dcs[i].rds));
			dcs[i].id=i;
			dcs[i].rds=10000000000.-dcs[i].rds;
		}
		sort(dcs,dcs+n);
		for(int i=0;i<n;i++){
			dcs[i].rds=10000000000.-dcs[i].rds;
		}
		int i=-1;
		int ct=0;
		while(i<n-1){
			i++;
			lc[i][0]=0;
			lc[i][1]=0;
			ct=0;
			while(ct<20 && !mt(i)){
				lc[i][0]=rdm()*w;
				lc[i][1]=rdm()*l;
				ct++;
			}
			if(ct==20){
				i=-1;
				continue;
			}
		}
		/*
		cout<<"Case #"<<z<<":";
		for(int j=0;j<n;j++){
			cout<<" "<<lc[j][0]<<" "<<lc[j][1];
		}
		cout<<endl;*/
		for(int j=0;j<n;j++){
			aid[dcs[j].id]=j;
		}
		printf("Case #%d:",z);
		for(int j=0;j<n;j++){
			printf(" %.6lf %.6lf",lc[aid[j]][0],lc[aid[j]][1]);
		}
		printf("\n");
	}
	return 0;
}
