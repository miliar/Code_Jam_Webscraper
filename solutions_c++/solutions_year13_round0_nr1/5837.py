#include<stdio.h>

int main(){
	
	char tab[4][4];
	int t, i, j, k;
	int xh, xv, oh, ov, xdp, odp, xds, ods;
	int winX, winO, emp;
	scanf("%d", &t);
	
	for(k=1;k<=t;k++){
		for(i=0;i<4;i++){
			scanf("%s", tab[i]);
			//printf("%s\n", tab[i]);
		}
		
		emp=0;
		winX=winO=0;
		xdp=odp=xds=ods=0;
		for(i=0;i<4;i++){
			xh=xv=oh=ov=0;
			if(tab[i][i]=='X')xdp++;
			else if(tab[i][i]=='O')odp++;
			else if(tab[i][i]=='T'){xdp++;odp++;}
			if(tab[3-i][i]=='X')xds++;
			else if(tab[3-i][i]=='O')ods++;
			else if(tab[3-i][i]=='T'){xds++;ods++;}
			
			for(j=0;j<4;j++){
				if(tab[i][j]=='.')emp=1;
				else if(tab[i][j]=='X')xh++;
				else if(tab[i][j]=='O')oh++;
				else{xh++;oh++;}
				
				if(tab[j][i]=='.')emp=1;
				else if(tab[j][i]=='X')xv++;
				else if(tab[j][i]=='O')ov++;
				else{xv++;ov++;}
			}
			
			if(xh==4||xv==4){
				winX=1;
				break;
			}
			else if(oh==4||ov==4){
				winO=1;
				break;
			}
		}
		
		if(xds==4||xdp==4)winX=1;
		else if(odp==4||ods==4)winO=1;
		
		printf("Case #%d: ", k);
		if(winX)printf("X won\n");
		else if(winO)printf("O won\n");
		else if(emp)printf("Game has not completed\n");
		else printf("Draw\n");
		
	}

	return 0;
}