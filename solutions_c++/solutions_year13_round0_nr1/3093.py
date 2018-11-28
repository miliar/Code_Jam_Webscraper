#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int n;
	int num_x,num_o;
	bool flag;
	bool finishd,xwin,owin;
	bool next1 = false;
	char box[5][5];
	ifstream ist1("input1.in");
	ofstream ost1("output1.out");
	ist1 >>n;
	for (int i = 1;i<=n;i++)
	{
		num_x = 0;
		num_o = 0;
		flag = false;
		finishd = true;
		next1 = false;
		xwin = false;
		owin = false;
		for (int i1 = 1;i1<=4;i1++)
			for (int i2 = 1;i2<=4;i2++)
			{
			ist1 >>box[i1][i2];
			if (box[i1][i2] == '.') finishd = false;
			}
		for (int i1 = 1;i1<=4;i1++)					//By Line
		{
			num_x = 0;
			num_o = 0;
			flag = false;
			for (int i2 = 1;i2<=4;i2++)
			{
				if (box[i1][i2] == 'X') num_x++;
				if (box[i1][i2] == 'O') num_o++;
				if (box[i1][i2] == 'T') flag = true;
			}
			if ((num_x == 4)||((flag)&&(num_x == 3))) {ost1<<"Case #"<<i<<": X won"<<endl;next1 = true;}
			if ((num_o == 4)||((flag)&&(num_o == 3))) {ost1<<"Case #"<<i<<": O won"<<endl;next1 = true;}
		}
		if (!next1)
		{
		for (int i1 = 1;i1<=4;i1++)					//By row
		{
			num_x = 0;
			num_o = 0;
			flag = false;
			for (int i2 = 1;i2<=4;i2++)
			{
				if (box[i2][i1] == 'X') num_x++;
				if (box[i2][i1] == 'O') num_o++;
				if (box[i2][i1] == 'T') flag = true;
			}
			if ((num_x == 4)||((flag)&&(num_x == 3))) {ost1<<"Case #"<<i<<": X won"<<endl;next1 = true;}
			if ((num_o == 4)||((flag)&&(num_o == 3))) {ost1<<"Case #"<<i<<": O won"<<endl;next1 = true;}
		}
		}
		if (!next1)
		{
			num_x = 0;						//Diag1
			num_o = 0;
			flag = false;
		for (int i1 = 1;i1<=4;i1++)
		{
				if (box[i1][i1] == 'X') num_x++;
				if (box[i1][i1] == 'O') num_o++;
				if (box[i1][i1] == 'T') flag = true;
		}
			if ((num_x == 4)||((flag)&&(num_x == 3))) {ost1<<"Case #"<<i<<": X won"<<endl;next1 = true;}
			if ((num_o == 4)||((flag)&&(num_o == 3))) {ost1<<"Case #"<<i<<": O won"<<endl;next1 = true;}
		}
		if (!next1)
		{
		num_x = 0;						//Diag2
		num_o = 0;
		flag = false;
		for (int i1 = 1;i1<=4;i1++)
		{
				if (box[i1][5-i1] == 'X') num_x++;
				if (box[i1][5-i1] == 'O') num_o++;
				if (box[i1][5-i1] == 'T') flag = true;
		}
			if ((num_x == 4)||((flag)&&(num_x == 3))) {ost1<<"Case #"<<i<<": X won"<<endl;next1 = true;}
			if ((num_o == 4)||((flag)&&(num_o == 3))) {ost1<<"Case #"<<i<<": O won"<<endl;next1 = true;}
		}
		//No One Win
		if (!next1)
		{
		if (finishd) {ost1<<"Case #"<<i<<": Draw"<<endl;next1 = true;}
		else 
		ost1<<"Case #"<<i<<": Game has not completed"<<endl;
		}
	}
	ist1.close();
	ost1.close();
}