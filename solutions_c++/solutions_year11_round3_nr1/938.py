#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
int T,f=0;
int m,n;
char maze[110][110];
bool chk(){
    for(int i=0;i<m;i++){
	for(int j=0;j<n;j++){
	    if(maze[i][j]=='#'){
		return 0;
	    }	    
	}
    }
    for(int i=0;i<m;i++)
	puts(maze[i]);
}
int main(){
    scanf("%d",&T);
    while(T--){
	scanf("%d%d",&m,&n);
	for(int i=0;i<m;i++){
	    scanf("%s",maze[i]);
	}
	for(int i=0;i<m-1;i++){
	    for(int j=0;j<n-1;j++){
		if(maze[i][j]=='#' && maze[i][j+1]=='#' && maze[i+1][j]=='#' && maze[i+1][j+1]=='#'){
		    maze[i][j]='/';
		    maze[i][j+1] = '\\';
		    maze[i+1][j] = '\\';
		    maze[i+1][j+1]='/';
		}
	    }
	}

	printf("Case #%d:\n",++f);
	if(chk()==0) puts("Impossible");
    }



}
