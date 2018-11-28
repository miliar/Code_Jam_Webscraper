#include <iostream>
#include <cstdio>

using namespace std;

int t;

char b[10][10];

bool win(char c)
{
	//row
	for (int i = 0 ; i < 4 ; i ++)
	{
		bool flag = true;
		for (int j = 0 ; j < 4 ; j ++)
		{
			if (b[i][j] != c && b[i][j] != 'T'){
				flag = false;
				break;
			}
		}
		if (flag == true)
			return true;
	}
	//col
	for (int i = 0 ; i < 4 ; i ++)
	{
		bool flag = true;
		for (int j = 0 ; j < 4 ; j ++)
		{
			if (b[j][i] != c && b[j][i] != 'T'){
				flag = false;
				break;
			}
		}
		if (flag == true)
			return true;
	}
	bool flag = true;
	for (int i = 0 ; i < 4 ; i ++){
		if (b[i][i] != c && b[i][i] != 'T'){
			flag = false;
			break;
		}
	}
	if (flag == true)return true;
	flag = true;
	for (int i = 0 ; i < 4 ; i ++){
		if (b[i][3 - i] != c && b[i][3-i] != 'T'){
			flag = false;
			break;
		}
	}
	if (flag == true)return true;


	return false;
}

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	scanf("%d" , &t);
	int cas = 0;
	while (t --)
	{
		cas ++;
		for (int i = 0 ; i < 4 ; i ++)
		{
			scanf("%s" , b[i]);
		}
		bool isover = true;
		for (int i = 0 ; i< 4 ; i ++){
			for (int j = 0 ; j < 4 ; j ++){
				if (b[i][j] == '.')isover = false;
			}
		}

		printf("Case #%d: " , cas );
		if (win('X') && !win('O')){
			printf("X won");
		}
		else if (!win('X')&& win('O') ){
			printf("O won");
		}
		else if (!win('X') && !win('O') && isover){
			printf("Draw");
		}
		else if (!win('X') && !win('O')){
			printf("Game has not completed");
		}
		printf("\n");
		

	}
}