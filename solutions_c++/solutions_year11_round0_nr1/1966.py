#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
char r[110][2];
char p[110];
int fab(int a){
	if(a > 0)
		return a;
	else
		return -a;
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j;
	int T,N;
	int st;
	int ct,tt;
	int ox,bx;
	int cas = 1;
	scanf("%d",&T);
	while(T --){
		scanf("%d",&N);
		st = 0;
		for(i = 0; i < N;i ++){
			scanf("%s%d",r[i],&p[i]);
		}
		ct = 0;
		ox = bx = 1;
		for(i = 0; i < N ;i ++){
			if(r[i][0] == 'B'){
				tt = fab(p[i] - bx);
				if(tt <= ct){
					ct = 1;
					st+=1;
				}else{
					st+=tt-ct+1;
					ct = tt-ct+1;
				}
				bx = p[i];
				while(r[i+1][0] == 'B' && i + 1< N){
					i++;
					tt =fab(p[i]-bx)+1;
					ct += tt;
					st +=tt;
					bx = p[i];
				}
			}else{
				tt = fab(p[i] - ox);
				if(tt <= ct){
					ct = 1;
					st += 1;
				}else{
					st += tt-ct +1;
					ct = tt -ct + 1;
				}
				ox = p[i];
				while(r[i+1][0] == 'O' && i+ 1 < N){
					i++;
					tt = fab(p[i]-ox)+1;
					ct += tt;
					st += tt;
					ox = p[i];
				}
			}
		}
		printf("Case #%d: %d\n",cas++,st);
	}
	return 0;
}
