#include<iostream>
#include<cstdio>
using namespace std;

char chk(char a[][5])
{
	int i,count1,count2,f,j;
	int count=0;
	char ch;
	for(i=0;i<4;i++) {
		count1=count2 = 0;
		f = 0;
		for(j=0;j<4;j++) {
			if((a[i][j]=='X') || (a[i][j]=='O') || (a[i][j]=='T'))
			count++;
			if(a[i][j]=='X') {
				count1++;
				ch = 'X';
			}
			else if(a[i][j]=='O') {
				count2++;
				ch = 'O';
			}	
			else if(a[i][j]=='T') {
				f = 1;
				count2++;
				count1++;
			}
		}
		if(count1 == 4)
		return 'X';
		if(count2 == 4)
		return 'O';
	}
		for(i=0;i<4;i++) {
		count1 =count2= 0;
		f = 0;
		for(j=0;j<4;j++) {
			if(a[j][i]=='X') {
				count1++;
				ch = 'X';
			}
			else if(a[j][i]=='O') {
				count2++;
				ch = 'O';
			}	
			else if(a[j][i]=='T') {
				f = 1;
				count2++;
				count1++;
			}
		}
		if(count1 == 4)
		return 'X';
		if(count2 == 4)
		return 'O';
	}
		count1 =count2= 0;
		f = 0;
		for(j=0;j<4;j++) {
			if(a[j][j]=='X') {
				count1++;
				ch = 'X';
			}
			else if(a[j][j]=='O') {
				count2++;
				ch = 'O';
			}	
			else if(a[j][j]=='T') {
				f = 1;
				count2++;
				count1++;
			}
		}
		if(count1 == 4)
		return 'X';
		if(count2 == 4)
		return 'O';
		
		count1 =count2= 0;
		f = 0;
		for(j=0;j<4;j++) {
			if(a[j][3-j]=='X') {
				count1++;
				ch = 'X';
			}
			else if(a[j][3-j]=='O') {
				count2++;
				ch = 'O';
			}	
			else if(a[j][3-j]=='T') {
				f = 1;
				count2++;
				count1++;
			}
		}
		if(count1 == 4)
		return 'X';
		if(count2 == 4)
		return 'O';
		if(count == 16)
		return 'd';
		if(count != 16)
		return 'n';
}
int main()
{
	int t,k,i;
	char a[5][5];
	scanf("%d",&t);
	getchar();
	char p;
	for(k=1;k<=t;k++) {
		for(i=0;i<4;i++)
		gets(a[i]);
	
		p = chk(a);
		if(p=='X')
		printf("Case #%d: X won\n",k);
		else if(p=='O')
		printf("Case #%d: O won\n",k);
		else if(p=='d')
		printf("Case #%d: Draw\n",k); 
		else if(p=='n')
		printf("Case #%d: Game has not completed\n",k); 
		getchar();
	}
	return 0;
}

