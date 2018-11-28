#include<conio.h>
#include<iostream>
#include <iomanip>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>

using namespace std;

class Data
{
public:
	vector<string> data;

	Data(string fileName);
	void display(void);
private:
	Data();
};

Data::Data(string fileName)
{
	fstream in("input.txt");
	string firstLine;
	getline(in, firstLine);
	istringstream firstLineStream(firstLine);
	int dataLength;
	firstLineStream >> dataLength;
	for(int i=0; i<dataLength; i++)
	{
		string line;
		getline(in, line);
		this->data.push_back(line);
	}
}

void Data::display()
{
	cout<<this->data.size()<<endl;
	for(int i=0; i<(this->data).size(); i++)
		cout<<this->data[i]<<endl;
}

int violent_countSeq(const string & source, const string & target)
{
	const int length = target.length();
	vector<int> strPos(length);
	strPos[0] = -1;
	int counter = 0;
	int currentCharNum = 0;

	while(true)
	{
		int pos = source.find(target[currentCharNum], strPos[currentCharNum] + 1);
		if(pos == string::npos)
		{
			currentCharNum--;
			if(currentCharNum == -1)
				break;
		}
		else
		{
			strPos[currentCharNum] = pos;
			if(currentCharNum == length - 1)
			{
				counter++;
			}
			else
			{
				currentCharNum++;
				strPos[currentCharNum] = pos;
			}
		}
	}

	return counter;
}


int main(int argc, char *argv[])
{
	Data data(string("input.txt"));
	data.display();

	string target("welcome to code jam");
	

	fstream outputFile("output.txt",ios::out);
	for(int i=0; i<data.data.size(); i++)
	{
		int result = violent_countSeq(data.data[i], target);
		cout<<i<<": "<<result<<endl;
		outputFile<<"Case #"<<i+1<<": "<<setfill('0')<<setw(4)<<setiosflags(ios::right)<<result<<endl;
	}
	_getch();
}