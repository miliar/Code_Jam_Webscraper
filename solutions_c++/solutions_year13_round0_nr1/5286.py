#include <cstdio>

char plansze[10][10];
char map[260];
#define mapchar(tab, X) ((tab)[map[(X)]])
char pionowo[5][5];
char poziomo[5][5];
char prawodol[5];
char prawogora[5];
char ogolem[5];

void clear() {
	for(int i=0; i<4; ++i) {
		for(int j=0; j<4; ++j)
			pionowo[i][j]=poziomo[i][j]=0;
		prawodol[i]=prawogora[i]=ogolem[i]=0;
	}
}

int main() {
	//config
	map['.']=0;map['O']=1;map['X']=2;map['T']=3;
	int T,t=0;
	scanf("%d",&T);
	while(++t<=T) {
		gets(plansze[0]); //linebreak after number of tests and empty lines
		clear(); //count tables
		for(int i=0; i<4; ++i) {
			gets(plansze[i]);
			for(int j=0; j<4; ++j) {
				mapchar(poziomo[i], plansze[i][j])++ ;
				mapchar(pionowo[j], plansze[i][j])++ ;
				if(i==j)
					mapchar(prawodol, plansze[i][j])++ ;
				if(i==3-j)
					mapchar(prawogora, plansze[i][j])++ ;
				mapchar(ogolem, plansze[i][j])++ ;
			}
		}
		bool resolved=false;
		for(int i=0; i<4; ++i) {
			if(mapchar(poziomo[i], 'X')==4 ||
			  (mapchar(poziomo[i], 'X')==3 &&
			   mapchar(poziomo[i], 'T')==1) ||
			   mapchar(pionowo[i], 'X')==4 ||
			  (mapchar(pionowo[i], 'X')==3 &&
			   mapchar(pionowo[i], 'T')==1) ||
			   mapchar(prawogora , 'X')==4 ||
			  (mapchar(prawogora , 'X')==3 &&
			   mapchar(prawogora , 'T')==1) ||
			   mapchar(prawodol  , 'X')==4 ||
			  (mapchar(prawodol  , 'X')==3 &&
			   mapchar(prawodol  , 'T')==1)) {
				resolved=true;
				printf("Case #%d: X won\n",t);
				break;
			}
			if(mapchar(poziomo[i], 'O')==4 ||
			  (mapchar(poziomo[i], 'O')==3 &&
			   mapchar(poziomo[i], 'T')==1) ||
			   mapchar(pionowo[i], 'O')==4 ||
			  (mapchar(pionowo[i], 'O')==3 &&
			   mapchar(pionowo[i], 'T')==1) ||
			   mapchar(prawogora , 'O')==4 ||
			  (mapchar(prawogora , 'O')==3 &&
			   mapchar(prawogora , 'T')==1) ||
			   mapchar(prawodol  , 'O')==4 ||
			  (mapchar(prawodol  , 'O')==3 &&
			   mapchar(prawodol  , 'T')==1)) {
				resolved=true;
				printf("Case #%d: O won\n",t);
				break;
			}
		}
		if(!resolved) {
			if(mapchar(ogolem, '.')>0){
				resolved=true;
				printf("Case #%d: Game has not completed\n",t);
			}
		}
		if(!resolved) {
			resolved=true;
			printf("Case #%d: Draw\n",t);	
		}
	}
	return 0;
}

