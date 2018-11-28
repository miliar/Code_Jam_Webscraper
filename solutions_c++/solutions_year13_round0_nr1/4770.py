#include <iostream>
#include <algorithm>

using namespace std;

int xwon,owon,unfinish;

void test(char a,char b,char c,char d){
	int xct=0,oct=0,tct=0;
	char ss[4];
	ss[0]=a;ss[1]=b;ss[2]=c;ss[3]=d;
	for(int i=0;i<4;i++)
		if(ss[i]=='O')
			oct++;
		else if(ss[i]=='X')
			xct++;
		else if(ss[i]=='T')
			tct++;

	if(tct<=1)
		if(xct+tct>3)
			xwon=1;
		else if(oct+tct>3)
			owon=1;
}

	char s[4][20];
int main(){
	long cc,tt;
	long n,i,j;
	int map[4][4];
	int ans,ans2;
	scanf("%d",&tt);

	for(cc=0;cc<tt;cc++){
		for(int i=0;i<4;i++)
			scanf("%s",s[i]);

		xwon=owon=unfinish=0;

		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(s[i][j]=='.')
					unfinish=1;

		
		test(s[0][0],s[0][1],s[0][2],s[0][3]);
		test(s[1][0],s[1][1],s[1][2],s[1][3]);
		test(s[2][0],s[2][1],s[2][2],s[2][3]);
		test(s[3][0],s[3][1],s[3][2],s[3][3]);
		
		test(s[1][0],s[2][0],s[3][0],s[0][0]);
		test(s[1][1],s[2][1],s[3][1],s[0][1]);
		test(s[1][2],s[2][2],s[3][2],s[0][2]);
		test(s[1][3],s[2][3],s[3][3],s[0][3]);
		
		test(s[0][0],s[1][1],s[2][2],s[3][3]);
		test(s[0][3],s[1][2],s[2][1],s[3][0]);

		if(xwon)
			printf("Case #%d: X won\n",cc+1);
		else if(owon)
			printf("Case #%d: O won\n",cc+1);
		else if(unfinish)
			printf("Case #%d: Game has not completed\n",cc+1);
		else
			printf("Case #%d: Draw\n",cc+1);
		
	}
	return 0;
}