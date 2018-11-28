/*
 * A.cxx
 * 
 * Copyright 2013 aras <aras@aras-Satellite-C645D>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


string Result(vector<vector<char> > M)
{
	int X,O,T;
	
	//horizoltal
	for(int i = 0;i < 4;i++)
	{	 
		X = O = T = 0;
		for(int j = 0;j < 4;j++)
			if(M[i][j] == 'X')
				X++;
			else if(M[i][j] == 'O')
				O++;
			else if(M[i][j] == 'T')
				T++;
		
		if(T + O == 4) return "O won";
		if(T + X == 4) return "X won";		
	}
	
	//vertical
	for(int i = 0;i < 4;i++)
	{	 
		X = O = T = 0;
		for(int j = 0;j < 4;j++)
			if(M[j][i] == 'X')
				X++;
			else if(M[j][i] == 'O')
				O++;
			else if(M[j][i] == 'T')
				T++;
		
		if(T + O == 4) return "O won";
		if(T + X == 4) return "X won";		
	}
	
	//diagonal
	{	 
		X = O = T = 0;
		for(int i = 0;i < 4;i++)
			if(M[i][i] == 'X')
				X++;
			else if(M[i][i] == 'O')
				O++;
			else if(M[i][i] == 'T')
				T++;
		
		if(T + O == 4) return "O won";
		if(T + X == 4) return "X won";		
	}
	
	//diagonal -
	{	 
		X = O = T = 0;
		for(int i = 0 , j = 3;i < 4;i++,j--)
			if(M[i][j] == 'X')
				X++;
			else if(M[i][j] == 'O')
				O++;
			else if(M[i][j] == 'T')
				T++;
		
		if(T + O == 4) return "O won";
		if(T + X == 4) return "X won";		
	}

	for(int i = 0;i < 4;i++)
		for(int j = 0;j < 4;j++)
			if(M[i][j] == '.')
				return "Game has not completed";
				
	return "Draw"; 
}

int main(int argc, char **argv)
{
	int T,test=1;
	vector<vector<char> > M(4 , vector<char>(4));
	
	ofstream OUT("Tic-Tac-Toe-Tomek.out");
	ifstream IN("A-large.in");
	
	IN >> T;
	
	while(T--)
	{
		for(int i = 0;i < 4;i++)
			for(int j = 0;j < 4;j++)
				IN >> M[i][j];
				
		cout << "Case #" << test << ": " << Result(M) << endl;
		OUT << "Case #" << test++ << ": " << Result(M) << endl;
	}
	
	// OUT << endl;
	
	return 0;
}

