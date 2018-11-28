#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main()
{
	ifstream fin("input.txt",ios::in);
	ofstream fout("output.txt",ios::out);

	int numCase,numData;
	char inputColor;
	int position;
	int todo=0;
	int i,j;
	int currentOrange = 1;
	int currentBlue = 1;
	int time=0;
	bool outFlag = false;

	fin >> numCase;

	for(i=0; i<numCase; i++)
	{
		currentOrange = currentBlue = 1;
		time = 0;
		todo = 0;
		position = 0;
		outFlag = false;

		fin >> numData;
		fin >> inputColor;
		fin >> position;
		for(j=0; j<numData; j++)
		{
			todo = 0;
			if(inputColor == 'O')
			{
				todo += abs(position-currentOrange); // 움직이는 시간
				todo++; //버튼 누르는 시간
				currentOrange = position;
				if(j >= (numData-1)) // 한줄을 끝까지 다 처리한 경우
				{
					time += todo;
					break;
				}
				fin >> inputColor;
				while(inputColor != 'B' )
				{
					fin >> position;
					todo += abs(position-currentOrange); // 움직이는 시간
					todo++; //버튼 누르는 시간
					currentOrange = position;
					j++;
					if(j >= (numData-1)) // 한줄을 끝까지 다 처리한 경우
					{
						time += todo;
						outFlag = true;
						break;
					}
					fin >> inputColor;
				}
				if(outFlag)
					break;
				fin >> position;

				//orange 처리할동안 blue는 목적지 가서 대기
				if(abs(position-currentBlue) <= todo)
				{
					currentBlue = position;
				}
				//orange 가 다 처리해도 blue 는 목적지 가는중
				else
				{
					if(position > currentBlue)
						currentBlue += todo;
					else
						currentBlue -= todo;

				}
				time += todo;

			}
			else
			{
				todo += abs(position-currentBlue); // 움직이는 시간
				todo++; //버튼 누르는 시간
				currentBlue = position;
				if(j >= (numData-1)) // 한줄을 끝까지 다 처리한 경우
				{
					time += todo;
					break;
				}
				fin >> inputColor;
				while(inputColor != 'O' )
				{
					fin >> position;
					todo += abs(position-currentBlue); // 움직이는 시간
					todo++; //버튼 누르는 시간
					currentBlue = position;
					j++;
					if(j >= (numData-1)) // 한줄을 끝까지 다 처리한 경우
					{
						time += todo;
						outFlag = true;
						break;
					}
					fin >> inputColor;
				}
				if(outFlag)
					break;
				fin >> position;
				//blue 처리할동안 orange는 목적지 가서 대기
				if(abs(position-currentOrange) <= todo)
				{
					currentOrange = position;
				}
				//blue 가 다 처리해도 orange 는 목적지 가는중
				else
				{
					if(position > currentOrange)
						currentOrange += todo;
					else
						currentOrange -= todo;

				}
				time += todo;
			}
		}
		fout << "Case #" << i+1 << ": " << time << endl;
	}
}