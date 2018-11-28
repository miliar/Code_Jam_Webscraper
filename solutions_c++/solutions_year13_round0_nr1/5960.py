#include <string>
#include <iostream>

using namespace std;

string tab[4];

bool check(char c){
	// check every line
	for(int line = 0; line < 4; ++line){
		int t = 0, cc = 0;
		for(int col = 0; col < 4; ++col){
			if(tab[line][col] == 'T')
				++t;
			if(tab[line][col] == c)
				++cc;
		}
		if(((t == 0 && cc == 4)) || ((t == 1) && (cc == 3)))
			return true;
	}
	
	// check every column
	for(int column = 0; column < 4; ++column){
		int t = 0, cc = 0;
		for(int line = 0; line < 4; ++line){
			if(tab[line][column] == 'T')
				++t;
			if(tab[line][column] == c)
				++cc;
		}
		if(((t == 0 && cc == 4)) || ((t == 1) && (cc == 3)))
			return true;
	}
	
	// check main diagonal
	int t = 0, cc = 0;
	for(int di = 0; di < 4; ++di){
		if(tab[di][di] == 'T')
			++t;
		if(tab[di][di] == c)
			++cc;
	}
	
	if(((t == 0 && cc == 4)) || ((t == 1) && (cc == 3)))
		return true;
		
	t = 0, cc = 0;
	for(int di = 0; di < 4; ++di){
		if(tab[di][3-di] == 'T')
			++t;
		if(tab[di][3-di] == c)
			++cc;
	}
	
	if(((t == 0 && cc == 4)) || ((t == 1) && (cc == 3)))
		return true;
		
	return false;
}

int main()
{
	int t;
	cin >> t;
	
	for(int testNo = 0; testNo < t; ++testNo){		
		cin >> tab[0] >> tab[1] >> tab[2] >> tab[3];
		bool x = check('X');
		bool o = check('O');
		
		bool complete = true;
		
		for(int i = 0; i < 4; ++i)
			for(unsigned j = 0; j < 4; ++j)
				if(tab[i][j] == '.')
					complete = false;
		
		cout << "Case #" << (testNo+1) << ": ";
		if(x)
			cout << "X won";
		else if(o)
			cout << "O won";
		else if(!complete)
			cout << "Game has not completed";
		else 
			cout << "Draw";
		cout << endl;
	}
	return 0;
}
