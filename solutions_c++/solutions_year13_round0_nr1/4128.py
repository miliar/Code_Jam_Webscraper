#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;

class A
{
private:
	bool checkRow(char ch, const vector<vector <char> > &board);
	bool checkColumn(char ch, const vector<vector <char> > &board);
	bool checkDiag(char ch, const vector<vector <char> > &board);
public:
	bool win(char ch, const vector<vector <char> > &board);
	bool isFull(const vector<vector <char> > &board);
};

bool A::checkRow(char ch, const vector<vector <char> > &board)
{
	bool flag=false;
	int count=0;
	for (vector<vector <char> >::size_type i=0; i<board.size(); ++i)
	{
		count=0;
		for (vector<char>::size_type j=0; j<board.at(i).size(); ++j)
		{
			if (board.at(i).at(j)==ch || board.at(i).at(j)=='T')
				++count;
			else 
				break;
		}
		if (count==4)
		{
			flag=true;
			break;
		}
	}
	return flag;
}

bool A::checkColumn(char ch, const vector<vector <char> > &board)
{
	bool flag=false;
	int count=0;
	for (int i=0; i<4; ++i)
	{
		count=0;
		for (int j=0; j<4; ++j)
		{
			if (board.at(j).at(i)==ch || board.at(j).at(i)=='T')
				++count;
			else 
				break;
		}
		if (count==4)
		{
			flag=true;
			break;
		}
	}
	return flag;
}

bool A::checkDiag(char ch, const vector<vector <char> > &board)
{
	bool flag=false;
	int count1=0,count2=0;
	for (int i=0; i<4; ++i)
	{
		if (board.at(i).at(i)==ch || board.at(i).at(i)=='T')
			++count1;
		if (board.at(i).at(3-i)==ch || board.at(i).at(3-i)=='T')
			++count2;
	}
	if (count1==4 || count2==4)
		flag=true;
	return flag;
}

bool A::win(char ch, const vector<vector <char> > &board)	//check whether charactor ch('O' or 'X') win
{
	bool flag=false;
	flag=checkRow(ch, board);
	if (flag)
		return true;
	flag=checkColumn(ch, board);
	if (flag)
		return true;
	flag=checkDiag(ch, board);
	if (flag)
		return true;
	return false;
}

bool A::isFull(const vector<vector <char> > &board)
{
	bool flag=false;
	for (vector<vector <char> >::size_type i=0; i<board.size(); ++i)
	{
		for (vector<char>::size_type j=0; j<board.at(i).size(); ++j)
		{
			if (board.at(i).at(j)=='.')
			{	
				flag=true;
				break;
			}
		}
	}
	return (!flag);
}

int main(int argc, char * args[])
{
	string line;
	int count=0;
	bool winA=false, winB=false;
	A a;
	ifstream infile("testcase",ios::binary | ios::in);
	if(!infile)		
		return -1;
	getline(infile,line);
	count=atoi(line.c_str());
	for (int i=0; i<count; ++i)
	{
		vector< vector <char> > board;
		vector<char> sub;
		for (int j=0; j<4; ++j)
		{
			getline(infile,line);
			sub.assign(line.begin(),line.end());
			board.push_back(sub);
		}
		winA=a.win('X',board);
		winB=a.win('O',board);
		if (!winA && !winB)
		{
			if(a.isFull(board))
				cout<<"Case #"<<i+1<<": Draw"<<endl;
			else
				cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
		}else if(winA)
		{
			cout<<"Case #"<<i+1<<": X won"<<endl;
		}else if(winB)
		{
			cout<<"Case #"<<i+1<<": O won"<<endl;
		}		
		getline(infile,line);
	}
	return 0;
}

