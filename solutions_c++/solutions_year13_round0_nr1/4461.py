#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<map>
#include<string>
#include<iostream>
#include<stack>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

#define EPS (1e-7)
#define PI (acos(-1.0))
#define MAXI(a,b) ((a)>(b)?(a):(b))
#define MINI(a,b) ((a)<(b)?(a):(b))
#define mxx 1005
#define SZOF sizeof
#define SZ size
typedef long long INT;


int main(){
	int i,j,tst,cas=1,n,flag;

	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tst);
	char z[6][6];

	while(tst--){
		for(i=0;i<4;i++){
			scanf("%s",z[i]);
		}
		flag=0;
		//hor
		int x=0,o=0,t=0;
		for(i=0;i<4;i++){
			x=0,o=0,t=0;
			for(j=0;j<4;j++){
				if(z[i][j]=='X'){x++;}
				else if(z[i][j]=='O'){o++;}
				else if(z[i][j]=='T'){t++;}
			}
			if(x+t==4){flag=1;break;}
			else if(o+t==4){flag=2;break;}
		}
		if(flag==1){
			printf("Case #%d: X won\n",cas++);continue;
		}
		else if(flag==2){
			printf("Case #%d: O won\n",cas++);continue;
		}
		for(j=0;j<4;j++){
			x=0,o=0,t=0;
			for(i=0;i<4;i++){
				if(z[i][j]=='X'){x++;}
				else if(z[i][j]=='O'){o++;}
				else if(z[i][j]=='T'){t++;}
			}
			if(x+t==4){flag=1;break;}
			else if(o+t==4){flag=2;break;}
		}
		if(flag==1){
			printf("Case #%d: X won\n",cas++);continue;
		}
		else if(flag==2){
			printf("Case #%d: O won\n",cas++);continue;
		}
		x=0,o=0,t=0;
		for(i=0;i<4;i++){	
			if(z[i][i]=='X'){x++;}
			else if(z[i][i]=='O'){o++;}
			else if(z[i][i]=='T'){t++;}
		}	
		if(x+t==4){flag=1;}
		else if(o+t==4){flag=2;}
		if(flag==1){
			printf("Case #%d: X won\n",cas++);continue;
		}
		else if(flag==2){
			printf("Case #%d: O won\n",cas++);continue;
		}
		x=0,o=0,t=0;
		for(i=0;i<4;i++){	
			if(z[3-i][i]=='X'){x++;}
			else if(z[3-i][i]=='O'){o++;}
			else if(z[3-i][i]=='T'){t++;}
		}	
		if(x+t==4){flag=1;}
		else if(o+t==4){flag=2;}
		if(flag==1){
			printf("Case #%d: X won\n",cas++);continue;
		}
		else if(flag==2){
			printf("Case #%d: O won\n",cas++);continue;
		}
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(z[i][j]=='.'){flag=-1;}
			}
		}
		if(flag==-1){printf("Case #%d: Game has not completed\n",cas++);}
		else{printf("Case #%d: Draw\n",cas++);}
	}
	

	//system("pause");
	return 0;
}

