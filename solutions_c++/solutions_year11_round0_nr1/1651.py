#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <list>
using namespace::std;

list<int> OButtons;
list<int> BButtons;
vector<char> Roles;
vector<int> Buttons;
/*
 * 这个模拟写的很烂，主要是因为没有考虑到1.list为空的时候，pop_front怎么办；2.和昨天晚上一样，终止条件误写为list.size() > 1，昨天是 i < k - 1，╮(╯▽╰)╭。
 */
int sign(int a)
{
	if (a > 0)
	{
		return -1;
	}
	else if (a == 0)
	{
		return 0;
	}
	else 
	{
		return 1;
	}
}

int main()
{
	char R;
	int P;
	int T;
	int N;
	int i, j;
	int OPos = 1;
	int BPos = 1;
	int OTime = -1;
	int BTime = -1;
	int Odir = 0;
	int Bdir = 0;
	int totalTime = 0;
	cin >> T;
	ofstream outfile;
	outfile.open("D:\\out",ofstream::out);
	
	for (i = 0; i < T; i++)
	{
		cin >> N;
		for (j = 0; j < N; j++)
		{
			cin >> R;
			cin >> P;
			if (R == 'O')
			{
				OButtons.push_back(P);
			}
			else
			{
				BButtons.push_back(P);
			}

			Roles.push_back(R);
			Buttons.push_back(P);
		}


		for (j = 0; j < N; j++)
		{
			R = Roles[j];
			P = Buttons[j];

			if (OButtons.size() > 0)
			{
				OTime = abs(OPos - OButtons.front());
				Odir = sign(OPos - OButtons.front());
			}
			else
			{
				OTime = 0;
				Odir = 0;
			}
			
			if (BButtons.size() > 0)
			{
				BTime = abs(BPos - BButtons.front());
				Bdir = sign(BPos - BButtons.front());
			}
			else
			{
				BTime = 0;
				Bdir = 0;
			}			

			if (R == 'O')
			{
				if (OTime < BTime)
				{
					OPos = OButtons.front();
					BPos += Bdir * (OTime + 1);

				}
				else
				{
					OPos = OButtons.front();
					if (BButtons.size() > 0)
						BPos = BButtons.front();
				}

				OButtons.pop_front();
				totalTime += OTime + 1;
				cout << "Opos" << OPos << endl;
				cout << "Bpos" << BPos << endl;
			}
			else if (R == 'B')
			{
				if (BTime < OTime)
				{
					BPos = BButtons.front();
					OPos += Odir * (BTime + 1);
				}
				else
				{
					if (OButtons.size() > 0)
						OPos = OButtons.front();
					BPos = BButtons.front();
				}

				BButtons.pop_front();
				totalTime += BTime + 1;
				cout << "Opos" << OPos << endl;
				cout << "Bpos" << BPos << endl;
			}

		}

		//output
		outfile << "Case #" << i + 1 << ": " << totalTime << endl;

		OPos = 1;
		BPos = 1;
		OTime = -1;
		BTime = -1;
		Odir = 0;
		Bdir = 0;
		totalTime = 0;
		OButtons.clear();
		BButtons.clear();
		Roles.clear();
		Buttons.clear();
	}

	outfile.close();


	return 0;
}
