#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
int T,n,f=0;
char maze[110][110];
double total[110],win[110],lose[110];
double WP[110],OWP[110],OOWP[110];	
int main(){
    scanf("%d",&T);
    while(T--){
	scanf("%d",&n);
	for(int i=0;i<n;i++){
	    scanf("%s",maze[i]);
	    total[i] = win[i] = lose[i] = 0;
	}
	for(int i=0;i<n;i++){
	    for(int j=0;j<n;j++){
		if(maze[i][j]!='.') total[i]+=1;
		if(maze[i][j]=='1') win[i]+=1;
		if(maze[i][j]=='0') lose[i]+=1;
	    }
	}
	printf("Case #%d:\n",++f);
	for(int i=0;i<n;i++){
	    WP[i] = win[i]/total[i];
	}
	for(int i=0;i<n;i++){
	    OWP[i] = 0;
	    for(int j=0;j<n;j++){
		if(maze[i][j]!='.'){
		    double up = win[j],down = total[j]-1;
		    if(maze[i][j]=='0') up=up-1;
		    OWP[i]+=(up/down);
		}
	    }
	    OWP[i] /= total[i];
	}
	for(int i=0;i<n;i++){
	    OOWP[i] = 0;
	    for(int j=0;j<n;j++){
		if(maze[i][j]!='.'){
		    OOWP[i]+=OWP[j];
		}
	    }
	    OOWP[i]/=total[i];
	}
	for(int i=0;i<n;i++){
	    printf("%.10lf\n",0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
	}
    }
}
