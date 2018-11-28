#include <stdio.h>
#include <string.h>

int main()
{
	char table[5][5];
	char result[100];
	bool owin,xwin,finish,draw;

	int T,x,o,t,dot;

	scanf("%d",&T);

	for (int i=1;i<=T;i++)
	{
		x=0;
		o=0;
		t=0;
		dot=0;
		owin=false;
		xwin=false;
		finish=false;

		for (int j=0;j<4;j++)
		{
			scanf("%s",table[j]);
			for (int k=0;k<4;k++)
			{
				switch(table[j][k])
				{
				case 'X': x++; break;
				case 'O': o++; break;
				case '.': dot++; break;
				}
			}
		}

		if (x<3 && o<3) {strcpy(result,"Game has not completed"); finish=true;}
		else
		{   //check row
			if (finish==false)
			{
			for (int j=0;j<4;j++)
				{
					xwin=owin=true;
					t=0;
					for (int k=0;k<4;k++)
					{
						if (table[j][k]=='T') t++;
						else
							if (table[j][k]=='X') owin=false;
							else
								if (table[j][k]=='O') xwin=false;
								else
									if (table[j][k]=='.') {xwin=false; owin=false;}

						if (owin==false && xwin==false) break;
						else
							if (t>1) break;
					}

					if (xwin==true && owin==false && t<=1) {strcpy(result,"X won"); finish=true;}
					else if (xwin==false && owin==true && t<=1) {strcpy(result,"O won"); finish=true;}
				}
			}
			//check column
			if (finish==false)
			{
				for (int k=0;k<4;k++)
				{
					xwin=owin=true;
					t=0;
					for (int j=0;j<4;j++)
					{
						if (table[j][k]=='T') t++;
						else
							if (table[j][k]=='X') owin=false;
							else
								if (table[j][k]=='O') xwin=false;
								else
									if (table[j][k]=='.') {xwin=false; owin=false;}

						if (owin==false && xwin==false) break;
						else
							if (t>1) break;
					}

					if (xwin==true && owin==false && t<=1) {finish=true; strcpy(result,"X won");}
					else if (xwin==false && owin==true && t<=1) {finish=true; strcpy(result,"O won");}
				}
			}
			//diagonal 1
			if (finish==false)
			{
				x=o=t=0;
				for (int j=0;j<4;j++)
				{
					if (table[j][j]=='O') o++;
					else
						if (table[j][j]=='X') x++;
						else
							if (table[j][j]=='T') t++;
							else
								if (table[j][j]=='.') break;
				}
				if (t==0 && x+o==4)
				{
					if (x==4) {strcpy(result,"X won"); finish=true;}
					else if (o==4) {strcpy(result,"O won"); finish=true;}
				}
				else if (t==1 && x+o==3)
				{
					if (x==3) {strcpy(result,"X won"); finish=true;}
					else if (o==3) {strcpy(result,"O won"); finish=true;}
				}
			}
			//diagonal 2
			if (finish==false)
			{
				x=o=t=0;
				for (int j=0;j<4;j++)
				{
					if (table[j][3-j]=='O') o++;
					else
						if (table[j][3-j]=='X') x++;
						else
							if (table[j][3-j]=='T') t++;
							else
								if (table[j][3-j]=='.') break;
				}
				if (t==0 && o+x==4)
				{
					if (x==4) {strcpy(result,"X won"); finish=true;}
					else if (o==4) {strcpy(result,"O won"); finish=true;}
				}
				else if (t==1 && o+x==3)
				{
					if (x==3) {strcpy(result,"X won"); finish=true;}
					else if (o==3) {strcpy(result,"O won"); finish=true;}
				}
			}

			if (finish==false && dot==0)
			{
				finish=true;
				strcpy(result,"Draw");
			}
			else
				if (finish==false && dot>0)
				{
					strcpy(result,"Game has not completed");
					finish=true;
				}
			
		}

		printf("Case #%d: %s\n",i,result);
	}



	return 0;
}