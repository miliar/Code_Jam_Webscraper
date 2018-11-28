#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <cstring>
using namespace std;

#define TL '/'
#define TR '\\'
#define BL '\\'
#define BR '/'

int R,C;
char board[52][52];
bool isPossible();
bool checkRange(int i, int j);
void recorver(int i, int j);
bool filled;
int rest;

void fillit()
{
	if(filled) return ;
	for(int i=0; i < R; ++i)
	{
		for(int j=0; j < C; ++j)
		{
			if(board[i][j]=='#'&& checkRange(i,j)==true)
			{
				fillit();
				if(filled) break;
				recorver(i,j);
				//return ;
				
			}
		}
		if(filled)break;
	}
}

int main()
{
	string line;
	getline(cin, line);
	int T = atoi(line.c_str());
	for(int tcase=1; tcase<=T; ++tcase)
	{
		getline(cin,line);
		istringstream is(line);
		is >> R >> C;
		memset(board, 0, sizeof(board));
		for(int i=0; i < R; ++i)
		{
			getline(cin,line);
			for(int j=0; j < C; ++j)
				board[i][j] = line[j];
		}

		rest=0;
		cout << "Case #" << tcase << ":" << endl;
		bool ret = isPossible();
		if(ret==true && rest!=0)
		{
			cout << "Impossible" << endl;
			continue;
		}
		else
		{
			filled=false;
			fillit();
		}
		if(filled||rest==0)
			for(int i=0; i < R; ++i)
				cout << board[i] << endl;
		else
			cout << "Impossible" << endl;
	}
	
	return 0;
}

bool isPossible()
{
	for(int i=0; i < R; ++i)
		for(int j=0; j < C; ++j)
			if(board[i][j]=='#')
				++rest;
	if(rest%4 != 0)
		return false;

	for(int i=0; i < R; ++i)
	{
		int cnt=0;
		for(int j=0; j < C; ++j)
		{
			if(board[i][j]=='#')
				++cnt;
			else
			{
				if(cnt!=0 && cnt&1)
					return true;
				cnt=0;
			}
		}
		if(cnt&1)
			return true;
	}
	for(int i=0; i < C; ++i)
	{
		int cnt=0;
		for(int j=0; j < R; ++j)
		{
			if(board[j][i]=='#')
				++cnt;
			else
			{
				if(cnt!=0 && cnt&1)
					return true;
				cnt=0;
			}
		}

		if(cnt&1)
			return true;
	}

	return false;

}

bool checkRange(int i, int j)
{
	if( i+1 >= R || j+1 >= C )
		return false;
	if(board[i][j+1]!='#' || board[i+1][j]!='#' || board[i+1][j+1]!='#')
		return false;
	board[i][j]=TL; board[i][j+1]=TR;
	board[i+1][j]=BL; board[i+1][j+1]=BR;
	rest-=4;
	if(rest==0) filled=true;
	return true;
}

void recorver(int i, int j)
{	
	board[i][j]='#'; board[i][j+1]='#';
	board[i+1][j]='#'; board[i+1][j+1]='#';
	rest+=4;
}
