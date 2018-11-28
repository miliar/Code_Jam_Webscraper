#include<stdio.h>

int testCount;
int testStatus;

char test[4][4];

void readTest(){
	//printf("readTest\n");
	for(int i=0;i<4;i++){//y
		scanf("%s",&test[i]);
	}
}
void writeData(){
	//printf("writeData\n");
	for(int i=0;i<4;i++){//y
		for(int j=0;j<4;j++){//x
			printf("%c",test[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}
void solveTest(){
	//writeData();
	bool winX = false;
	bool winO = false;
	bool tableFull = true;

	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(test[i][j]=='.') tableFull = false;
		}

	for(int i=0;i<4;i++)
	{
		if((test[i][0]=='X' || test[i][0]=='T') && (test[i][1]=='X' || test[i][1]=='T') 
			&& (test[i][2]=='X' || test[i][2]=='T') && (test[i][3]=='X' || test[i][3]=='T'))winX = true;// рядки
		if((test[0][i]=='X' || test[0][i]=='T') && (test[1][i]=='X' || test[1][i]=='T') 
			&& (test[2][i]=='X' || test[2][i]=='T') && (test[3][i]=='X' || test[3][i]=='T'))winX = true;// стовпчики
	}

	if((test[0][0]=='X' || test[0][0]=='T') && (test[1][1]=='X' || test[1][1]=='T') 
			&& (test[2][2]=='X' || test[2][2]=='T') && (test[3][3]=='X' || test[3][3]=='T'))winX = true;//діагональ
	
	if((test[0][3]=='X' || test[0][3]=='T') && (test[1][2]=='X' || test[1][2]=='T') 
			&& (test[2][1]=='X' || test[2][1]=='T') && (test[3][0]=='X' || test[3][0]=='T'))winX = true;
	
	
	for(int i=0;i<4;i++)
	{
		if((test[i][0]=='O' || test[i][0]=='T') && (test[i][1]=='O' || test[i][1]=='T') 
			&& (test[i][2]=='O' || test[i][2]=='T') && (test[i][3]=='O' || test[i][3]=='T'))winO = true;// рядки
		if((test[0][i]=='O' || test[0][i]=='T') && (test[1][i]=='O' || test[1][i]=='T') 
			&& (test[2][i]=='O' || test[2][i]=='T') && (test[3][i]=='O' || test[3][i]=='T'))winO = true;// стовпчики
	}

	if((test[0][0]=='O' || test[0][0]=='T') && (test[1][1]=='O' || test[1][1]=='T') 
			&& (test[2][2]=='O' || test[2][2]=='T') && (test[3][3]=='O' || test[3][3]=='T'))winO = true;//діагональ
	
	if((test[0][3]=='O' || test[0][3]=='T') && (test[1][2]=='O' || test[1][2]=='T') 
			&& (test[2][1]=='O' || test[2][1]=='T') && (test[3][0]=='O' || test[3][0]=='T'))winO = true;
	//printf("winX: %s\n",(winX)?"true":"false");
	//printf("winO: %s\n",(winO)?"true":"false");
	if(winX) testStatus = 1;
	if(winO) testStatus = 2;
	if(!winX && !winO && tableFull) testStatus = 3;
	if(!winX && !winO && !tableFull) testStatus = 4;

}



int main(){
	freopen ("input.txt","r",stdin);
	freopen ("A-small-attempt0.out","w",stdout);
	scanf("%d",&testCount);
	//printf("Test Count = %d\n",testCount);
	for(int i=0;i<testCount;i++){
		//printf("Test Count = %d\n",testCount);
		readTest();
		if(i<testCount-1) scanf("\n");
		solveTest();
		printf("Case #%d: ",i+1);
		if(testStatus==1) printf("X won");
		if(testStatus==2) printf("O won");
		if(testStatus==3) printf("Draw");
		if(testStatus==4) printf("Game has not completed");
		if(i<testCount-1) printf("\n");
		
	}
	//printf("Test Count = %d\n",testCount);
	return 0;
}

