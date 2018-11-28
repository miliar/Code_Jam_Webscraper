#include<stdio.h>
#include<stdlib.h>
#define PAUSE system("pause")
const char Status[4][30]={"X won","O won","Draw","Game has not completed"};
char A[5][5];
bool win(const char P)
{
	int i,j;
	bool m1,mr;
	m1=mr=1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
			if(A[i][j]!=P && A[i][j]!='T') break;
		if(j==4) return 1;
		for(j=0;j<4;j++)
			if(A[j][i]!=P && A[j][i]!='T') break;
		if(j==4) return 1;
		if(A[i][i]!=P && A[i][i]!='T') m1=0;
		if(A[i][3-i]!=P && A[i][3-i]!='T') mr=0;
	}
	return (m1 || mr);
}
int result()
{
	if(win('X')) return 0;
	if(win('O')) return 1;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(A[i][j]=='.') return 3;
	return 2;
}
main()
{
//	freopen("A_large.in","r",stdin);
//	freopen("A_large_out.txt","w",stdout);
	int Test,Case,i;
	scanf("%d",&Test);
	for(Case=1;Case<=Test;Case++)
	{
		getchar();
		for(i=0;i<4;i++) gets(A[i]);
		printf("Case #%d: ",Case);
		puts(Status[result()]);
	}
}
