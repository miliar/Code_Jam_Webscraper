/*
TASK: G2011_2_1 - Airport Walkways
LANG: C++
NAME: untitled.cpp
*/
#include <cstdio>
#include <algorithm>

#define NMAX 3000

using namespace std;

struct NODE
{
	double b,e,s;
};
bool operator<(const NODE &left,const NODE &right)
{
	return left.s<right.s;
};

NODE table[NMAX];

void func()
{
	double x,s,r,t; int n; scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
	int size=0; double cur=0.0l;
	for(int i=0;i<n;i++){
		double b,e,w; scanf("%lf%lf%lf",&b,&e,&w);
		table[size].b = cur; table[size].e = b; table[size].s = 0.0l; size++;
		table[size].b = b; table[size].e = e; table[size].s = w; size++;
		cur = e;
	}
	table[size].b = table[size-1].e; table[size].e = x; table[size].s = 0.0l; size++;
	sort(table,table+size);

	double ret=0.0l,amt=t;
	for(int i=0;i<size;i++){
		double tmp = (table[i].e-table[i].b)/(table[i].s+r);
		if(tmp>amt){
			ret += amt+(table[i].e-table[i].b-amt*(table[i].s+r))/(table[i].s+s);
			amt = 0.0l;
		}else{
			ret += tmp;
			amt -= tmp;
		}
	}

	printf("%.10lf\n",ret);

	return;
}

int main()
{
	FILE *fin=NULL,*fout=NULL;
	fin = freopen("input.txt","r",stdin);
	fout = freopen("output.txt","w",stdout);

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