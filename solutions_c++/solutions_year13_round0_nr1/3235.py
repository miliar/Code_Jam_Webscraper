#include<iostream>
using namespace std;

int main()
{
	int t;
	char map[5][5];
	int i,j,x,o,ww;
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	scanf("%d",&t);
	bool draw;
	bool fin;
	for (ww=1;ww<=t;ww++)
	{
		fin=false;
		draw=true;
		for (i=0;i<4;i++) scanf("%s",map[i]);
		for (i=0;i<4;i++)
		{	
			x=0;o=0;
			for (j=0;j<4;j++)
				{
					if (map[i][j]=='X') x++;
					if (map[i][j]=='O') o++;
					if (map[i][j]=='T') {x++;o++;}
					if (map[i][j]=='.') {draw=false;break;}
				}
			if (x==4) {printf("Case #%d: X won\n",ww);fin=true;break;}
			if (o==4) {printf("Case #%d: O won\n",ww);fin=true;break;}
		}
		if (fin) continue;
		for (i=0;i<4;i++)
		{	
			x=0;o=0;
			for (j=0;j<4;j++)
				{
					if (map[j][i]=='X') x++;
					if (map[j][i]=='O') o++;
					if (map[j][i]=='T') {x++;o++;}
				}
			if (x==4) {printf("Case #%d: X won\n",ww);fin=true;break;}
			if (o==4) {printf("Case #%d: O won\n",ww);fin=true;break;}
		}
		if (fin) continue;
		x=0;o=0;
		for (i=0;i<4;i++)
		{
			if (map[i][i]=='X') x++;
			if (map[i][i]=='O') o++;
			if (map[i][i]=='T') {x++;o++;}
		}
		if (x==4) {printf("Case #%d: X won\n",ww);continue;}
		if (o==4) {printf("Case #%d: O won\n",ww);continue;}
		x=0;o=0;
		for (i=0;i<4;i++)
		{
			if (map[i][3-i]=='X') x++;
			if (map[i][3-i]=='O') o++;
			if (map[i][3-i]=='T') {x++;o++;}
		}
		if (x==4) {printf("Case #%d: X won\n",ww);continue;}
		if (o==4) {printf("Case #%d: O won\n",ww);continue;}
		
		if (draw) printf("Case #%d: Draw\n",ww);
			else printf("Case #%d: Game has not completed\n",ww);
	}
	return 0;
}
