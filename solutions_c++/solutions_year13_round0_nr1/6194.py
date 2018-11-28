#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

bool czyTeSame(char tab[4]){
	bool wyn=true;
	int pos=0;
	if (tab[0]=='T') pos++;
	if (tab[0]=='.') return false;
	for (int i=0; i<4; i++)
		if (tab[pos]!=tab[i] and tab[i]!='T'){
			wyn=false;
			break;
			}
	return wyn;
	}
	
int main(){
    int z;
    scanf(" %d",&z);
    for(int lol=1;lol<=z;lol++){
		char tab[4][4],rtab[4][4], zwy='.'; //TAB[wiersz][kolumna]
		bool kon=1;		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				scanf(" %c",&tab[i][j]);
				rtab[j][i]=tab[i][j];
				if (tab[i][j]=='.') kon=0;
				}
		for(int i=0;i<4;i++){
			if (czyTeSame(tab[i])){tab[i][0]=='T' ? zwy=tab[i][1]:zwy=tab[i][0]; break;}
			if (czyTeSame(rtab[i])){rtab[i][0]=='T' ? zwy=rtab[i][1]:zwy=rtab[i][0]; break;}
			}
		char dia1[4],dia2[4];
		for (int i=0;i<4;i++){
			dia1[i]=tab[i][i];
			dia2[i]=tab[i][(3-i)];
			}

		if (czyTeSame(dia1)){dia1[0]=='T' ? zwy=dia1[1]:zwy=dia1[0];}
		if (czyTeSame(dia2)){dia2[0]=='T' ? zwy=dia2[1]:zwy=dia2[0];}	
		printf("Case #%d: ", lol);
		if (zwy!='.') printf("%c won\n", zwy);
		else if (kon) printf("Draw\n");
		else printf("Game has not completed\n");
        }
    return 0;
    }

