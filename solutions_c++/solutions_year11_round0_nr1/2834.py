#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>

using namespace std;

struct Robot
{
	int start_pos;
	int start_time;

	Robot()
	{
		start_pos = 1;
		start_time = 0;
	}
};

int main(int argc, char* argv[])
{
	ifstream ifile("q1.in");
	ofstream ofile("a1.txt");

	int case_num;
	ifile >> case_num;

	for(int i=0;i<case_num;++i)
	{
		Robot robots[2];
		int btn_num;
		int cur_time = 0;
		ifile >> btn_num;
		for(int j=0;j<btn_num;++j)
		{
			char color;
			int dst;
			ifile >> color;
			ifile >> dst;
			Robot *ptr;
			if(color == 'O')
				ptr = robots;
			else
				ptr = robots+1;
			ptr->start_time = abs(dst - ptr->start_pos) + 1 + ptr->start_time;
			ptr->start_pos = dst;
			if(ptr->start_time <= cur_time)
				ptr->start_time = cur_time + 1;
			cur_time = ptr->start_time;
		}
		ofile << "Case #" << i+1 << ": " << cur_time << endl;
	}

	ifile.close();
	ofile.close();

	//system("pause");
	return 0;
}

