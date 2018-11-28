#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

using namespace std;

//typedef vector<int> VectorInt;

int main(int argc, char** argv) {
	int casen = 0;
	ifstream ifile;
	ofstream ofile;
	//ifile.open("sample.txt");
	//ifile.open("A-small-attempt0.in");
	ifile.open("A-large.in");
	ofile.open("output.txt");
	ifile >> casen;
	//cout << casen;
	string buffer;
	buffer.resize(16);
	memset((void*)buffer.c_str(), 0, buffer.size());
	for (int c=0; c<casen; c++)
	{
		char* pt = (char*)buffer.c_str();
		for (int i=0;i<4;i++)
		{
			string tmpbuf;
			ifile >> tmpbuf;
			const char* tmppt = tmpbuf.c_str();
			for (int j=0;j<4;j++)
			{
				*pt = tmppt[j];
				cout << *pt;
				pt++;
			}
			cout << endl;
		}
		int result, scrx, scro, comencing;
		result = -1;
		comencing = 0;
		pt = (char*)buffer.c_str();
		for (int x=0;x<4&result==-1;x++)
		{
			scrx = 0;
			scro = 0;
			for (int y=0;y<4&result==-1;y++)
			{
				if (pt[y*4+x]=='.') comencing = 1;
				if (pt[y*4+x]=='X') scrx++;
				if (pt[y*4+x]=='O') scro++;
				if (pt[y*4+x]=='T')
				{
					scrx++;
					scro++;
				}
				if (scrx>=4) result = 1;
				if (scro>=4) result = 2;
			}
		}
		for (int y=0;y<4&result==-1;y++)
		{
			scrx = 0;
			scro = 0;
			for (int x=0;x<4&result==-1;x++)
			{
				if (pt[y*4+x]=='X') scrx++;
				if (pt[y*4+x]=='O') scro++;
				if (pt[y*4+x]=='T')
				{
					scrx++;
					scro++;
				}
				if (scrx>=4) result = 1;
				if (scro>=4) result = 2;
			}
		}
		scrx = 0;
		scro = 0;
		for (int x=0;x<4&result==-1;x++)
		{
			if (pt[x*4+x]=='X') scrx++;
			if (pt[x*4+x]=='O') scro++;
			if (pt[x*4+x]=='T')
			{
				scrx++;
				scro++;
			}
		}
		if (scrx>=4) result = 1;
		if (scro>=4) result = 2;
		scrx = 0;
		scro = 0;
		for (int x=0;x<4&result==-1;x++)
		{
			if (pt[x*4+(3-x)]=='X') scrx++;
			if (pt[x*4+(3-x)]=='O') scro++;
			if (pt[x*4+(3-x)]=='T')
			{
				scrx++;
				scro++;
			}
		}
		if (scrx>=4) result = 1;
		if (scro>=4) result = 2;
		string msg = "Game has not completed";
		if (result==1)
		{
			msg = "X won";
		}
		else if (result==2)
		{
			msg = "O won";
		}
		else
		{
			if (!comencing)
			{
				msg = "Draw";
			}
		}
		cout << "Case #" << c+1 << ": " << msg << endl;
		ofile << "Case #" << c+1 << ": " << msg << endl;
	}
	ifile.close();
	ofile.close();
	return 0;
}
