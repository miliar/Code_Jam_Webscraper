#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>

using namespace std;

struct board
{
	vector< vector<char> > config;

	board(vector< vector<char> > con) : config(con) {};

	bool won_r(char ch, int n)//line number
	{
		for(char c : config[n])
		{
			if(c != 'T' && c != ch)
			{
				return false;
			}
		}
		return true;
	}

	bool won_c(char ch, int n)//column number
	{
		for(int i=0;i<4;i++)
		{
			char c = config[i][n];
			if(c != 'T' && c != ch)
			{
				return false;
			}
		}
		return true;
	}

	bool won_diag(char ch)
	{
		vector<char> d1, d2;
		for(int i=0;i<4;i++)
		{
			d1.push_back(config[i][i]);
			d2.push_back(config[i][3-i]);
		}
		bool t1=true, t2=true;
		for(char c : d1)
		{
			if(c != 'T' && c != ch)
			{
				t1=false;
				break;
			}
		}
		for(char c : d2)
		{
			if(c != 'T' && c != ch)
			{
				t2=false;
				break;
			}
		}
		return t1||t2;
	}

	bool has_won(char ch)
	{
		return (won_diag(ch) || won_r(ch, 0) || won_r(ch, 1) || won_r(ch, 2) || won_r(ch, 3) || won_c(ch, 0) || won_c(ch, 1) || won_c(ch, 2) || won_c(ch, 3));
	}

	bool incomplete()
	{
		for(vector<char> vect_ch : config)
		{
			for(char ch : vect_ch)
			{
				if(ch == '.')
				{
					return true;
				}
			}
		}
		return false;
	}

	void print()
	{
		for(int i=0;i<4;i++)
		{
			for(int k=0;k<4;k++)
			{
				cout<<config[i][k]<<" ";
			}
			cout<<endl;
		}
	
	}

};

vector< vector<char> > get_array(ifstream& fin)
{
	vector< vector<char> > answer;
	fin.get();//newline
	for(int i=0;i<4;i++)
	{
		vector<char> line;
		for(int k=0;k<4;k++)
		{
			line.push_back(fin.get());
		}
		answer.push_back(line);
		fin.get();//newline
	}
	return answer;
}

int main()
{
	ifstream fin("tictac.in");
	int T;
	fin>>T;

	vector<board> trials;

	ofstream fout("tictac.out");
	for(int i=0;i<T;i++)
	{
		board b = get_array(fin);
		fout<<"Case #"<<(i+1)<<": ";
		if(b.has_won('X'))
		{
			fout<<"X won";
		}
		else if(b.has_won('O'))
		{
			fout<<"O won";
		}
		else if(b.incomplete())
		{
			fout<<"Game has not completed";
		}
		else
		{
			fout<<"Draw";
		}
		fout<<endl;
	}

	return 1;
}
