#include<stdio.h>
#include<iostream>
using namespace std;
// Won X, Won Y, Draw(Game Over), Left
int main()
{
	char c;
	int a,i,j,k,store,X,O;
	char b[4][4],ch;
	scanf("%d",&a);
	for(k=1; k<=a; k++)
	{
		store = 0;
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				scanf("%c",&ch);
				if(ch!='\n')
				b[i][j] = ch;
				else
					j--;
				if(b[i][j]=='.')
					store = 5;
			}
		}
		
		if((b[0][0]=='X')||(b[0][0]=='T'))
			if((b[0][1]=='X')||(b[0][1]=='T'))
				if((b[0][2]=='X')||(b[0][2]=='T'))
					if((b[0][3]=='X')||(b[0][3]=='T'))
						{printf("Case #%d: X won\n",k);continue;}
		if((b[1][0]=='X')||(b[1][0]=='T'))
			if((b[1][1]=='X')||(b[1][1]=='T'))
				if((b[1][2]=='X')||(b[1][2]=='T'))
					if((b[1][3]=='X')||(b[1][3]=='T'))
						{printf("Case #%d: X won\n",k);continue;}
		if((b[2][0]=='X')||(b[2][0]=='T'))
			if((b[2][1]=='X')||(b[2][1]=='T'))
				if((b[2][2]=='X')||(b[2][2]=='T'))
					if((b[2][3]=='X')||(b[2][3]=='T'))
						{printf("Case #%d: X won\n",k);continue;}
		if((b[3][0]=='X')||(b[3][0]=='T'))
			if((b[3][1]=='X')||(b[3][1]=='T'))
				if((b[3][2]=='X')||(b[3][2]=='T'))
					if((b[3][3]=='X')||(b[3][3]=='T'))
						{printf("Case #%d: X won\n",k);continue;}
		//////////Column
		if((b[0][0]=='X')||(b[0][0]=='T'))
			if((b[1][0]=='X')||(b[1][0]=='T'))
				if((b[2][0]=='X')||(b[2][0]=='T'))
					if((b[3][0]=='X')||(b[3][0]=='T'))
						{printf("Case #%d: X won\n",k);continue;}
		if((b[0][1]=='X')||(b[0][1]=='T'))
			if((b[1][1]=='X')||(b[1][1]=='T'))
				if((b[2][1]=='X')||(b[2][1]=='T'))
					if((b[3][1]=='X')||(b[3][1]=='T'))
						{printf("Case #%d: X won\n",k);continue;}
		if((b[0][2]=='X')||(b[0][2]=='T'))
			if((b[1][2]=='X')||(b[1][2]=='T'))
				if((b[2][2]=='X')||(b[2][2]=='T'))
					if((b[3][2]=='X')||(b[3][2]=='T'))
						{printf("Case #%d: X won\n",k);continue;}
		if((b[0][3]=='X')||(b[0][3]=='T'))
			if((b[1][3]=='X')||(b[1][3]=='T'))
				if((b[2][3]=='X')||(b[2][3]=='T'))
					if((b[3][3]=='X')||(b[3][3]=='T'))
						{printf("Case #%d: X won\n",k);continue;}


		if((b[0][0]=='X')||(b[0][0]=='T'))
			if((b[1][1]=='X')||(b[1][1]=='T'))
				if((b[2][2]=='X')||(b[2][2]=='T'))
					if((b[3][3]=='X')||(b[3][3]=='T'))
						{printf("Case #%d: X won\n",k);continue;}
		if((b[3][0]=='X')||(b[3][0]=='T'))
			if((b[2][1]=='X')||(b[2][1]=='T'))
				if((b[1][2]=='X')||(b[1][2]=='T'))
					if((b[0][3]=='X')||(b[0][3]=='T'))
						{printf("Case #%d: X won\n",k);continue;}




		if((b[0][0]=='O')||(b[0][0]=='T'))
			if((b[0][1]=='O')||(b[0][1]=='T'))
				if((b[0][2]=='O')||(b[0][2]=='T'))
					if((b[0][3]=='O')||(b[0][3]=='T'))
						{printf("Case #%d: O won\n",k);continue;}
		if((b[1][0]=='O')||(b[1][0]=='T'))
			if((b[1][1]=='O')||(b[1][1]=='T'))
				if((b[1][2]=='O')||(b[1][2]=='T'))
					if((b[1][3]=='O')||(b[1][3]=='T'))
						{printf("Case #%d: O won\n",k);continue;}
		if((b[2][0]=='O')||(b[2][0]=='T'))
			if((b[2][1]=='O')||(b[2][1]=='T'))
				if((b[2][2]=='O')||(b[2][2]=='T'))
					if((b[2][3]=='O')||(b[2][3]=='T'))
						{printf("Case #%d: O won\n",k);continue;}
		if((b[3][0]=='O')||(b[3][0]=='T'))
			if((b[3][1]=='O')||(b[3][1]=='T'))
				if((b[3][2]=='O')||(b[3][2]=='T'))
					if((b[3][3]=='O')||(b[3][3]=='T'))
						{printf("Case #%d: O won\n",k);continue;}

		//////////Column
		if((b[0][0]=='O')||(b[0][0]=='T'))
			if((b[1][0]=='O')||(b[1][0]=='T'))
				if((b[2][0]=='O')||(b[2][0]=='T'))
					if((b[3][0]=='O')||(b[3][0]=='T'))
						{printf("Case #%d: O won\n",k);continue;}
		if((b[0][1]=='O')||(b[0][1]=='T'))
			if((b[1][1]=='O')||(b[1][1]=='T'))
				if((b[2][1]=='O')||(b[2][1]=='T'))
					if((b[3][1]=='O')||(b[3][1]=='T'))
						{printf("Case #%d: O won\n",k);continue;}
		if((b[0][2]=='O')||(b[0][2]=='T'))
			if((b[1][2]=='O')||(b[1][2]=='T'))
				if((b[2][2]=='O')||(b[2][2]=='T'))
					if((b[3][2]=='O')||(b[3][2]=='T'))
						{printf("Case #%d: O won\n",k);continue;}
		if((b[0][3]=='O')||(b[0][3]=='T'))
			if((b[1][3]=='O')||(b[1][3]=='T'))
				if((b[2][3]=='O')||(b[2][3]=='T'))
					if((b[3][3]=='O')||(b[3][3]=='T'))
						{printf("Case #%d: O won\n",k);continue;}

					

		if((b[0][0]=='O')||(b[0][0]=='T'))
			if((b[1][1]=='O')||(b[1][1]=='T'))
				if((b[2][2]=='O')||(b[2][2]=='T'))
					if((b[3][3]=='O')||(b[3][3]=='T'))
						{printf("Case #%d: O won\n",k);continue;}
		if((b[3][0]=='O')||(b[3][0]=='T'))
			if((b[2][1]=='O')||(b[2][1]=='T'))
				if((b[1][2]=='O')||(b[1][2]=='T'))
					if((b[0][3]=='O')||(b[0][3]=='T'))
						{printf("Case #%d: O won\n",k);continue;}


		if(store == 5)
			{printf("Case #%d: Game has not completed\n",k);continue;}
		else
			{printf("Case #%d: Draw\n",k);continue;}
			/*
			Case #1: X won
			Case #2: Draw
			Case #3: Game has not completed
			*/
	}
}