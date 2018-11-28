/*	Author       :	Muntasir Muzahid Chowdhury
	Problem Name :	
	Algorithm    :	
	Complexity   :	*/

//HEADERFILE
#include<iostream>
#include<stack>
#include<queue>
#include<list>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<ctime>
#include<cassert>
#include<string>
#include<algorithm>

using namespace std;

int main(){
		//freopen("A-large.in","r",stdin);
		//freopen("A-large.out","w",stdout);
	int cases,caseno=0,i,j,result;
	int R,C;
	char grid[51][51];
	scanf("%d",&cases);
	while(cases--){
		scanf("%d %d",&R,&C);
		for(i=0;i<51;i++) for(j=0;j<51;j++) grid[51][51]='.';
		getchar();
		for(i=0;i<R;i++) gets(grid[i]);			
		int cnt;
		for(cnt=0,i=0;i<R;i++) for(j=0;j<C;j++) if(grid[i][j]=='#') ++cnt;
		
		if(cnt%4!=0) printf("Case #%d:\nImpossible\n",++caseno);
		else{
			int imp=0;
			for(i=0;i<R;i++){
				for(j=0;j<C;j++){
					if(grid[i][j]!='#') continue;
					grid[i][j]='1';
					if(j+1>C-1 || grid[i][j+1]!='#') {imp=1;break;}
					grid[i][j+1]='2';
					if(i+1>R-1 || grid[i+1][j]!='#') {imp=1;break;}
					grid[i+1][j]='3';
					if(i+1>R-1 || j+1>C-1 || grid[i+1][j+1]!='#') {imp=1;break;}
					grid[i+1][j+1]='4';
				}
				if(imp==1) break;
			}
			if(imp==1) printf("Case #%d:\nImpossible\n",++caseno);
			else{
				for(i=0;i<R;i++){
					for(j=0;j<C;j++){
						if(grid[i][j]=='1') 
							grid[i][j]='/';
						else if(grid[i][j]=='2') 
							grid[i][j]='\\';
						else if(grid[i][j]=='3') 
								grid[i][j]='\\';
						else if(grid[i][j]=='4') 
						        grid[i][j]='/';
					}
				}
				printf("Case #%d:\n",++caseno);
				for(i=0;i<R;i++){
					//printf("%s\n",grid[i]);
					for(j=0;j<C;j++) printf("%c",grid[i][j]);
					printf("\n");
				}
			}
		}
	}
	return 0;
}

