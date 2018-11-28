#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;

char Map[60][60];
int main(){
	freopen("D://A-large.in","r",stdin);
    freopen("D://A-large.out","w",stdout);
	int t ; 
	scanf("%d",&t);
	for(int cases = 1 ; cases<=t;++cases){
		int R , C ; 
		scanf("%d%d",&R,&C);
		for(int i = 0 ; i<R ;++i)
			for(int j = 0 ; j<C ;++j)
				scanf(" %c",&Map[i][j]);
		bool fl = 0 ; 
		for(int i = 0 ; i<R && fl== 0; ++i)
			for(int j = 0 ; j<C&&fl==0 ;++j){
				if( Map[i][j] =='#'){
					if(	(j+1 < C && Map[i][j+1] == '#') && (i+1<R && Map[i+1][j] =='#') && ( (i+1<R)&&Map[i+1][j+1]=='#')){
						Map[i][j] ='/'; Map[i][j+1]='\\' ;
						Map[i+1][j]='\\',Map[i+1][j+1]='/';
					}
					else fl = 1 ;
				}
			}
		printf("Case #%d:\n",cases);
		if( fl == 1 )puts("Impossible");
		else{
			for(int i = 0 ; i<R;++i){
				for(int j = 0 ; j<C;++j)
					printf("%c",Map[i][j]);
				printf("\n");
			}
		}
	}
	return 0;
}