#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
using namespace std;

const int dir[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
vector<pair<int,int> > p;
vector<pair<int,int> > seg;
int in[7000],mn[7000],mx[7000],d1[7000],d2[7000],d3[7000],d4[7000];
int n;

void input() {
	scanf("%d",&n);
	int dd=0,x=0,y=0,t;
	char tmp[64];
	p.push_back(make_pair(x,y));
	for(int i=0;i<n;i++) {
		scanf("%s %d",tmp,&t);
		for(;t;t--) for(int j=0;tmp[j];j++)
		if (tmp[j]=='F') {
			x+=dir[dd][0],y+=dir[dd][1];
			p.push_back(make_pair(x,y));
		}
		else if (tmp[j]=='L') dd=(dd+3)%4;
		else dd=(dd+1)%4;
	}
}

int area() {
	int ret=0;
	int n=p.size();
	for(int i=0;i<n;i++) {
		ret+=p[(i+1)%n].first*p[i].second-p[(i+1)%n].second*p[i].first;
	}
	return abs(ret)/2;
}

void run(int T) {
	p.clear(),seg.clear();
	input();
	int s=area();
	int m=p.size();
	for(int i=0;i<m;i++)
		if (p[i].first==p[(i+1)%m].first) {
			if (p[(i+1)%m].second>p[i].second) seg.push_back(p[i]);
			else seg.push_back(p[(i+1)%m]);
		}
	sort(seg.begin(),seg.end());
	for(int i=0;i<7000;i++) mx[i]=-100000000,mn[i]=1000000000;
	for(int i=0;i<seg.size();i++) {
		int x=seg[i].first,y1=seg[i].second;
		y1+=3000;
		mn[y1]=min(mn[y1],x);
		mx[y1]=max(mx[y1],x);
	}
	for(int i=6999;i>=0;i--) d1[i]=mn[i],d3[i]=mx[i];
	for(int i=6998;i>=0;i--) d1[i]=min(d1[i],d1[i+1]),d3[i]=max(d3[i],d3[i+1]);
	for(int i=0;i<7000;i++) d2[i]=mx[i],d4[i]=mn[i];
	for(int i=1;i<7000;i++) d2[i]=max(d2[i],d2[i-1]),d4[i]=min(d4[i],d4[i-1]);
	int s1=0;
	for(int i=0;i<7000;i++)
	if (mx[i]>mn[i]) {
		s1+=min(d2[i],d3[i])-max(d1[i],d4[i]);
	}
	printf("Case #%d: %d\n",T,s1-s);
}

int main() {
	int N,cs=0;
	for(scanf("%d",&N);N--;)
		run(++cs);
	return 0;
}
