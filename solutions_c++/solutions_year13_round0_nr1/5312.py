#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <math.h>
#include <string>
using namespace std;
string m[4];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);
	int t,cas=0;
	scanf("%d",&t);
	while(t--){
		int win=0;
		for(int i=0;i<4;i++)cin>>m[i];
		for(int i=0;i<4;i++){
			int f=0;
			for(int k=0;k<4;k++){
				if(m[i][k]=='O'||m[i][k]=='T')f++;
			}
			if(f==4){
				win=1;break;
			}
			f=0;
			for(int k=0;k<4;k++){
				if(m[i][k]=='X'||m[i][k]=='T')f++;
			}
			if(f==4){win=-1;break;}
		}
		if(win!=0){
			if(win==1)printf("Case #%d: O won\n",++cas);
			else printf("Case #%d: X won\n",++cas);
			continue;
		}
			for(int i=0;i<4;i++){
			int f=0;
			for(int k=0;k<4;k++){
				if(m[k][i]=='O'||m[k][i]=='T')f++;
			}
			if(f==4){
				win=1;break;
			}
			f=0;
			for(int k=0;k<4;k++){
				if(m[k][i]=='X'||m[k][i]=='T')f++;
			}
			if(f==4){win=-1;break;}
		}
		if(win!=0){
		if(win==1)printf("Case #%d: O won\n",++cas);
			else printf("Case #%d: X won\n",++cas);
			continue;
		}
		int f=0;
		for(int i=0;i<4;i++){
			if(m[i][i]=='O'||m[i][i]=='T')f++;
		}
		if(f==4){
			printf("Case #%d: O won\n",++cas);
			continue;
		}
		f=0;
		for(int i=0;i<4;i++){
			if(m[i][i]=='X'||m[i][i]=='T')f++;
		}
		if(f==4){
			printf("Case #%d: X won\n",++cas);
			continue;
		}
		f=0;
		for(int i=0;i<4;i++){
			if(m[i][3-i]=='O'||m[i][3-i]=='T')f++;
		}
		if(f==4){
		printf("Case #%d: O won\n",++cas);
			continue;
		}
		f=0;
		for(int i=0;i<4;i++){
			if(m[i][3-i]=='X'||m[i][3-i]=='T')f++;
		}
		if(f==4){
			printf("Case #%d: X won\n",++cas);
			continue;
		}
		f=0;
		for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(m[i][j]=='.'){f=1;break;}
		if(f==1){
			printf("Case #%d: Game has not completed\n",++cas);
		}else{
			printf("Case #%d: Draw\n",++cas);
		}
	}	
	return 0;	
}