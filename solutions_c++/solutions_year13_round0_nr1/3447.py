#include <stdio.h>

void setHarsh(char temp,int harsh[])
{
	if(temp == 'X')harsh[0]++;
	else if(temp == 'O')harsh[1]++;
	else if(temp == 'T')harsh[2]++;
	else if(temp == '.')harsh[3]++;
}

bool setRes(int harsh[],char &ans)
{
	if(harsh[0] == 4 || (harsh[0] == 3 && harsh[2] == 1))
	{
		ans = 'X';
		return true;
	}

	if(harsh[1] == 4 || (harsh[1] == 3 && harsh[2] == 1))
	{
		ans = 'O';
		return true;
	}
	return false;
}

void test(char &ans,char panel[][5])
{
	bool leave = false;

	/* test row */
	for(int i=0;i<4;i++)
	{
		int harsh[4] = {0};
		for(int j=0;j<4;j++)setHarsh(panel[i][j],harsh);
		if(!leave && harsh[3] > 0)leave = true;
		if(setRes(harsh,ans))return;
	}

	/* test col */
	for(int j=0;j<4;j++)
	{
		int harsh[4] = {0,0,0,0};
		for(int i=0;i<4;i++)setHarsh(panel[i][j],harsh);
		if(setRes(harsh,ans))return;
	}

	/* test diag */

	int harsh[4] = {0,0,0,0};
	for(int j=0;j<4;j++)setHarsh(panel[j][j],harsh);
	if(setRes(harsh,ans))return;

	int hsh[4] = {0,0,0,0};
	for(int i=0;i<4;i++)setHarsh(panel[i][3-i],hsh);
	if(setRes(hsh,ans))return;

	/* test draw */
	if(!leave)
	{
		ans = 'D';
		return;
	}
	else
	{
		ans = 'G';
		return;
	}
}

int main(int argc, char const *argv[])
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	/* code */
	int tCase;
	char panel[4][5];
	char ans;

	scanf("%d",&tCase);

	for(int tNum = 1;tNum <= tCase; tNum++)
	{
		/* input */
		for(int i=0;i<4;i++)scanf("%s",panel[i]);

		test(ans,panel);

		printf("Case #%d: ",tNum);
		if(ans == 'X')printf("X won\n");
		else if(ans == 'O')printf("O won\n");
		else if(ans == 'D')printf("Draw\n");
		else if(ans == 'G')printf("Game has not completed\n");
	}

	return 0;
}
