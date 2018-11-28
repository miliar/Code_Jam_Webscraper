#include<iostream>
#include<cstdio>
using namespace std;

int RowToWin(char a[4][4]);
int ColToWin(char a[4][4]);
int RDtoWin(char a[4][4]);
int LDtoWin(char a[4][4]);
int draw(char a[4][4]);

int main()
{
	int t, temp, temp_1, temp_2, temp_3, temp_4, i, j, start = 1;
	char arr[4][4];
	scanf("%d", &t);

	while(start <= t)
	{
		for(i = 0; i < 4; i++) {
			for(j = 0;j < 4; j++)
				cin >> arr[i][j];
		}

		temp = RowToWin(arr);
		temp_1 = ColToWin(arr);
		temp_2 = RDtoWin(arr);
		temp_3 = LDtoWin(arr);
		temp_4 = draw(arr);
		
		if(temp > 0) {
			if(temp == 1)
				cout << "Case #" << start << ": X won\n";
			else if(temp==2)
				cout << "Case #" << start << ": O won\n";
			else
				;
		}
		else if(temp_1 > 0)
		{
			if(temp_1 == 1)
				cout<<"Case #"<<start<<": X won\n";
			else if(temp_1==2)
				cout<<"Case #"<<start<<": O won\n";
			else
				;
		}
		else if(temp_2 > 0)
		{
			if(temp_2==1)
				cout<<"Case #"<<start<<": X won\n";
			else if(temp_2==2)
				cout<<"Case #"<<start<<": O won\n";
			else
				;
		}
		else if(temp_3 > 0)
		{
			if(temp_3==1)
				cout<<"Case #"<<start<<": X won\n";
			else if(temp_3==2)
				cout<<"Case #"<<start<<": O won\n";
		}
		else if(temp_4 == 1)
		{
			cout<<"Case #"<<start<<": Game has not completed\n";
		}
		else
		{
			cout<<"Case #"<<start<<": Draw\n";
		}
		start++;
	}

	return 0;
}


int RowToWin(char a[4][4])
{
	int i, j, c1, c2, f = 0;

	for(i = 0; i < 4; i++) {
		c1 = 0;
		c2 = 0;

		for(j = 0; j < 4; j++) {	
			if(a[i][j]=='X')
				c1++;
			else if(a[i][j]=='O')
				c2++;
			else if(a[i][j]=='T') {
				c1++;
				c2++;
			} else
				;
		}
		
		if(c1 == 4 || c2 == 4)
			break;
	}

	if(c1 == 4)
		f = 1;
	else if(c2 == 4)
		f = 2;
	else
		f = 0;
	return f;
}

int ColToWin(char a[4][4]) {
	int i, j, c1, c2, f = 0;
	for(i = 0; i < 4; i++)
	{
		c1 = 0;
		c2=0;
		
		for(j=0;j<4;j++) {	
			if(a[j][i]=='X')
				c1++;
			else if(a[j][i]=='O')
				c2++;
			else if(a[j][i]=='T'){
				c1++;
				c2++;
			} else
				;
		}

		if(c1 == 4 || c2 == 4)
			break;
	}

	if(c1==4)
		f = 1;
	else if(c2 == 4)
		f = 2;
	else
		f = 0;
	return f;
}

int RDtoWin (char a[4][4])
{
	int i, j, c1 = 0, c2 = 0, f = 0;
	for(i = 0; i < 4; i++) {
		if(a[i][i]=='X')
			c1++;
		else if(a[i][i]=='O')
			c2++;
		else if(a[i][i]=='T'){
			c1++;
			c2++;
		}
		else
			;
	}
	if(c1 == 4)
		f = 1;
	else if(c2 == 4)
		f = 2;
	else
		f = 0;
	return f;
}

int LDtoWin(char a[4][4])
{
	int i, j, temp = 3, c1 = 0, c2 = 0, f = 0;
	for(i = 0; i < 4; i++) {
		if(a[i][temp] =='X')
			c1++;
		else if(a[i][temp]=='O')
			c2++;
		else if(a[i][temp]=='T') {
			c1++;
			c2++;
		}
		temp--;
	}
	if(c1 == 4)
		f = 1;
	else if(c2 == 4)
		f = 2;
	else
		f = 0;
	return f;
}

int draw (char a[4][4])
{
	int i, j = 0, f = 0;
	for(i = 0; i < 4; i++){
		for(j = 0; j < 4; j++)
		{
			if(a[i][j] == '.')
			{
				f = 1;
				break;
			}
		}
		if(f == 1)
			break;
	}

	return f;
}

