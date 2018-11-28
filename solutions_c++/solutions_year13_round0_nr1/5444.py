#include <iostream>
#include <vector>
#include <string>
#include <fstream>

std::string find(std::vector<std::vector<char> > vect)
{

		
		bool acrossX = false;
		for(int i = 0; i < vect.size(); i++)
		{
			acrossX = true;
			for(int j = 0; j < vect[i].size(); j++)
			{
				if(vect[i][j] != 'X' && vect[i][j] != 'T')
					acrossX = false;
			}
			if(acrossX)
			{
				return "X won";
			}
		}
		bool acrossO= false;
		for(int i = 0; i < vect.size(); i++)
		{
			acrossO = true;
			for(int j = 0; j < vect[i].size(); j++)
			{
				if(vect[i][j] != 'O' && vect[i][j] != 'T')
					acrossO = false;
			}
			if(acrossO)
			{
				return "O won";
			}
		}
		bool downX = false;
		for(int i = 0; i < vect.size(); i++)
		{
			downX = true;
			for(int j = 0; j < vect[i].size(); j++)
			{
				if(vect[j][i] != 'X' && vect[i][j] != 'T')
					downX = false;
			}
			if(downX)
			{
				return "X won";
			}
		}
		bool downO = false;
		for(int i = 0; i < vect.size(); i++)
		{
			downO = true;
			for(int j = 0; j < vect[i].size(); j++)
			{
				if(vect[j][i] != 'O' && vect[i][j] != 'T')
					downO = false;
			}
			if(downO)
			{
				return "O won";
			}
		}
		bool diagdx = true;
		for(int i = 0; i < 4; i++)
		{
			if(vect[i][i] != 'X' && vect[i][i] != 'T')
			{
				diagdx = false;
			}
		}
		if(diagdx)
		{
			return "X won";
		}
		bool diagdo = true;
		for(int i = 0; i < 4; i++)
		{
			if(vect[i][i] != 'O' && vect[i][i] != 'T')
			{
				diagdo = false;
			}
		}
		if(diagdo)
		{
			return "O won";
		}
		bool diagux = true;
		for(int i = 0; i < 4; i++)
		{
			if(vect[i][3-i] != 'X' && vect[i][3-i] != 'T')
			{
				diagux = false;
			}
		}
		if(diagux)
		{
			return "X won";
		}
		bool diaguo = true;
		for(int i = 0; i < 4; i++)
		{
			if(vect[i][3-i] != 'O' && vect[i][3-i] != 'T')
			{
				diaguo = false;
			}
		}
		if(diaguo)
		{
			return "O won";
		}
	
	bool period =false;
	for(int i = 0; i < vect.size(); i++)
	{
		for(int j = 0; j < vect[i].size(); j++)
		{
			if(vect[i][j] == '.')
				period = true;
		}
	}
	if(period)
	{
		return "Game has not completed";
	}
	else
	{
		return "Draw";
	}
}
int main()
{
	std::ifstream fin;
	fin.open("A-small-attempt2.in");
	if(fin.fail())
	{
		std::cout << "Fail..." << std::endl;
		return 0;
	}
	int num;
	fin >> num;
	std::ofstream fout("A-small-attempt2.out");
	for(int i = 0; i < num; i++)
	{
		std::vector<std::vector<char> > vect;
		for(int j = 0; j < 4; j++)
		{
			std::vector<char> temp;
			for(int k = 0; k < 4; k++)
			{
				char t;
				fin >> t;
				temp.push_back(t);
			}
			vect.push_back(temp);
		}

		std::string a = find(vect);
		
		fout <<"Case #"<< i+1 << ": " << a << std::endl;
		
	}
	fout.close();
	return 0;
}