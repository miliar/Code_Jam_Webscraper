#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	char str[101];
	char values[26];
	int n;
	cin>>n;
	//cout<<"lol";
		values[0]='y';
		values[1]='h';
		values[2]='e';
		values[3]='s';
		values[4]='o';
		values[5]='c';
		values[6]='v';
		values[7]='x';
		values[8]='d';
		values[9]='u';
		values[10]='i';
		values[11]='g';
		values[12]='l';
		values[13]='b';
		values[14]='k';
		values[15]='r';
		values[16]='z';
		values[17]='t';
		values[18]='n';
		values[19]='w';
		values[20]='j';
		values[21]='p';
		values[22]='f';
		values[23]='m';
		values[24]='a';
		values[25]='q';
		
	//fflush(stdin);
	for(int j=0;j<=n;j++)
	{
		
		gets(str);
		
		if(j!=0)
		{
		int len=strlen(str);
		cout<<"Case #"<<j<<": ";
		for(int i=0;i<len;i++)
		{
			if(str[i]==' ') cout<<" ";
			
			else
			{
				int ascii=int(str[i]);
				ascii=ascii-97;
				cout<<values[ascii];
			}
			
		}
		
		cout<<endl;
		}
	}
	

	return 0;
}
