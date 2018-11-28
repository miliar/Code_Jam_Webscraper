#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int t;
char v[5][5];

int main(){
	int h,i,j,k;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		for(i=0;i<4;i++)
			scanf("%s",v[i]);
		bool x=0,o=0,c=1;
		for(i=0;i<4;i++){
			bool _x=1,_o=1;
			for(j=0;j<4;j++){
				if(v[i][j]!='X' && v[i][j]!='T')_x=0;
				if(v[i][j]!='O' && v[i][j]!='T')_o=0;
				if(v[i][j]=='.')c=0;
			}
			if(_x)x=1;
			if(_o)o=1;
		}
		for(i=0;i<4;i++){
			bool _x=1,_o=1;
			for(j=0;j<4;j++){
				if(v[j][i]!='X' && v[j][i]!='T')_x=0;
				if(v[j][i]!='O' && v[j][i]!='T')_o=0;
			}
			if(_x)x=1;
			if(_o)o=1;
		}
		bool _x=1,_o=1;
		for(i=0;i<4;i++){
			if(v[i][i]!='X' && v[i][i]!='T')_x=0;
			if(v[i][i]!='O' && v[i][i]!='T')_o=0;
		}
		if(_x)x=1;
		if(_o)o=1;
		_x=1,_o=1;
		for(i=0;i<4;i++){
			if(v[i][3-i]!='X' && v[i][3-i]!='T')_x=0;
			if(v[i][3-i]!='O' && v[i][3-i]!='T')_o=0;
		}
		if(_x)x=1;
		if(_o)o=1;
		printf("Case #%d: ",h);
		if(x)printf("X won\n");
		else if(o)printf("O won\n");
		else if(c)printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}
