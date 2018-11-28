#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("out.txt");
	int T;
	in>>T;
	char arr[26];
	arr[0]='y';
	arr[1]='h';
	arr[2]='e';
	arr[3]='s';
	arr[4]='o';
	arr[5]='c';
	arr[6]='v';
	arr[7]='x';
	arr[8]='d';
	arr[9]='u';
	arr[10]='i';
	arr[11]='g';
	arr[12]='l';
	arr[13]='b';
	arr[14]='k';
	arr[15]='r';
	arr[16]='z';
	arr[17]='t';
	arr[18]='n';
	arr[19]='w';
	arr[20]='j';
	arr[21]='p';
	arr[22]='f';
	arr[23]='m';
	arr[24]='a';
	arr[25]='q';
	string line,outline;
	int val;
	getline(in,line);
	for(int i=0;i<T;i++)
	{
		outline="";
		getline(in,line);
		for(int j=0;j<line.size();j++)
		{
			if(line[j]==' ')
			{
				outline=outline+" ";
				continue;
			}
			val=line[j]-'a';
			outline=outline+arr[val];
		}
		if(i+1==T)
		{
			out<<"Case #"<<i+1<<": "<<outline;
		}
		else
		{
			out<<"Case #"<<i+1<<": "<<outline<<endl;
		}
	}
	in.close();
	out.close();
	return 0;
}