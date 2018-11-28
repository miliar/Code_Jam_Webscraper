#include<cstdio>

int main(){
	int t;
	char tab[4][4];
	scanf("%d", &t);
	for(int caso=1;caso<=t;caso++){
		bool dot=0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				scanf(" %c",&tab[i][j]);
				if(tab[i][j]=='.')
					dot=1;
			}
		int won=0;
		bool xd=1, od=1, xs=1, os=1;
		for(int i=0;i<4;i++){
			bool x=1,o=1, xc=1, oc=1;
			for(int j=0;j<4;j++){
				if(tab[i][j]=='.' || tab[i][j] == 'O')
					x=0;
				if(tab[i][j]=='.' || tab[i][j] == 'X')
					o=0;
				if(tab[j][i]=='.' || tab[j][i] == 'O')
					xc=0;
				if(tab[j][i]=='.' || tab[j][i] == 'X')
					oc=0;
			}
			if(x || xc) won=1;
			if(o || oc) won=2;
			if(tab[i][i]=='.' || tab[i][i] == 'O')
				xd=0;
			if(tab[i][i]=='.' || tab[i][i] == 'X')
				od=0;
			if(tab[i][3-i]=='.' || tab[i][3-i] == 'O')
				xs=0;
			if(tab[i][3-i]=='.' || tab[i][3-i] == 'X')
				os=0;
		}
		if(xd || xs) won=1;
		if(od || os) won=2;
		if(won==0){
			if(dot)
				printf("Case #%d: Game has not completed\n", caso);
			else printf("Case #%d: Draw\n", caso);
		}
		else if(won==1)
		printf("Case #%d: X won\n", caso);
		else printf("Case #%d: O won\n", caso);
	}
	return 0;
}
