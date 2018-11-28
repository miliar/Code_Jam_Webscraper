// CodeJam2011Quali.cpp : 定义控制台应用程序的入口点。
//
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(int argc, char* argv[])
{
	fstream file("A-large.in");
	fstream outfile("A-large.out");
	int cases;
	file >> cases;
	int index = 1;

	while(cases)
	{
		vector<char> v_color;
		vector<int> v_btn;
		int N;
		file >> N;
		while(N)
		{
			char color;
			int btn;
			file >> color >> btn;
			v_color.push_back(color);
			v_btn.push_back(btn);
			N--;
		}

		int prevPosO, prevPosB, curPosO, curPosB;
		prevPosO = 1; prevPosB = 1; curPosO = 1; curPosB = 1;
		bool whichColor = false;
		if(v_color[0] == 'O')
		{
			whichColor = true;
			prevPosO = v_btn[0];
			curPosO = v_btn[0];
		}
		else
		{
			prevPosB = v_btn[0];
			curPosB = v_btn[0];
		}

		int temp = v_btn[0];
		int res = temp;
		for(int i = 1; i < v_color.size(); i++)
		{
			if(v_color[i] == v_color[i-1])
			{
				temp += abs(v_btn[i]-v_btn[i-1]) + 1;
				res += abs(v_btn[i]-v_btn[i-1])+1;
				if(whichColor)
					prevPosO = v_btn[i];
				else
					prevPosB = v_btn[i];
			}
			else
			{
				int temp2;
				if(whichColor)
					temp2 = prevPosB;
				else
					temp2 = prevPosO;
				if(temp < abs(v_btn[i] - temp2)+1)
				{
					temp = abs(v_btn[i] - temp2)+1 - temp;
					res += temp;
				}
				else
				{
					res += 1;
					temp = 1;
				}
				if(whichColor)
					prevPosB = v_btn[i];
				else
					prevPosO = v_btn[i];
				whichColor = !whichColor;
			}			
		}

		outfile << "Case #" << index << ": " << res << endl;
		index++;
		cases--;
	}

	file.close();
	outfile.close();
	return 0;
}

