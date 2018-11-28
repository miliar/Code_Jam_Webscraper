#include<iostream>
#include<fstream>
#include<string>

using namespace std;
char convert(char m)
{
	if(int(m)>64 & int(m)<91)
		m=char(int(m)+32);
	if(m=='a')
		m='y';
	else if(m=='b')
		m='h';
	else if(m=='c')
		m='e';
	else if(m=='d')
		m='s';
	else if(m=='e')
		m='o';
	else if(m=='f')
		m='c';
	else if(m=='g')
		m='v';
	else if(m=='h')
		m='x';
	else if(m=='i')
		m='d';
	else if(m=='j')
		m='u';
	else if(m=='k')
		m='i';
	else if(m=='l')
		m='g';
	else if(m=='m')
		m='l';
	else if(m=='n')
		m='b';
	else if(m=='o')
		m='k';
	else if(m=='p')
		m='r';
	else if(m=='q')
		m='z';
	else if(m=='r')
		m='t';
	else if(m=='s')
		m='n';
	else if(m=='t')
		m='w';
	else if(m=='u')
		m='j';
	else if(m=='v')
		m='p';
	else if(m=='w')
		m='f';
	else if(m=='x')
		m='m';
	else if(m=='y')
		m='a';
	else if(m=='z')
		m='q';
	else 
		m=m;

	return m;
}

void main()
{
	int i,j,k,m;
	string line[31],st;
	ifstream ifile("A-small-attempt0.in");
	ofstream ofile("output.txt");
	if (ifile.is_open())
	{
		ifile>>i;
		//i=i-48;
		cout<<i<<endl;
		getline(ifile,line[0]);
		for(j=0;j<i;j++)
		{
			
			getline(ifile,line[j]);
			k=line[j].length();
			st=line[j];
			
			for(m=0;m<k;m++)
			{
				
				st[m]=convert(st[m]);
			}
			line[j]=st;
			ofile<<"Case #"<<j+1<<": "<<st<<endl;
		}
	}
	cin>>st[0];
}