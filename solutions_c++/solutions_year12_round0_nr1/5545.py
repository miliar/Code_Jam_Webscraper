#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	char ch[35][150],ch1[35][150];
	int i=0,j=0,t;
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt3.in",ios::in);
	fout.open("output.txt",ios::out);


	fin>>t;
	fin.seekg(3);
	
	while(!fin.eof())
	{
    fin.getline(ch[j],150,'\n');
	 j++;
	}
	

	
	for(int j=0;j<t;j++)
	{
	
	while(ch[j][i]!='\0')
	{
		switch(ch[j][i])
		{
		case 'a':
			ch1[j][i]='y';
			break;
		case 'b':
			ch1[j][i]='h';
			 break;
		case 'c':
			ch1[j][i]='e';
			break;
		case 'd':
			ch1[j][i]='s';
			break;
		case 'e':
			ch1[j][i]='o';
			break;
		case 'f':
			ch1[j][i]='c';
			break;
		case 'g':
			ch1[j][i]='v';
			break;
		case 'h':
			ch1[j][i]='x';
			break;
		case 'i':
			ch1[j][i]='d';
			break;
		case 'j':
			ch1[j][i]='u';
			break;
		case 'k':
			ch1[j][i]='i';
			break;
		case 'l':
			ch1[j][i]='g';
			break;
		case 'm':
			ch1[j][i]='l';
			break;
		case 'n':
			ch1[j][i]='b';
			break;
		case 'o':
			 ch1[j][i]='k';
			 break;
		case 'p':
			ch1[j][i]='r';
			break;
		case 'q':
			ch1[j][i]='z';
			break;
		case 'r':
			ch1[j][i]='t';
			break;
		case 's':
			ch1[j][i]='n';
			break;
		case 't':
			ch1[j][i]='w';
			break;
		case 'u':
			ch1[j][i]='j';
			break;
		case 'v':
			ch1[j][i]='p';
			break;
		case 'w':
			ch1[j][i]='f';
			break;
		case 'x':
			ch1[j][i]='m';
			break;
		case 'y':
			ch1[j][i]='a';
			break;
		case 'z':
			ch1[j][i]='q';
			break;
		case ' ':
			ch1[j][i]=' ';
			break;
		}
	i++;
	}

	ch1[j][i]='\0';
	i=0;
	}

	for(int j=0;j<t;j++)
		fout<<"Case #"<<j+1<<":"<<" "<<ch1[j]<<endl;
	fout.close();
	system("pause");
	}




