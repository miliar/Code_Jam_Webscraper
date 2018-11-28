#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <string>
using namespace std;
int n,m;
#define MAXN 1010
char Map[MAXN][MAXN];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("Ago.out","w",stdout);
	int ca,cs=1;
	scanf("%d",&ca);
	while(ca--){
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
		{
			scanf("%s",Map[i]);	
		}	
		
		for(int i=0;i<n-1;i++)
		{
			for(int j=0;j<m-1;j++)
			{
				if(Map[i][j]=='#'){
					if(Map[i+1][j] == '#' && Map[i+1][j+1] == '#' && Map[i][j+1]=='#'){
						Map[i][j] = '/';
						Map[i+1][j] = '\\';
						Map[i][j+1] = '\\';
						Map[i+1][j+1] = '/';
					}			
					
				}	
			}	
			
		}
		bool T= true;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				if(Map[i][j]=='#') T=false;
				
		printf("Case #%d:\n",cs++);
		if(!T) printf("Impossible\n");
		else{
			for(int i=0;i<n;i++)
				printf("%s\n",Map[i]);	
			
		}
	}	
	
	return 0;	
}
