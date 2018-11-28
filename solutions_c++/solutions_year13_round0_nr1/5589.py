#include <cstdio>
#include <iostream>

using namespace std;

#define sz 5
char g[sz][sz];

bool is_sol(int vi,int vj, char ch){
	int i,j,k,l;
	g[vi][vj] = ch;

	//row checking
	for(i = 0; i < 4; i++){
		for(j = 0; j < 4; j++){
			if(g[i][j] != ch)
				break;
		}
		if(j == 4)
			return true;
	}

	//column checking
	for(i = 0; i < 4; i++){
		for(j = 0; j < 4; j++){
			if(g[j][i] != ch)
				break;
		}
		if(j == 4)
			return true;
	}

	//diagonal
	for(j = 0; j < 4; j++){
		if(g[j][j] != ch)
			break;
	}
	if(j == 4)
		return true;
	for(i = 0, j = 3; i < 4; i++, j--){
		if(g[i][j] != ch)
			break;
	}
	if(i == 4)
		return true;


	return false;
}

int main(){
	int i,j,k,l,n,dot,I,J,cas=1;
	char ch[5];
	
	freopen("0.in", "r", stdin);
	freopen("out.txt","w",stdout);

	scanf("%ld",&n);
	while(n--){
		dot = 0;
		gets(ch);
		for(i = 0; i < 4; i++){
			gets(g[i]);
			for(j = 0; j < 4; j++){
				if(g[i][j] == '.')
					dot++;
				else if(g[i][j] == 'T'){
					I = i;
					J = j;
				}
			}
		}

		if(is_sol(I,J,'X'))
			printf("Case #%d: X won\n",cas++);
		else if(is_sol(I,J,'O'))
			printf("Case #%d: O won\n",cas++);
		else if(!dot)
			printf("Case #%d: Draw\n",cas++);
		else
			printf("Case #%d: Game has not completed\n",cas++);
	}

	return 0;
}