#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cstring>
#include<stdio.h>
#include<fstream>
#include<map>
#include<set>
using namespace std;

int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("A-small-attempt0.out");
	int C,k=1;
	cin>>C;
	cin.ignore(1);
	while(C--)
	{
		string G;
		getline(cin,G);
		string temp=G;
		for(int i=0;i<G.size();i++)
		{
			if(G[i]=='a')
				temp[i]='y';
			else if(G[i]=='b')
				temp[i]='h';
			else if(G[i]=='c')
				temp[i]='e';
			else if(G[i]=='d')
				temp[i]='s';
			else if(G[i]=='e')
				temp[i]='o';
			else if(G[i]=='f')
				temp[i]='c';
			else if(G[i]=='g')
				temp[i]='v';
			else if(G[i]=='h')
				temp[i]='x';
			else if(G[i]=='i')
				temp[i]='d';
			else if(G[i]=='j')
				temp[i]='u';
			else if(G[i]=='k')
				temp[i]='i';
			else if(G[i]=='l')
				temp[i]='g';
			else if(G[i]=='m')
				temp[i]='l';
			else if(G[i]=='n')
				temp[i]='b';
			else if(G[i]=='o')
				temp[i]='k';
			else if(G[i]=='p')
				temp[i]='r';
			else if(G[i]=='q')
				temp[i]='z';
			else if(G[i]=='r')
				temp[i]='t';
			else if(G[i]=='s')
				temp[i]='n';
			else if(G[i]=='t')
				temp[i]='w';
			else if(G[i]=='u')
				temp[i]='j';
			else if(G[i]=='v')
				temp[i]='p';
			else if(G[i]=='x')
				temp[i]='m';
			else if(G[i]=='w')
				temp[i]='f';
			else if(G[i]=='y')
				temp[i]='a';
			else if(G[i]=='z')
				temp[i]='q';
		}
		cout<<"Case #"<<k++<<": "<<temp<<endl;
	}





	return 0;
}