#pragma once
#include "taskBase.h"

class TaskSolution : public TaskBase
{
public:
	TaskSolution(std::istream &is)
		: TaskBase(is)
	{
	}

	void readData()
	{
		vs.resize(4);
		for(int i = 0; i < 4; i++)
		{
			cin >> vs[i];
		}
	}

	void solve()
	{
		int cd = 0;
		for(int i = 0; i < 4; i++)
		{
			int co, cx, ct;

			co = cx = ct = 0;
			for(int j = 0; j < 4; j++)
			{
				switch(vs[i][j])
				{
				case 'X':
					cx++;
					break;
				case 'O':
					co++;
					break;
				case 'T':
					ct++;
					break;
				case '.':
					cd++;
					break;
				}
			}
			if(co + ct == 4)
			{
				cout << "O won";
				return;
			}
			if(cx + ct == 4)
			{
				cout << "X won";
				return;
			}

			co = cx = ct = 0;
			for(int j = 0; j < 4; j++)
			{
				switch(vs[j][i])
				{
				case 'X':
					cx++;
					break;
				case 'O':
					co++;
					break;
				case 'T':
					ct++;
					break;
				case '.':
					cd++;
					break;
				}
			}
			if(co + ct == 4)
			{
				cout << "O won";
				return;
			}
			if(cx + ct == 4)
			{
				cout << "X won";
				return;
			}
		}

		int co, cx, ct;

		co = cx = ct = 0;
		for(int i = 0; i < 4; i++)
		{
			switch(vs[i][i])
			{
			case 'X':
				cx++;
				break;
			case 'O':
				co++;
				break;
			case 'T':
				ct++;
				break;
			}
		}
		if(co + ct == 4)
		{
			cout << "O won";
			return;
		}
		if(cx + ct == 4)
		{
			cout << "X won";
			return;
		}

		co = cx = ct = 0;
		for(int i = 0; i < 4; i++)
		{
			switch(vs[3 - i][i])
			{
			case 'X':
				cx++;
				break;
			case 'O':
				co++;
				break;
			case 'T':
				ct++;
				break;
			}
		}
		if(co + ct == 4)
		{
			cout << "O won";
			return;
		}
		if(cx + ct == 4)
		{
			cout << "X won";
			return;
		}
		if(cd == 0) cout << "Draw";
		else cout << "Game has not completed";
	}

private:

	std::vector<std::string> vs;
};
