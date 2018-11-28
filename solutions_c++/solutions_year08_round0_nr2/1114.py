#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("B-large.in","r");
FILE *out=fopen("B-large.out","w");

int vis[2][200];

class gtr{
public:
	int s;
	int d;
}f[2][200];

bool cmp(gtr a,gtr b)
{
	if(a.s!=b.s)return a.s<b.s;
	return a.d<b.d;
}
int main()
{
	int tests,test,t;
	int i,n1,n2,j,p1,p2,h1,m1,h2,m2;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++){
		p1=p2=0;
		fscanf(in,"%d",&t);
		fscanf(in,"%d%d",&n1,&n2);
		for(i=0;i<n1;i++){
			fscanf(in,"%d:%d %d:%d",&h1,&m1,&h2,&m2);
			f[0][i].s=h1*60+m1;
			f[0][i].d=h2*60+m2;
		}
		for(i=0;i<n2;i++){
			fscanf(in,"%d:%d %d:%d",&h1,&m1,&h2,&m2);
			f[1][i].s=h1*60+m1;
			f[1][i].d=h2*60+m2;
		}
		sort(f[0],f[0]+n1,cmp);
		sort(f[1],f[1]+n2,cmp);
		int ret[2],minn,best,p;
		CLR(vis,0);
		CLR(ret,0);
		while(p1<n1 || p2<n2){
			minn=1<<30;
			if(p1<n1 && f[0][p1].s<minn){
				minn=f[0][p1].s;
				best=0;
				p=p1;
			}
			if(p2<n2 && f[1][p2].s<minn){
				minn=f[1][p2].s;
				best=1;
				p=p2;
			}
			vis[best][p]=1;
			ret[best]++;
			int curtime=f[best][p].d,cur=!best;
			while(1){
				curtime+=t;
				int size=(cur==0)?n1:n2;
				int ver=0;
				
				int B1=-1;
				for(i=0;i<size;i++){
					if(f[cur][i].s>=curtime && !vis[cur][i]){
						B1=i;
						break;
					}
				}

				if(B1==-1)break;
				vis[cur][B1]=1;
				curtime=f[cur][B1].d;
				cur=!cur;
			}
			while(vis[0][p1] && p1<n1)p1++;
			while(vis[1][p2] && p2<n2)p2++;
		}
		fprintf(out,"Case #%d: %d %d\n",test+1,ret[0],ret[1]);	
	}
	return 0;
}