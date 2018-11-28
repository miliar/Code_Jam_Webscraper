/*
TASK: G2011_1B_2 - Revenge of the Hot Dogs
LANG: C++
NAME: untitled.cpp
*/
#include <cstdio>
#include <algorithm>

#define CMAX 200
#define EPS 1e-9l
#define DBLMAX 1e30l

using namespace std;

pair<double,int> table[CMAX]; //(p,v)
int c;
double d;

bool check(double t)
{
	double range=-DBLMAX;
	for(int i=0;i<c;i++){
		if(range<table[i].first){
			if(range+d<table[i].first-t){
				double pos=table[i].first-t+d*(double)(table[i].second-1);
				if(pos>table[i].first+t) return false;
				range = pos;
			}else{
				double pos=range+d+d*(double)(table[i].second-1);
				if(pos>table[i].first+t) return false;
				range = pos;
			}
		}else{
			double pos=range+d*(double)table[i].second;
			if(pos>table[i].first+t) return false;
			range = pos;
		}
	}

	return true;
}

void func()
{
	int cnt=0; scanf("%d%lf",&c,&d);
	for(int i=0;i<c;i++){
		scanf("%lf%d",&table[i].first,&table[i].second);
		cnt += table[i].second;
	}
	sort(table,table+c);

	double left=0.0l,right=d*(double)cnt*2.0l;
	while(right-left>EPS&&(right-left)/right>EPS){
		double mid=(left+right)/2.0l;
		if(check(mid)){
			right = mid;
		}else{
			left = mid;
		}
	}
	if(check(left)){
		right = left;
	}

	printf("%.10lf\n",right);

	return;
}

int main()
{
	FILE *fin=NULL,*fout=NULL;
	fin = freopen("input.txt","r",stdin);
	fout = freopen("output.txt","w",stdout);

	//ìÒï™íTçıÅB

	int t; scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		func();
	}

	//finalize
	if(NULL!=fin) fclose(fin);
	if(NULL!=fout) fclose(fout);

	return 0;
}