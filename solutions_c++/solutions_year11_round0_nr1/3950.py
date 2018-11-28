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
				todo += abs(position-currentOrange); // �����̴� �ð�
				todo++; //��ư ������ �ð�
				currentOrange = position;
				if(j >= (numData-1)) // ������ ������ �� ó���� ���
				{
					time += todo;
					break;
				}
				fin >> inputColor;
				while(inputColor != 'B' )
				{
					fin >> position;
					todo += abs(position-currentOrange); // �����̴� �ð�
					todo++; //��ư ������ �ð�
					currentOrange = position;
					j++;
					if(j >= (numData-1)) // ������ ������ �� ó���� ���
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

				//orange ó���ҵ��� blue�� ������ ���� ���
				if(abs(position-currentBlue) <= todo)
				{
					currentBlue = position;
				}
				//orange �� �� ó���ص� blue �� ������ ������
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
				todo += abs(position-currentBlue); // �����̴� �ð�
				todo++; //��ư ������ �ð�
				currentBlue = position;
				if(j >= (numData-1)) // ������ ������ �� ó���� ���
				{
					time += todo;
					break;
				}
				fin >> inputColor;
				while(inputColor != 'O' )
				{
					fin >> position;
					todo += abs(position-currentBlue); // �����̴� �ð�
					todo++; //��ư ������ �ð�
					currentBlue = position;
					j++;
					if(j >= (numData-1)) // ������ ������ �� ó���� ���
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
				//blue ó���ҵ��� orange�� ������ ���� ���
				if(abs(position-currentOrange) <= todo)
				{
					currentOrange = position;
				}
				//blue �� �� ó���ص� orange �� ������ ������
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