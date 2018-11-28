#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <iostream>
#include <list>
#include <deque>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int a[31][2];

void init(){
	memset(a,-1,sizeof(a));
	for(int i=0;i<11;++i){
		for(int j=0;j<11;++j){
			for(int k=0;k<11;++k){
				if(abs(i-j)<3&& abs(j-k)<3&&abs(i-k)<3){//aceitavel
					if(abs(i-j)<2&& abs(j-k)<2&&abs(i-k)<2){//normal
						a[i+j+k][0]=max( a[i+j+k][0] ,max(i,max(j,k)));
					}
					else{//surprise
						a[i+j+k][1]=max( a[i+j+k][1] ,max(i,max(j,k)));
					}
				}
			}
		}
	}
}
int main (){
	int  n, s, p, t, x, y, w;
	scanf("%d", &t);
	init();
	for(int cc=1;cc<=t;++cc){
		scanf("%d%d%d", &n, &s, &p);
		y=x=0;
		for(int i=0;i<n;++i){
			scanf("%d", &w);
			if(a[w][0]>=p)++x;
			else if(a[w][1]>=p)++y;
			
		}
		printf("Case #%d: %d\n", cc, x+min(s,y));
	}
	
	
	return 0;
}
