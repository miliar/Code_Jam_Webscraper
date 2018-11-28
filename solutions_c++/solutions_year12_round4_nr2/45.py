#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxn=1001;
const int oo=(1<<30);
int n,w,l;
int r[maxn],id[maxn];
int px[maxn],py[maxn];
int ansx[maxn],ansy[maxn];

void qsort(int left,int right){
	int i=left;
	int j=right;
	int mid=r[(left+right)>>1];
	int midid=id[(left+right)>>1];
	do{
		while ((r[i]>mid)||((r[i]==mid)&&(id[i]<midid))){
			i++;
		}
		while ((r[j]<mid)||((r[j]==mid)&&(id[j]>midid))){
			j--;
		}
		if (i<=j){
			swap(r[i],r[j]);
			swap(id[i],id[j]);
			i++;
			j--;
		}
	} while (i<=j);
	if (left<j){
		qsort(left,j);
	}
	if (i<right){
		qsort(i,right);
	}
	return;
}

void init(){
	scanf("%d%d%d",&n,&w,&l);
	memset(r,0,sizeof(r));
	for (int i=1;i<=n;i++){
		scanf("%d",&r[i]);
		id[i]=i;
	}
	qsort(1,n);
	memset(px,0,sizeof(px));
	memset(py,0,sizeof(py));
	return;
}

bool nocollision(int tx,int ty,int p){
	if ((tx+r[p]<0)||(tx+r[p]>w)||(ty+r[p]<0)||(ty+r[p]>l)){
		return false;
	}
	for (int i=1;i<p;i++){
		if ((px[i]<(tx+(r[p]<<1)))&&(px[i]>(tx-(r[i]<<1)))&&(py[i]<(ty+(r[p]<<1)))&&(py[i]>(ty-(r[i]<<1)))){
			return false;
		}
	}
	return true;
}

void process(){
	for (int i=1;i<=n;i++){
		int resx=oo;
		int resy=oo;
		for (int j=0;j<=i;j++){
			int curx=max(0,px[j]+(r[j]<<1));
			int cury=max(0,py[j]);
			if (curx==0){
				curx-=r[i];
			}
			if (cury==0){
				cury-=r[i];
			}
			if (nocollision(curx,cury,i)){
				if ((curx<resx)||((curx==resx)&&(cury<resy))){
					resx=curx;
					resy=cury;
				}
			}
			curx=max(0,px[j]);
			cury=max(0,py[j]+(r[j]<<1));
			if (curx==0){
				curx-=r[i];
			}
			if (cury==0){
				cury-=r[i];
			}
			if (nocollision(curx,cury,i)){
				if ((curx<resx)||((curx==resx)&&(cury<resy))){
					resx=curx;
					resy=cury;
				}
			}
		}
		px[i]=resx;
		py[i]=resy;
	}
	for (int i=1;i<=n;i++){
		ansx[id[i]]=px[i]+r[i];
		ansy[id[i]]=py[i]+r[i];
	}
	for (int i=1;i<=n;i++){
		printf(" %d %d",ansx[i],ansy[i]);
	}
	puts("");
	return;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d:",i);
		process();
	}
	return 0;
}
