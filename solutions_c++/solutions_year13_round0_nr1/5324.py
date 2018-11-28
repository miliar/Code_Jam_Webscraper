#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int charcheck(char** input, int loc[8])
{
	int sum=0;
	for (int i=0,j=1;i<8;i+=2,j+=2)
	{
		if (input[loc[i]][loc[j]]=='X') sum+=1;
		else if (input[loc[i]][loc[j]]=='O') sum+=10;
		else if (input[loc[i]][loc[j]]=='T') sum+=50;
		else sum+=0;
	}
	return sum;
}

string check(char** input)
{
	int temp[10];
	int loc[][8] = {{0,0,0,1,0,2,0,3},{1,0,1,1,1,2,1,3},{2,0,2,1,2,2,2,3},{3,0,3,1,3,2,3,3},{0,0,1,0,2,0,3,0},{0,1,1,1,2,1,3,1},{0,2,1,2,2,2,3,2},{0,3,1,3,2,3,3,3},{0,0,1,1,2,2,3,3},{0,3,1,2,2,1,3,0}};
	for (int i=0;i<10;i++)
	{
		temp[i]=charcheck(input, loc[i]);
	}
	for (int i=0;i<10;i++)
	{
		switch (temp[i])
		{
		case 4: return "X won";
		case 53: return "X won";
		case 40: return "O won";
		case 80: return "O won";
		default: ;
		}
	}
	for(int i1=0; i1<4; i1++)
		for(int j1=0; j1<4; j1++)
			if(input[i1][j1]=='.')
				return "Game has not completed";
	return "Draw";
}

int main()
{
	char*** input;
	string line, strnum;
	int size;
	ifstream myfile ("A-large.in");
	if (myfile.is_open())
	{
		getline (myfile, strnum);
		size = atoi(strnum.c_str());
		input = new char**[atoi(strnum.c_str())];
		input[0]=new char*[4];
		input[0][0] = new char[4];
		input[0][1] = new char[4];
		input[0][2] = new char[4];
		input[0][3] = new char[4];
		for (int i=0, j=0; myfile.good();)
		{
			getline (myfile, line);
			if (line=="\0") {
				i++;j=0;
				input[i]=new char*[4];
				input[i][0] = new char[4];
				input[i][1] = new char[4];
				input[i][2] = new char[4];
				input[i][3] = new char[4];
			}
			else 
			{
				strcpy(input[i][j++], line.c_str());
			}
		}
		myfile.close();
	}
	else cout << "Unable to open file";

	ofstream youfile("output.txt");
	for (int i=0;i<size;i++)
	{
		string output = check(input[i]);
		youfile<<"Case #"<<i+1<<": "<<output<<endl;
	}

	system("pause");
}