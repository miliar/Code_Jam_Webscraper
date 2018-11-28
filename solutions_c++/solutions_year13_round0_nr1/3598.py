#include <stdio.h>
#include <assert.h>

using namespace std;

int n;

char mas[5][5];

int oxt[4];

int g(char c){
	if (c == 'O')
		return 0;
	if (c == 'X')
		return 1;
	if (c == 'T')
		return 2;
	if (c == '.')
		return 3;
	assert(false);
}


bool cexit(int it){
	if (oxt[0] == 4 || (oxt[0] == 3 && oxt[2] == 1)){
		printf("Case #%d: O won\n", it);
		return true;
	}
	if (oxt[1] == 4 || (oxt[1] == 3 && oxt[2] == 1)){
		printf("Case #%d: X won\n", it);
		return true;
	}
	return false;
}

void cal(int it){
	for (int i = 0; i < 4; i++){
		oxt[0] = 0; oxt[1] = 0; oxt[2] = 0;
		for (int j = 0; j < 4; j++)
			oxt[g(mas[i][j])]++;
		if (cexit(it))
			return;
	}

	for (int i = 0; i < 4; i++){
		oxt[0] = 0; oxt[1] = 0; oxt[2] = 0;
		for (int j = 0; j < 4; j++)
			oxt[g(mas[j][i])]++;
		if (cexit(it))
			return;
	}

	oxt[0] = 0; oxt[1] = 0; oxt[2] = 0;
	for (int i = 0; i < 4; i++)
		oxt[g(mas[i][i])]++;
	if (cexit(it))
		return;
	oxt[0] = 0; oxt[1] = 0; oxt[2] = 0;
	for (int i = 0; i < 4; i++)
		oxt[g(mas[4 - i - 1][i])]++;
	if (cexit(it))
		return;
	if (!oxt[3])
		printf("Case #%d: Draw\n", it);
	else
		printf("Case #%d: Game has not completed\n", it);
	return;
}

int main(){
	freopen("input.txt", "r", stdin);

	scanf("%d\n", &n);
	for (int i = 0; i < n; i++){
		oxt[0] = 0; oxt[1] = 0; oxt[2] = 0; oxt[3] = 0;
		for (int j = 0; j < 4; j++)
			gets(mas[j]);
		cal(i + 1);
		scanf("\n");
	}
	return 0;

}