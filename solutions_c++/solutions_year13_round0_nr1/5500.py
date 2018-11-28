#include<iostream>
#include<string>
using namespace std;

char findLine(string line)
{
	bool x = false;
	bool o = false;
	bool dot = false;
	for(int i = 0; i < 4; i++)
	{
		if(line[i] == 'X')
			x = true;
		else if(line[i] == 'O')
			o = true;
		else if(line[i] == '.')
			dot = true;
	}
	if(!dot)
	{
		if(x && o)
			return 'd';
		if(x)
			return 'x';
		if(o)
			return 'o';
	}else
	{
		return 'n';
	}

}

int main()
{
	int num;
	cin>>num;
	for(int k = 1; k <= num; k++)
	{
		string line[10];
		char result[10];
		for(int i = 0; i < 4; i++)
		{
			cin>>line[i];
			result[i] = findLine(line[i]);
		}
		for(int i = 0; i < 4; i++)
		{
			char chs[4];
			for(int j = 0; j < 4; j++)
				chs[j] = line[j][i];
			string s(chs,4);
			line[4+i] = s;
			result[4+i] = findLine(line[4+i]);
		}
		char chs1[4];
		char chs2[4];
		for(int j = 0; j < 4; j++)
		{
			chs1[j] = line[j][j];
			chs2[j] = line[j][3-j];
		}
		string s1(chs1, 4);
		string s2(chs2, 4);

		line[8] = s1;
		line[9] = s2;

		result[8] = findLine(line[8]);
		result[9] = findLine(line[9]);

		bool x = false;
		bool o = false;
		bool n = false;
		bool d = false;
		for(int i = 0; i < 10; i++)
		{
			if(result[i] == 'x')
				x = true;
			else if(result[i] == 'o')
				o = true;
			else if(result[i] == 'n')
				n = true;
			else if(result[i] == 'd')
				d = true;
		}

		if(x)
			cout<<"Case #"<<k<<": X won"<<endl;
		else if(o)
			cout<<"Case #"<<k<<": O won"<<endl;
		else if(d)
			cout<<"Case #"<<k<<": Draw"<<endl;
		else
			cout<<"Case #"<<k<<": Game has not completed"<<endl;

		

		getchar();

	}


	//system("pause");


	return 0;
}