#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

#define pb push_back
#define all(x) (x).begin(), (x).end()
#define mk make_pair


string A[4];


string solve()
{
	bool X_won = false;
	bool O_won = false;
	bool hadEmptyCell = false;
	
	
	//horizontal
	for(int x = 0; x < 4; x++)
	{
		bool won = true;
		for(int y = 0; y < 4; y++)
			if( !(A[x][y] == 'X' || A[x][y] == 'T') ) won = false;
		if( won )
			X_won = true;
	}
	//vert
	for(int y = 0; y < 4; y++)
	{
		bool won = true;
		for(int x = 0; x < 4; x++)
			if( !(A[x][y] == 'X' || A[x][y] == 'T') ) won = false;
		if( won )
			X_won = true;
	}
	//main diagonal
	bool won = true;
	for(int x = 0; x < 4; x++)
		if( !(A[x][x] == 'X' || A[x][x] == 'T') ) won = false;
	if( won )
		X_won = true;
		
	//other diagonal
	 won = true;
	for(int x = 0; x < 4; x++)
		if( !(A[x][3-x] == 'X' || A[x][3-x] == 'T') ) won = false;
	if( won )
		X_won = true;	
		
		
		//horizontal
	for(int x = 0; x < 4; x++)
	{
		bool won = true;
		for(int y = 0; y < 4; y++)
			if( !(A[x][y] == 'O' || A[x][y] == 'T') ) won = false;
		if( won )
			O_won = true;
	}
	//vert
	for(int y = 0; y < 4; y++)
	{
		bool won = true;
		for(int x = 0; x < 4; x++)
			if( !(A[x][y] == 'O' || A[x][y] == 'T') ) won = false;
		if( won )
			O_won = true;
	}
	//main diagonal
	 won = true;
	for(int x = 0; x < 4; x++)
		if( !(A[x][x] == 'O' || A[x][x] == 'T') ) won = false;
	if( won )
		O_won = true;
		
	//other diagonal
	 won = true;
	for(int x = 0; x < 4; x++)
		if( !(A[x][3-x] == 'O' || A[x][3-x] == 'T') ) won = false;
	if( won )
		O_won = true;
		
	
	if( X_won )
		return "X won";
	if( O_won )
		return "O won";
	
	for(int x = 0; x < 4; x++)
	{
		for(int y = 0; y < 4; y++)
			if( A[x][y] == '.' )
				hadEmptyCell = true;
	}	
	if( hadEmptyCell )
		return "Game has not completed";
		
	return "Draw";
}

int main()
{	
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w", stdout);
	int T;
	cin >> T;
	
	for(int i = 0; i < T; i++)
	{
		for(int x = 0; x < 4; x++)
		{
			cin >> A[x];
			//cout << A[x];
		}	
		printf("Case #%d: %s\n",i+1, string(solve()).c_str() );
	}
	
	
	return 0;
}
