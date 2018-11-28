#include <iostream>
#include <fstream>
#include <list>
#include <string>

using namespace std;

class robot
{
public:
	int currpos;
	int turn;
	int loc;

	void moveup();
	void movedown();
	void push();
};

typedef list <robot, allocator<robot>> LIST;

class chain
{
public:
	LIST blue;
	LIST orange;

	void pushB (robot t)
	{
		blue.insert(blue.end(), t);
	}
	void pushO (robot t)
	{
		orange.insert(orange.end(), t);
	}

}input[102];


chain decode(char *str)
{
	class robot tmpO, tmpB;
	chain temp;
	//LIST::iterator it;
	int num = 0, turn = 1, N;
	char bot = 'x', ch;
	char *p1 = str, *p2;

	for (int i=0; *p1 != '\0'; ++i)
	{
		if (i == 0)
		{
			N = (int) strtol (p1, &p2, 10);
			p1 = p2;
			p2 = NULL;
		}
		//	p1++;
		//	N = (int)(*p1++) - 48;

		if (*p1 == ' ')
			p1++;

		if (isalpha(*p1))
		{
			ch = *p1++;
			p1++;
			num = (int) strtol (p1, &p2, 10);
			p1 = p2;
			p2 = NULL;

			if (toupper(ch) == 'O')
			{
				tmpO.turn = turn;
				tmpO.currpos = 1;
				tmpO.loc = num;
				temp.pushO(tmpO);
			}
			else
			{
				tmpB.turn = turn;
				tmpB.currpos = 1;
				tmpB.loc = num;
				temp.pushB(tmpB);
			}
			turn++;
			num = 0;
		}
	}
	{
		tmpB.turn = -1;
		tmpB.currpos = -1;
		tmpB.loc = -1;
		temp.pushB(tmpB);
	}
	{
		tmpO.turn = -1;
		tmpO.currpos = -1;
		tmpO.loc = -1;
		temp.pushO(tmpO);
	}
	//if ( N != (turn-1) )
	//{
	//	cout << "Mismatched N. Incorrect file !!!" << endl;
	//	exit (0);
	//}
	return temp;
}

int calculate(chain test)
{
	int i = 1;
	int step = 1, turn = 1, pB = 1, pO = 1;
	robot tB, tO;
	LIST::iterator itB = test.blue.begin(), itO = test.orange.begin();
	tB = *itB; tO = *itO;
	int N = test.blue.size() + test.orange.size(), turnState = turn;

	for (; turn <= N-2; ++i)
	{
		if (turn == turnState+1)
			turnState++;

		if (tO.turn == turnState)
		{
			if (tO.loc == pO)
			{
				cout << "O Turn: " << turnState << " switch@loc: " << pO;
				turn++;
				if (itO != test.orange.end())
					tO = *(++itO);
			}
			else if (tO.loc < pO)
			{
				pO--;
				cout << "O Turn: " << turnState << " mov@loc: " << pO;
			}
			else
			{
				pO++;
				cout << "O Turn: " << turnState << " mov@loc: " << pO;
			}
		}
		else
		{
			if (tO.loc < pO)
			{
				pO--;
				cout << "O Turn: " << turnState << " mov@loc: " << pO;
			}
			else if (tO.loc > pO)
			{
				pO++;
				cout << "O Turn: " << turnState << " mov@loc: " << pO;
			}
			else
			{
				cout << "O Turn: " << turnState << " stay@loc: " << pO;
			}
		}

		if (tB.turn == turnState)
		{
			if (tB.loc == pB)
			{
				cout << " B Turn: " << turnState << " switch@loc: " << pB << endl;
				turn++;
				if (itB != test.blue.end())
					tB = *(++itB);
			}
			else if (tB.loc < pB)
			{
				pB--;
				cout << " B Turn: " << turnState << " mov@loc: " << pB << endl;
			}
			else
			{
				pB++;
				cout << " B Turn: " << turnState << " mov@loc: " << pB << endl;
			}
		}
		else
		{
			if (tB.loc < pB)
			{
				pB--;
				cout << " B Turn: " << turnState << " mov@loc: " << pB << endl;
			}
			else if (tB.loc > pB)
			{
				pB++;
				cout << " B Turn: " << turnState << " mov@loc: " << pB << endl;
			}
			else
			{
				cout << " B Turn: " << turnState << " stay@loc: " << pB << endl;
			}
		}
	}
	return (i-1);
}

int main (int argc, char *argv[])
{
	ifstream f1;
	ofstream f2;
	f1.open(argv[1], ios_base::in);
	f2.open("output.txt", ios_base::out);
	int l = 0;
	//string str;
	char str[400], ch[5];
	chain tmp;

	f1.getline(ch, 5, '\n');
	while ( !f1.eof() )
	{
		f1.getline(str, 400, '\n');
		//input[l++] = decode(str);
		if (strlen(str) > 1)
		{
			tmp = decode(str);
			f2 << "Case #" << l+1 << ": " << calculate(tmp) << endl;
			l++;
		}
	}
	if (atoi(ch) != l)
	{
		cout << "Mismatched testcases. Exit !!!" << endl;
		exit (0);
	}
	f1.close();
	f2.close();
	return 0;
}