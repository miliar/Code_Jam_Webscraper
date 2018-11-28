#include <iostream>
#include <fstream>
using namespace std;

#define INPUT "A-large.in"

struct dot
{
	int color;  //B means 1;  O means 0
	int no;
};

struct line
{
	int num;
	dot* po;
};	

line* readin(int& n)
{
	ifstream fin (INPUT);
	fin >> n;
	line* result = new line[n];
	for (int i = 0; i < n; i++)
	{
		fin >> result[i].num;
		result[i].po = new dot[result[i].num];
		char tmp;
		for ( int j = 0; j < result[i].num; j++)
		{
			fin >> tmp;
			if (tmp == 'O') result[i].po[j].color = 0;
			if (tmp == 'B') result[i].po[j].color = 1;
			fin >> result[i].po[j].no;
		}
	}
	return result;
}

void check(const line& a, int& BNS, int& ONS, int count)
{
	for( int i = count; i < a.num; i++)
		if(a.po[i].color == 1)
		{
			BNS = a.po[i].no;
			break;
		}
	for( int i = count; i < a.num ; i++)
		if(a.po[i].color == 0)
		{
			ONS = a.po[i].no;
			break;
		}
}

int main()
{
	ofstream fout ("1.txt");
	int n;
	line* body= readin(n);
	int BS = 1, OS = 1;
	int BNS, ONS;
	int count = 0;
	int step = 0;
	int moved = 0;
	int movestate = 0;
	for (int ccc = 0; ccc < n; ccc++)
	{
		BS = 1, OS = 1;
		count = 0;
		step = 0;
		moved = 0;
		while (count < body[ccc].num)
		{
			step ++;
			check(body[ccc], BNS, ONS, count);
			if (BS != BNS)
			{
				if (BS < BNS) BS++;
				else BS--;
			}
			else if (body[ccc].po[count].color == 1)
			{
				movestate = 1;
			}
			if (OS != ONS)
			{
				if (OS < ONS) OS++;
				else OS--;
			}
			else if (body[ccc].po[count].color == 0)
			{
				movestate = 1;
			}
			if (movestate == 1)
			{
				count++;
				movestate = 0;
			}
		}
		fout << "Case #"<< ccc + 1 <<": " << step << endl;	
	}
	fout.close();
	return 0;
}
	