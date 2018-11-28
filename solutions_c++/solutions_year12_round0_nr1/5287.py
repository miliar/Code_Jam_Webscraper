#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>
using namespace std;


int main()
{
	/*
	char google[27];
	for(int i=0;i<26;i++)
	{
		google[i] = 'a'+i;
	}
	google[26] = ' ';
	*/

	char map[27];
	map[0]='y';map[1]='h';map[2]='e';map[3]='s';map[4]='o';map[5]='c';
	map[6]='v';map[7]='x';map[8]='d';map[9]='u';map[10]='i';map[11]='g';
	map[12]='l';map[13]='b';map[14]='k';map[15]='r';map[16]='z';map[17]='t';
	map[18]='n';map[19]='w';map[20]='j';map[21]='p';map[22]='f';map[23]='m';
	map[24]='a';map[25]='q';map[26]=' ';
	/*
	ifstream in("A-small-attempt4.in");
	cin.rdbuf(in.rdbuf());
	ofstream out("a.out");
	cout.rdbuf(out.rdbuf());
	*/
	int T = 0;
	cin>>T;
	char G[110];
	char S[110];
	cin.ignore();//
	for(int i=0;i<T;i++)
	{
		cin.getline(G,110);
		int a = 0;
		while(1)
		{
			if(G[a]=='\0')
				break;
			if(G[a]==' ')
			{
				S[a] = ' ';
			}
			else
			{
				S[a] = map[(int)G[a]-97];
			}
			a++;
		}
		S[a] = '\0';
		cout<<"Case #"<<i+1<<": "<<S<<endl;
	}

//	system("pause");
	return 0;
}