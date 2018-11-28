#include <fstream>
#include <sstream>
#include <string>
#include <cctype>
#include <vector>
#include <time.h>	//to measure the time
using namespace std;

bool VectorMatch(const vector<string> & winning, const vector<string> & list);
bool DotFind(const vector<string> & list);

bool DotFind(const vector<string> & list)
{
	for (int i = 0; i < 10; i++)
		if (list[i].find(".") != string::npos) //if there is a dot
			return true;
	return false;
}

bool VectorMatch(const vector<string> & winning, const vector<string> & list)
{
	for (int i = 0; i < 10; i++)
		for (int j = 0; j < 5; j++)
			if (winning[j] == list[i]) return true;
	return false;
}

int main()
{
	ifstream input("f.txt");
	ofstream output("out.txt");
	string line;
	int tekrar;
	getline(input,line);
	tekrar = atoi(line.c_str());
	vector<string> x;
	vector<string> o;
	x.push_back("XXXX");
	x.push_back("XXXT");
	x.push_back("XXTX");
	x.push_back("XTXX");
	x.push_back("TXXX");

	o.push_back("OOOO");
	o.push_back("OOOT");
	o.push_back("OOTO");
	o.push_back("OTOO");
	o.push_back("TOOO");

	for (int i = 1; i <= tekrar; i++)
	{
		//read table
		vector<string> list;
		string row1, row2, row3, row4;
		getline(input,row1);
		getline(input,row2);
		getline(input,row3);
		getline(input,row4);
		list.push_back(row1);
		list.push_back(row2);
		list.push_back(row3);
		list.push_back(row4);
		list.push_back(row1.substr(0,1) + row2.substr(0,1) + row3.substr(0,1) + row4.substr(0,1));
		list.push_back(row1.substr(1,1) + row2.substr(1,1) + row3.substr(1,1) + row4.substr(1,1));
		list.push_back(row1.substr(2,1) + row2.substr(2,1) + row3.substr(2,1) + row4.substr(2,1));
		list.push_back(row1.substr(3,1) + row2.substr(3,1) + row3.substr(3,1) + row4.substr(3,1));
		list.push_back(row1.substr(0,1) + row2.substr(1,1) + row3.substr(2,1) + row4.substr(3,1));
		list.push_back(row1.substr(3,1) + row2.substr(2,1) + row3.substr(1,1) + row4.substr(0,1));
		//find situation
		output << "Case #" << i << ": ";
		if (VectorMatch(x,list)) output << "X won" ;
		else if(VectorMatch(o,list)) output << "O won";
		else if(DotFind(list)) output << "Game has not completed";
		else output << "Draw";
		if (i != tekrar) { output << endl; getline(input,line);}
	}
	output.close();
	system("PAUSE");
	return 0;
}