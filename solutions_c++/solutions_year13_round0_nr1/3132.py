#include<stdio.h>

const int SIZE = 4;
const int MAXT = 1000;
int T;
char A[SIZE][SIZE];
char str[16];




int isX(int l0,int l1)
{
	return A[l0][l1]=='X';
}
int isT(int l0,int l1)
{
	return A[l0][l1]=='T';
}
int isO(int l0,int l1)
{
	return A[l0][l1]=='O';
}
int calc()
{

 int l0,l1,nx,no,nt,wx,wo,isDot;
 
 wx=0;
 wo=0;
 isDot=0;
 //horizontal
 
 nx=no=nt=0;
 for(l0=0;l0<SIZE;l0++)
 {
	nx=no=nt=0;
 	for(l1=0;l1<SIZE;l1++)
	{
	nx+=isX(l1,l0);
	nt+=isT(l1,l0);
	no+=isO(l1,l0);	
	if(A[l1][l0]=='.')
	 isDot=1;
	}
	if((nt==1&&nx==3) || nx==4)
		wx++;
	if((nt==1&&no==3) || no==4)
		wo++;
 }

 //vertical
 nx=no=nt=0;
 for(l0=0;l0<SIZE;l0++)
 {
	nx=no=nt=0;
	for(l1=0;l1<SIZE;l1++)
	{
	nx+=isX(l0,l1);
	nt+=isT(l0,l1);
	no+=isO(l0,l1);
	}
	if((nt==1 && nx==3) || nx==4)
		wx++;
	if((nt==1 && no==3) || no==4)
		wo++;
 }

/////
nx=no=nt=0;

for(l0=0;l0<SIZE;l0++)
	{
	nx+=isX(SIZE-1-l0,l0);
	nt+=isT(SIZE-1-l0,l0);
	no+=isO(SIZE-1-l0,l0);
	}
	if((nt==1&&nx==3) || nx==4)
	wx++;
	if((nt==1&&no==3) || no==4)
	wo++;

nx=no=nt=0;
for(l0=0;l0<SIZE;l0++)
{
	nx+=isX(l0,l0);
	nt+=isT(l0,l0);
	no+=isO(l0,l0);
}
	if((nt==1&&nx==3)||nx==4)
	wx++;
	if((nt==1&&no==3)||no==4)
	wo++;


//printf("%d %d\n",wx,wo);

if( wx > 0 && wo >0)
return 3;

if( wx > 0 )
return 2;

if( wo > 0 )
return 1;

if(isDot==0)
return 3;


return 0;


}

void show(void)
{


	int l0,l1;

	for(l0=0;l0<SIZE;l0++)
	{
		for(l1=0;l1<SIZE;l1++)
		{
		printf("%c",A[l1][l0]);
		}
		printf("\n");
	}
	

}
int main(void)
{
	int l0, l1, l2;
	int t1, t2;

	freopen("./A-large.in","r",stdin);
	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		for(l1=0;l1<SIZE; l1++)
		{
			scanf("%s",str);
			A[0][l1]=str[0];
			A[1][l1]=str[1];
			A[2][l1]=str[2];
			A[3][l1]=str[3];
		}
//		show();
		t1=calc();
		printf("Case #%d: ",l0);
		if(t1==2)
		printf("X won\n");
		if(t1==3)
		printf("Draw\n");
		if(t1==1)	
		printf("O won\n");
		if(t1==0)	
		printf("Game has not completed\n");


	}
}
