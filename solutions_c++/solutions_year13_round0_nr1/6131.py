#include<cstdio>
#include<cstdlib>
using namespace std;

char tab[4][6];
int pelne[4];

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		for(int i=0; i<4; i++)
			scanf("%s", tab[i]);
		bool skonczone = false;
		char znak;
		for(int i=0; i<4; i++){
			for(int j=1; j<4; j++){
				if(tab[j][i] == '.')
					break;
				if(tab[j][i] != tab[j-1][i])
					if(tab[j][i] != 'T' && tab[j-1][i] != 'T') 	
						break;
				if(j>=2)
					if(tab[j][i] != tab[j-2][i])
						break;
				if(j == 3 && tab[j][i] != '.'){
					skonczone = true;
					znak = tab[j][i];
					if(znak == 'T')
						znak = tab[j-1][i];
					printf("Case #%d: %c won\n",t,znak);
					break;
				}  				
			}
			if(skonczone)
				break;
		}
		if(skonczone)
			continue;
		for(int i=0; i<4; i++){
			for(int j=1; j<4; j++){
				if(tab[i][j] == '.')
					break;
				if(tab[i][j] != tab[i][j-1])
					if(tab[i][j] != 'T' && tab[i][j-1] != 'T')
						break;
				if(j>=2)
					if(tab[i][j] != tab[i][j-2])
						break;
				if(j == 3 && tab[i][j] != '.'){
					skonczone = true;
					znak = tab[i][j];
					if(znak == 'T')
						znak = tab[i][j-1];
					printf("Case #%d: %c won\n",t,znak);	
					break;
				}						
			}
			if(skonczone)
				break;
		}
		if(skonczone)
			continue;
		for(int i=1, j=1; i<4; i++, j++){
			if(tab[i][j] == '.')
					break;
			if(tab[i][j] != tab[i-1][j-1])
				if(tab[i][j] != 'T' && tab[i-1][j-1] != 'T')
					break;
			if(i>=2)	
				if(tab[i][j] != tab[i-2][j-2])
					break;
			if(i == 3 && tab[i][j] != '.'){
				skonczone = true;
				znak = tab[i][j];
				if(znak == 'T')
					znak = tab[i-1][j-1];
				printf("Case #%d: %c won\n",t,znak);
			}	
		}
		if(skonczone)
			continue;
		for(int i=2, j=1; i>=0; i--, j++){
			if(tab[i][j] == '.')
					break;
			if(tab[i][j] != tab[i+1][j-1])
				if(tab[i][j] != 'T' && tab[i+1][j-1] != 'T')
					break;
			if(j>=2)
				if(tab[i][j] != tab[i+2][j-2])
					break;
			if(i == 0 && tab[i][j] != '.'){
				skonczone = true;
				znak = tab[i][j];
				if(znak == 'T')
					znak = tab[i+1][j-1];
				printf("Case #%d: %c won\n",t,znak);
			}
		}
		if(skonczone)
			continue;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(tab[i][j] == 'T' || tab[i][j] == 'O' || tab[i][j] == 'X')
					pelne[i]++;
		for(int i=0; i<4; i++){			
			if(pelne[i] < 4){
				printf("Case #%d: Game has not completed\n", t);
				skonczone = true;
				break;
			}	
		}	
		for(int i=0; i<4; i++)
			pelne[i] = 0;
		if(skonczone)
			continue;
		printf("Case #%d: Draw\n", t);
	}
}
