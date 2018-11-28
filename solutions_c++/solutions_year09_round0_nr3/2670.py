#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;


string search = "welcome to code jam";

int searchlength = 19;
char table[11][501];
void findchar(int c,int start,int *result);
int findindex(char c);
int main()
{
	int totalline;
	ifstream infile;
	infile.open("in");
    if (!infile) {
		cerr << "error: unable to open input file: "
			 << endl;
	    return -1;
	}
	ofstream outfile;
	outfile.open("out.txt");

	string meta;
	getline(infile,meta);
	istringstream stream(meta);
	stream >> totalline;
	int *answer = (int*)malloc(sizeof(int)*totalline);
	for(int i=0; i<totalline;i++)
	{
		string temp;
		getline(infile,temp);
		

		memset(table,0,sizeof(table));
		for (int s=0;s<(int)temp.size();s++)
		{
			if (findindex(temp[s])!=-1)
			{
				table[findindex(temp[s])][0]++;
				table[findindex(temp[s])][table[findindex(temp[s])][0]] = s;
			}
		}
		int result = 0;
		findchar(0,0,&result);
		cout<<result<<endl;
		answer[i] = result % 10000;
	}

	for (int j=0;j<totalline;j++)
	{
		outfile << "Case #"<<j+1<<": " << answer[j]/1000 <<(answer[j]/100)%10 << (answer[j]/10%10)<<(answer[j]%10)<<endl;
	}
	infile.close();
	outfile.close();
}

//find c th element in "search" 
void findchar(int c,int start,int *result)
{
	int index = findindex(search[c]);
	int m=1;
	while(m<=table[index][0])
	{
		if (table[index][m]>=start)
		{
			if (c == 18)
			{
				(*result)++;
			}
			else
			{
				findchar(c+1,table[index][m]+1,result);
			}
		}
		m++;
	}
}
int findindex(char c)
{
	switch(c)
	{
	case 'w':
		return 0;
	case 'e':
		return 1;
	case 'l':
		return 2;
	case 'c':
		return 3;
	case 'o':
		return 4;
	case 'm':
		return 5;
	case 't':
		return 6;
	case 'd':
		return 7;
	case 'j':
		return 8;
	case 'a':
		return 9;
	case ' ':
		return 10;

	}
	return -1;
}