#include<iostream>
#include<cstdio>

using namespace std;

char map(char ch)
{
	if(ch=='e')return 'o';
	if(ch=='j')return 'u';
	if(ch=='p')return 'r';
	if(ch=='m')return 'l';
	if(ch=='s')return 'n';
	if(ch=='l')return 'g';
	if(ch=='k')return 'i';
	if(ch=='d')return 's';
	if(ch=='x')return 'm';
	if(ch=='v')return 'p';
	if(ch=='n')return 'b';
	if(ch=='c')return 'e';
	if(ch=='r')return 't';
	if(ch=='i')return 'd';
	if(ch=='y')return 'a';
	if(ch=='a')return 'y';
	if(ch=='b')return 'h';
	if(ch=='f')return 'c';
	if(ch=='g')return 'v';
	if(ch=='h')return 'x';
	if(ch=='o')return 'k';
	if(ch=='t')return 'w';
	if(ch=='u')return 'j';
	if(ch=='w')return 'f';
	if(ch=='z')return 'q';
	if(ch=='q')return 'z';
	if(ch==' ')return ' ';
	else return ch;
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("probA.out","w",stdout);
	char ch;
	long int i,n;
	cin>>n;
	getchar();
	for(i=0;i<n;i++)
	{
		printf("Case #%ld: ",i+1);
		while(1)
		{
			ch=getchar();
			if(ch=='\n'||ch==EOF){cout<<endl;break;}
			else cout<<map(ch);


		}
	}

	return 0;

}
