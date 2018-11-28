#include<iostream>
using namespace std;
int caseNum;
char map[4][4];
int symbolCount[3]={0};
int ans;
bool isWin;
int emptyCount=0;
void checkType(char input)
{
	if(input=='O')
		symbolCount[0]++;
	else if(input=='X')
		symbolCount[1]++;
	else if(input=='T')
		symbolCount[2]++;
}
int checkWin()
{
	if(symbolCount[0]==4)
		return 1;
	if(symbolCount[1]==4)
		return 2;
	if(symbolCount[0]==3 && symbolCount[2]==1)
		return 1;
	if(symbolCount[1]==3 && symbolCount[2]==1)
		return 2;
	return 0;	
}
int win(int who,int index)
{
	if(who==1)
	{
		printf("Case #%d: O won\n",index);
		return 1;
	}
	else if (who==2)	
	{
		printf("Case #%d: X won\n",index);
		return 1;
	}
	return 0;
}
int main()
{
	cin>>caseNum;
	for(int i=0;i<caseNum;i++)
	{
		memset(symbolCount,0,3*sizeof(int));
		isWin =false;
		emptyCount = 0;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
			{
				cin>>map[j][k];
				checkType(map[j][k]);
				if(map[j][k]=='.')
					emptyCount++;
			}
		//check complete
		if( (symbolCount[1]+symbolCount[2])<4 && (symbolCount[0]+symbolCount[2])<4)
		{
			printf("Case #%d: Game has not completed\n",i+1);
			continue;
		}
		//check row
		for(int j=0;j<4;j++)
		{
			memset(symbolCount,0,3*sizeof(int));
			checkType(map[j][0]);		
			checkType(map[j][1]);		
			checkType(map[j][2]);		
			checkType(map[j][3]);		
			ans = checkWin();
			if(win(ans,i+1))
			{
				isWin = true;
				break;
			}
		}
		if(isWin)
			continue;

		//check columni
		for(int j=0;j<4;j++)
		{
			memset(symbolCount,0,3*sizeof(int));
			checkType(map[0][j]);		
			checkType(map[1][j]);		
			checkType(map[2][j]);		
			checkType(map[3][j]);		
			ans = checkWin();
			if(win(ans,i+1))
			{
				isWin = true;
				break;
			}
		}
		if(isWin)
			continue;
		//checkdiagonal
		memset(symbolCount,0,3*sizeof(int));
		checkType(map[0][0]);
		checkType(map[1][1]);
		checkType(map[2][2]);
		checkType(map[3][3]);
		ans = checkWin();
		if(win(ans,i+1))
			isWin = true;
		if(isWin)
			continue;

		memset(symbolCount,0,3*sizeof(int));
		checkType(map[3][0]);
		checkType(map[2][1]);
		checkType(map[1][2]);
		checkType(map[0][3]);
		ans = checkWin();
		if(win(ans,i+1))
			isWin = true;
		if(isWin)
			continue;
		if(emptyCount==0)	
			printf("Case #%d: Draw\n",i+1);
		else	
			printf("Case #%d: Game has not completed\n",i+1);
	}

}
