#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
#include<vector>

using namespace std;

#define FOR(i,n,first) for(int i=first;i<n;i++)
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1
#define pb push_back
#define N 11000
#define M 101000
const int MOD=100000007;
const int INF = 0x3f3f3f3f;
typedef long long int Int64;
//#define SMALL

int main()
{
	#ifdef SMALL
    freopen("A-large.in","rt",stdin);
    freopen("text.out","w",stdout);
    #endif
    int cas;
    scanf("%d",&cas);
    char maps[10][10];
    for(int ii=1;ii<=cas;ii++){
    	bool flag=false;
    	for(int i=1;i<=4;i++){
    		scanf("%s",&maps[i]);
    		for(int j=0;j<4;j++)if(maps[i][j]=='.')flag=true;
    	}
    	bool flagx=false,flagy=false;
    	int x,o,t;
    	for(int i=1;i<=4;i++){
    		x=0,o=0,t=0;
    		for(int j=0;j<4;j++){
    			if(maps[i][j]=='X')x++;
    			if(maps[i][j]=='O')o++;
    			if(maps[i][j]=='T')t++;
    		}
    		if((x==3&&t==1)||(x==4))flagx=true;
    		if((o==3&&t==1)||(o==4))flagy=true;
    		
    	}
    	printf("Case #%d: ",ii);
		if(flagx||flagy){
    		if(flagx)puts("X won");
    		else if(flagy)puts("O won");
    		continue;
    	}
    	for(int i=0;i<4;i++){
    		x=0,o=0,t=0;
    		for(int j=1;j<=4;j++){
    			//printf("%d,%d,%c",j,i,maps[j][i]);
    			if(maps[j][i]=='X')x++;
    			if(maps[j][i]=='O')o++;
    			if(maps[j][i]=='T')t++;
    		}
    		if((x==3&&t==1)||(x==4))flagx=true;
    		if((o==3&&t==1)||(o==4))flagy=true;
    		
    	}

    	if(flagx||flagy){
    		if(flagx)puts("X won");
    		else if(flagy)puts("O won");
    		continue;
    	}
    	x=0,o=0,t=0;
    	for(int i=1;i<=4;i++){	
    		if(maps[i][i-1]=='X')x++;
    		if(maps[i][i-1]=='O')o++;
    		if(maps[i][i-1]=='T')t++;
    		
    	}
    	if((x==3&&t==1)||(x==4))flagx=true;
    	if((o==3&&t==1)||(o==4))flagy=true;
    	if(flagx||flagy){
    		if(flagx)puts("X won");
    		else if(flagy)puts("O won");
    		continue;
    	}
    	x=0,o=0,t=0;
    	for(int i=1;i<=4;i++){	
    		if(maps[i][4-i]=='X')x++;
    		if(maps[i][4-i]=='O')o++;
    		if(maps[i][4-i]=='T')t++;
    		
    	}
    	if((x==3&&t==1)||(x==4))flagx=true;
    	if((o==3&&t==1)||(o==4))flagy=true;
    	if(flagx||flagy){
    		if(flagx)puts("X won");
    		else if(flagy)puts("O won");
    	}else {
    			if(flag){
    				puts("Game has not completed");
    			}
    			else puts("Draw");
    		}
    	
    }
    return 0;
}