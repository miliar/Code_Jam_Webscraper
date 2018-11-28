#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
#include<fstream>
using namespace std;
int check(string a[],char x)
{
	int i,j,sum=0,sum1=0,sum2=0,sum3=0;
	for(i=0;i<4;i++)
	{
		sum=0;sum1=0;
		for(j=0;j<4;j++)
		{
		if(a[i][j]=='T'||a[i][j]==x)
		sum++;
		if(a[j][i]=='T'||a[j][i]==x)
		sum1++;
		if(i==j)
		{
		if(a[i][i]=='T'||a[i][i]==x)
		sum2++;
		}
		if(i+j==3)
		{
		if(a[i][j]=='T'||a[i][j]==x)
		sum3++;
		}
		}
		if(sum==4||sum1==4)
		return 1;
	}
	if(sum==4||sum1==4||sum2==4||sum3==4)
		return 1;
}
int main()
{
 string a[4];
 int t,i,j,f=0,g=0,h=0,k=1;
 //ifstream fin;
 //fin.open("input.txt");
 //ofstream fout.open("output.txt");
 //fin>>t;
 scanf("%d",&t);
 while(t--)
 {
 	for(i=0;i<4;i++)
 	cin>>a[i];
 	h=0;g=0;f=0;
 	for(i=0;i<4;i++)
 	{
 	for(j=0;j<4;j++)
 	{
 	if(a[i][j]=='.')
 	{
 	h=1;
	break;	
 	}
    }
    }
 	printf("Case #%d: ",k++);
 	f=check(a,'X');
 	g=check(a,'O');
 	if(f==1&&g==0)
 	printf("X won\n");
 	else if(f==0&&g==1)
 	printf("O won\n");
 	else if(h==1)
 	printf("Game has not completed\n");
 	else 
 	printf("Draw\n");
 }	
}
